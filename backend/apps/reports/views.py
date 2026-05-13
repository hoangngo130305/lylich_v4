import io
from django.db.models import Count, Q
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.accounts.permissions import IsOfficer, IsAdmin
from apps.profiles.models import Profile
from apps.auditlogs.utils import log_activity
from apps.auditlogs.models import ActivityLog
from .models import StatsMonthly, ReportExport
from .serializers import StatsMonthlySerializer, ReportExportSerializer


@api_view(['GET'])
@permission_classes([IsOfficer])
def dashboard_stats(request):
    """Aggregated counts for the admin dashboard KPI cards."""
    now  = timezone.now()
    qs   = Profile.objects.filter(deleted_at__isnull=True)

    counts = qs.aggregate(
        total        =Count('id'),
        draft        =Count('id', filter=Q(status='draft')),
        submitted    =Count('id', filter=Q(status='submitted')),
        under_review =Count('id', filter=Q(status='under_review')),
        approved     =Count('id', filter=Q(status='approved')),
        rejected     =Count('id', filter=Q(status='rejected')),
        archived     =Count('id', filter=Q(status='archived')),
    )

    # Monthly trend — last 6 months
    monthly = (
        StatsMonthly.objects
        .filter(unit_id__isnull=True)
        .order_by('-year', '-month')[:6]
    )
    trend = StatsMonthlySerializer(reversed(list(monthly)), many=True).data

    return Response({
        'counts': counts,
        'trend':  trend,
        'as_of':  now.isoformat(),
    })


@api_view(['GET'])
@permission_classes([IsOfficer])
def monthly_stats(request):
    year  = request.query_params.get('year', timezone.now().year)
    month = request.query_params.get('month')
    qs    = StatsMonthly.objects.all()
    if year:
        qs = qs.filter(year=year)
    if month:
        qs = qs.filter(month=month)
    serializer = StatsMonthlySerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsOfficer])
def export_excel_report(request):
    """Export monthly stats to Excel via openpyxl."""
    try:
        import openpyxl
    except ImportError:
        return Response({'detail': 'openpyxl not installed'}, status=status.HTTP_501_NOT_IMPLEMENTED)

    year  = request.data.get('year', timezone.now().year)
    month = request.data.get('month')

    qs = StatsMonthly.objects.filter(year=year)
    if month:
        qs = qs.filter(month=month)

    wb  = openpyxl.Workbook()
    ws  = wb.active
    ws.title = f'ThongKe_{year}'
    headers = ['Năm', 'Tháng', 'Nháp', 'Đã nộp', 'Đang xét', 'Duyệt', 'Từ chối', 'Lưu trữ', 'Tổng']
    ws.append(headers)
    for row in qs:
        ws.append([row.year, row.month, row.count_draft, row.count_submitted,
                   row.count_under_review, row.count_approved,
                   row.count_rejected, row.count_archived, row.count_total])

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


class ReportExportListView(generics.ListAPIView):
    serializer_class   = ReportExportSerializer
    permission_classes = [IsOfficer]

    def get_queryset(self):
        return ReportExport.objects.select_related('created_by').order_by('-created_at')
