import re
import traceback

from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.accounts.permissions import IsOfficer, IsOfficerOrApplicant, _has_officer_perm
from apps.auditlogs.utils import log_activity
from apps.auditlogs.models import ActivityLog
from apps.profiles.models import Profile
from .models import (ProfileEditHistory, ProfileCorrectionRequest,
                     ProfileCorrectionItem, WordExportLog)
from .serializers import (ProfileEditHistorySerializer,
                           ProfileCorrectionRequestSerializer,
                           CorrectionRequestCreateSerializer,
                           ProfileCorrectionItemSerializer,
                           WordExportLogSerializer)
from .word_builder_from_template import build_lylich_docx


# ── Edit History ──────────────────────────────────────────────────────────────

class EditHistoryListView(generics.ListAPIView):
    serializer_class   = ProfileEditHistorySerializer
    permission_classes = [IsOfficer]

    def get_queryset(self):
        profile_id = self.kwargs.get('profile_id')
        qs = ProfileEditHistory.objects.select_related('edited_by')
        if profile_id:
            qs = qs.filter(profile_id=profile_id)
        return qs


# ── Correction Requests ───────────────────────────────────────────────────────

class CorrectionRequestListCreateView(generics.ListCreateAPIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsOfficer()]
        return [IsOfficerOrApplicant()]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CorrectionRequestCreateSerializer
        return ProfileCorrectionRequestSerializer

    def get_queryset(self):
        qs = ProfileCorrectionRequest.objects.prefetch_related('items').select_related('created_by', 'resolved_by')
        role_code = getattr(self.request.user, 'role_code', None)
        if role_code not in ('admin', 'can_bo_bxd'):
            qs = qs.filter(profile__user=self.request.user)
        profile_id = self.request.query_params.get('profile_id')
        if profile_id:
            qs = qs.filter(profile_id=profile_id)
        return qs

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        log_activity(
            self.request.user, ActivityLog.Action.CREATE,
            target_model='ProfileCorrectionRequest', target_id=obj.id,
            description=f'Tạo yêu cầu bổ sung hồ sơ #{obj.profile_id}',
            request=self.request,
        )


class CorrectionRequestDetailView(generics.RetrieveUpdateAPIView):
    serializer_class   = ProfileCorrectionRequestSerializer
    permission_classes = [IsOfficer]
    queryset           = ProfileCorrectionRequest.objects.prefetch_related('items').select_related('created_by', 'resolved_by')

    def perform_update(self, serializer):
        new_status = serializer.validated_data.get('status')
        extra = {}
        if new_status == ProfileCorrectionRequest.Status.RESOLVED:
            extra = {'resolved_by': self.request.user, 'resolved_at': timezone.now()}
        obj = serializer.save(**extra)
        log_activity(
            self.request.user, ActivityLog.Action.UPDATE,
            target_model='ProfileCorrectionRequest', target_id=obj.id,
            description=f'Cập nhật yêu cầu bổ sung: status={obj.status}',
            request=self.request,
        )


@api_view(['PATCH'])
@permission_classes([IsOfficer])
def update_correction_item(request, pk):
    item = get_object_or_404(ProfileCorrectionItem, pk=pk)
    serializer = ProfileCorrectionItemSerializer(item, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    new_status = serializer.validated_data.get('status')
    extra = {}
    if new_status == ProfileCorrectionItem.ItemStatus.CORRECTED:
        extra = {'corrected_at': timezone.now()}
    serializer.save(**extra)

    parent = item.request
    items  = parent.items.all()
    if items.filter(status=ProfileCorrectionItem.ItemStatus.PENDING).count() == 0:
        parent.status = ProfileCorrectionRequest.Status.RESOLVED
        parent.resolved_by = request.user
        parent.resolved_at = timezone.now()
        parent.save(update_fields=['status', 'resolved_by', 'resolved_at'])

    return Response(serializer.data)


# ── Word Export ───────────────────────────────────────────────────────────────

@api_view(['POST'])
@permission_classes([IsOfficerOrApplicant])
def export_word(request, profile_id):
    print(f"[EXPORT] generating word for profile {profile_id} by user {request.user.id}")
    try:
        # Load profile with all related fields to avoid N+1 and missing attr errors
        profile = get_object_or_404(
            Profile.objects.select_related(
                'user',
                'ethnic_group',
                'religion',
                'edu_level',
                'political_level',
                'officer_in_charge',
                'current_ward',
                'birth_place_ward',
                'hometown_ward',
            ).prefetch_related(
                'committee_comments',
                'family_members',
                'history_entries',
                'work_history',
                'education_history',
                'awards',
                'overseas_travels',
            ),
            pk=profile_id,
        )

        # Only officers can export Word — applicants cannot
        if request.user.role_code not in ('admin', 'can_bo_bxd'):
            return Response(
                {'success': False, 'detail': 'Quần chúng không có quyền xuất file Word.'},
                status=status.HTTP_403_FORBIDDEN,
            )
        # Granular permission: can_bo_bxd must have can_export_word flag
        if request.user.role_code == 'can_bo_bxd' and not _has_officer_perm(request.user, 'can_export_word'):
            return Response(
                {'success': False, 'detail': 'Bạn chưa được cấp quyền xuất file Word.'},
                status=status.HTTP_403_FORBIDDEN,
            )

        template = request.data.get('template_name', 'Mẫu 2-KNĐ')

        buf = build_lylich_docx(profile)
        content = buf.read()

        safe_name = re.sub(r'[^\w\-]', '_', profile.full_name or 'profile')
        file_name = f'SoYeuLyLich_{safe_name}.docx'

        WordExportLog.objects.create(
            profile=profile,
            exported_by=request.user,
            template_name=template,
            file_name=file_name,
            file_size=len(content),
            sections_json=None,
        )

        log_activity(
            request.user, ActivityLog.Action.EXPORT,
            target_model='Profile', target_id=profile.id,
            description=f'Xuất Word hồ sơ {profile.full_name}',
            request=request,
        )

        print(f"[EXPORT] success – {file_name} ({len(content)} bytes)")

        response = HttpResponse(
            content,
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        )
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        response['Content-Length']      = len(content)
        return response

    except Exception as e:
        tb = traceback.format_exc()
        print(f"[EXPORT] ERROR for profile {profile_id}:\n{tb}")
        return Response(
            {
                'success': False,
                'error':   str(e),
                'detail':  'Lỗi khi tạo file Word. Xem server log để biết chi tiết.',
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class WordExportLogListView(generics.ListAPIView):
    serializer_class   = WordExportLogSerializer
    permission_classes = [IsOfficer]

    def get_queryset(self):
        qs = WordExportLog.objects.select_related('profile', 'exported_by')
        profile_id = self.request.query_params.get('profile_id')
        if profile_id:
            qs = qs.filter(profile_id=profile_id)
        return qs
