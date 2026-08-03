import io
from django.db.models import Count, Q
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.accounts.permissions import IsOfficer, IsAdmin, CanViewReports
from apps.profiles.models import Profile
from apps.auditlogs.utils import log_activity
from apps.auditlogs.models import ActivityLog
from .models import ReportExport
from .serializers import ReportExportSerializer


def _monthly_profile_stats(qs):
    """Group a Profile queryset by the month it was created, into per-status
    counts. Computed live from real data (there's no periodic job populating
    StatsMonthly, so that table is always empty and unusable as a source)."""
    from collections import OrderedDict
    rows = OrderedDict()
    for p in qs.only('created_at', 'status').order_by('created_at'):
        if not p.created_at:
            continue
        key = (p.created_at.year, p.created_at.month)
        row = rows.get(key)
        if row is None:
            row = rows[key] = {
                'year': key[0], 'month': key[1],
                'count_draft': 0, 'count_submitted': 0, 'count_pending': 0,
                'count_under_review': 0, 'count_returned': 0, 'count_verifying': 0,
                'count_approved': 0, 'count_completed': 0, 'count_rejected': 0,
                'count_withdrawn': 0, 'count_total': 0,
            }
        field = f'count_{p.status}'
        if field in row:
            row[field] += 1
        row['count_total'] += 1
    return list(rows.values())


@api_view(['GET'])
@permission_classes([CanViewReports])
def dashboard_stats(request):
    """Aggregated counts for the admin dashboard KPI cards."""
    now  = timezone.now()
    qs   = Profile.objects.filter(deleted_at__isnull=True)

    counts = qs.aggregate(
        total        =Count('id'),
        draft        =Count('id', filter=Q(status='draft')),
        submitted    =Count('id', filter=Q(status='submitted')),
        under_review =Count('id', filter=Q(status='under_review')),
        returned     =Count('id', filter=Q(status='returned')),
        approved     =Count('id', filter=Q(status='approved')),
        completed    =Count('id', filter=Q(status='completed')),
        rejected     =Count('id', filter=Q(status='rejected')),
    )

    # Monthly trend — last 6 months with data, computed live from Profile
    trend = _monthly_profile_stats(qs)[-6:]

    return Response({
        'counts': counts,
        'trend':  trend,
        'as_of':  now.isoformat(),
    })


@api_view(['GET'])
@permission_classes([CanViewReports])
def monthly_stats(request):
    year  = request.query_params.get('year')
    month = request.query_params.get('month')
    qs = Profile.objects.filter(deleted_at__isnull=True)
    if year:
        qs = qs.filter(created_at__year=year)
    if month:
        qs = qs.filter(created_at__month=month)
    return Response(_monthly_profile_stats(qs))


@api_view(['POST'])
@permission_classes([CanViewReports])
def export_excel_report(request):
    """Export monthly hồ sơ stats to Excel via openpyxl, computed live from Profile data."""
    try:
        import openpyxl
    except ImportError:
        return Response({'detail': 'openpyxl not installed'}, status=status.HTTP_501_NOT_IMPLEMENTED)

    year  = request.data.get('year', timezone.now().year)
    month = request.data.get('month')

    qs = Profile.objects.filter(deleted_at__isnull=True, created_at__year=year)
    if month:
        qs = qs.filter(created_at__month=month)
    rows = _monthly_profile_stats(qs)

    wb  = openpyxl.Workbook()
    ws  = wb.active
    ws.title = f'ThongKe_{year}'
    headers = ['Năm', 'Tháng', 'Đang kê khai', 'Đã nộp', 'Đang xem xét', 'Đang thẩm định',
               'Trả lại', 'Đang xác minh', 'Đã phê duyệt', 'Hoàn thiện', 'Từ chối', 'Rút hồ sơ', 'Tổng']
    ws.append(headers)
    for row in rows:
        ws.append([row['year'], row['month'], row['count_draft'], row['count_submitted'],
                   row['count_pending'], row['count_under_review'], row['count_returned'],
                   row['count_verifying'], row['count_approved'], row['count_completed'],
                   row['count_rejected'], row['count_withdrawn'], row['count_total']])

    buf       = io.BytesIO()
    wb.save(buf)
    buf.seek(0)
    content   = buf.read()
    file_name = f'BaoCao_{year}{"_" + str(month) if month else ""}.xlsx'

    ReportExport.objects.create(
        created_by  =request.user,
        report_type =ReportExport.ReportType.MONTHLY,
        format      =ReportExport.Format.EXCEL,
        params      ={'year': year, 'month': month},
        file_name   =file_name,
        file_size   =len(content),
    )

    log_activity(request.user, ActivityLog.Action.EXPORT,
                 description=f'Xuất báo cáo Excel {file_name}', request=request)

    from django.http import HttpResponse
    response = HttpResponse(
        content,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    response['Content-Length'] = len(content)
    return response


@api_view(['GET'])
@permission_classes([CanViewReports])
def export_profiles_excel(request):
    """Export the quần chúng roster (Danh sách quần chúng / Dashboard 'Xuất Excel')."""
    try:
        import openpyxl
    except ImportError:
        return Response({'detail': 'openpyxl not installed'}, status=status.HTTP_501_NOT_IMPLEMENTED)

    from apps.accounts.models import User

    status_filter = request.query_params.get('status')
    qs = User.objects.filter(role__code='quan_chung', deleted_at__isnull=True).select_related('profile').order_by('-created_at')
    if status_filter:
        qs = qs.filter(profile__status=status_filter)

    status_labels = dict(Profile.Status.choices)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'DanhSachQuanChung'
    ws.append(['Họ và tên', 'Số điện thoại', 'CCCD', 'Chi bộ', 'Đảng bộ', 'Trạng thái tài khoản', 'Trạng thái hồ sơ', 'Ngày tạo'])
    for u in qs:
        profile = getattr(u, 'profile', None)
        ws.append([
            u.full_name, u.phone, u.cccd or '',
            u.chi_bo or '', u.dang_bo or '',
            'Hoạt động' if u.status == 'active' else 'Bị khoá',
            status_labels.get(profile.status, '—') if profile else 'Chưa có hồ sơ',
            u.created_at.strftime('%d/%m/%Y') if u.created_at else '',
        ])

    buf     = io.BytesIO()
    wb.save(buf)
    buf.seek(0)
    content = buf.read()
    file_name = 'DanhSachQuanChung.xlsx'

    ReportExport.objects.create(
        created_by  =request.user,
        report_type =ReportExport.ReportType.CUSTOM,
        format      =ReportExport.Format.EXCEL,
        params      ={'status': status_filter} if status_filter else None,
        file_name   =file_name,
        file_size   =len(content),
    )
    log_activity(request.user, ActivityLog.Action.EXPORT,
                 description='Xuất danh sách quần chúng Excel', request=request)

    from django.http import HttpResponse
    response = HttpResponse(
        content,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    response['Content-Length'] = len(content)
    return response


class ReportExportListView(generics.ListAPIView):
    serializer_class   = ReportExportSerializer
    permission_classes = [CanViewReports]

    def get_queryset(self):
        return ReportExport.objects.select_related('created_by').order_by('-created_at')
