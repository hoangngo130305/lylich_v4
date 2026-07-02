from django.utils import timezone
from django.db import transaction
from django.db.models import Count, Avg, Q
from datetime import date
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from apps.accounts.models import User, Role

from .models import Profile, ProfileReview, CommitteeComment, ProfileOfficerAssignment, ProfileFieldNote
from .serializers import (
    ProfileListSerializer, ProfileDetailSerializer,
    ProfileReviewSerializer, CommitteeCommentSerializer, ProfileWorkflowSerializer,
    ProfileFieldNoteSerializer,
)
from apps.accounts.permissions import IsOfficer, IsApplicant, IsOwnerOrOfficer, IsOfficerOrApplicant, _has_officer_perm
from apps.auditlogs.utils import log_activity

# Status transition rules
VALID_TRANSITIONS = {
    Profile.Status.DRAFT:        [Profile.Status.SUBMITTED, Profile.Status.RETURNED],
    Profile.Status.SUBMITTED:    [Profile.Status.PENDING, Profile.Status.RETURNED, Profile.Status.REJECTED],
    Profile.Status.PENDING:      [Profile.Status.UNDER_REVIEW, Profile.Status.RETURNED, Profile.Status.REJECTED],
    Profile.Status.UNDER_REVIEW: [Profile.Status.APPROVED, Profile.Status.RETURNED, Profile.Status.REJECTED],
    Profile.Status.RETURNED:     [Profile.Status.SUBMITTED, Profile.Status.RETURNED],
    Profile.Status.APPROVED:     [Profile.Status.VERIFYING, Profile.Status.COMPLETED, Profile.Status.RETURNED],
    Profile.Status.VERIFYING:    [Profile.Status.COMPLETED, Profile.Status.RETURNED],
    Profile.Status.COMPLETED:    [],
    Profile.Status.REJECTED:     [],
    Profile.Status.WITHDRAWN:    [],
}

ACTION_TO_STATUS = {
    'submit':         Profile.Status.SUBMITTED,
    'approve':        Profile.Status.APPROVED,
    'return':         Profile.Status.RETURNED,
    'reject':         Profile.Status.REJECTED,
    'request_verify': Profile.Status.VERIFYING,
    'complete':       Profile.Status.COMPLETED,
    'withdraw':       Profile.Status.WITHDRAWN,
}


class ProfileListView(generics.ListCreateAPIView):
    serializer_class = ProfileListSerializer
    permission_classes = [IsOfficer]
    filterset_fields  = ['status', 'gender']
    search_fields     = ['full_name', 'profile_number']
    ordering_fields   = ['full_name', 'dob', 'submitted_at', 'ai_score', 'created_at']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProfileDetailSerializer
        return ProfileListSerializer

    def get_queryset(self):
        return Profile.objects.select_related(
            'user', 'officer_in_charge'
        ).filter(deleted_at__isnull=True).order_by('-created_at')

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        payload = request.data.copy()

        def _clean_text(v):
            if v is None:
                return None
            if isinstance(v, str):
                s = v.strip()
                return s or None
            return v

        # Minimal defaults for quick draft creation from officer/admin UI.
        payload['full_name'] = _clean_text(payload.get('full_name'))
        if not payload.get('full_name'):
            payload['full_name'] = f'Hồ sơ mới {timezone.now().strftime("%d/%m/%Y %H:%M")}'

        payload['gender'] = _clean_text(payload.get('gender'))
        if payload.get('gender') not in {Profile.Gender.MALE, Profile.Gender.FEMALE, Profile.Gender.OTHER}:
            payload['gender'] = Profile.Gender.MALE

        payload['dob'] = _clean_text(payload.get('dob'))
        if payload.get('dob'):
            try:
                date.fromisoformat(str(payload['dob']))
            except Exception:
                payload['dob'] = '1990-01-01'
        else:
            payload['dob'] = '1990-01-01'

        serializer = self.get_serializer(data=payload)
        serializer.is_valid(raise_exception=True)

        role_qc, _ = Role.objects.get_or_create(
            code='quan_chung',
            defaults={'name': 'Quần chúng xin vào Đảng'}
        )

        # Generate a temporary unique phone for placeholder applicant account.
        temp_user = None
        for _ in range(20):
            phone = f"0999{timezone.now().strftime('%H%M%S%f')[-6:]}"
            if not User.objects.filter(phone=phone).exists():
                temp_user = User.objects.create_user(
                    phone=phone,
                    password=None,
                    full_name=serializer.validated_data.get('full_name') or 'Hồ sơ mới',
                    role=role_qc,
                    status=User.Status.ACTIVE,
                    created_by=request.user,
                )
                break

        if temp_user is None:
            return Response(
                {'success': False, 'error': 'Không thể tạo tài khoản tạm cho hồ sơ mới.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        profile = serializer.save(
            user=temp_user,
            created_by=request.user,
            updated_by=request.user,
            officer_in_charge=request.user,
            status=Profile.Status.DRAFT,
        )

        log_activity(
            request.user,
            'profile_create',
            target_model='Profile',
            target_id=profile.id,
            description=f'Tạo hồ sơ nháp: {profile.full_name}',
        )

        return Response({'success': True, 'data': ProfileDetailSerializer(profile).data}, status=status.HTTP_201_CREATED)


class MyProfileView(generics.RetrieveUpdateAPIView):
    """Quần chúng: view/edit their own profile."""
    permission_classes = [IsApplicant]

    def get_serializer_class(self):
        return ProfileDetailSerializer

    def get_object(self):
        profile, _ = Profile.objects.get_or_create(
            user=self.request.user,
            defaults={
                'full_name': self.request.user.full_name,
                'gender': 'male',
                'dob': '1990-01-01',
                'status': Profile.Status.DRAFT,
                'created_by': self.request.user,
            }
        )
        return profile

    def retrieve(self, request, *args, **kwargs):
        """Allow applicants to GET their partial profile without all required fields."""
        profile = self.get_object()
        # For GET, don't require all fields - applicant may still be filling the profile
        serializer = self.get_serializer(profile)
        return Response({'success': True, 'data': serializer.data})

    def update(self, request, *args, **kwargs):
        profile = self.get_object()
        if not profile.is_editable_by_applicant:
            return Response(
                {'success': False, 'error': 'Hồ sơ đang ở trạng thái không cho phép chỉnh sửa.'},
                status=status.HTTP_403_FORBIDDEN
            )
        kwargs['partial'] = True
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            # Log validation errors for debugging
            return Response(
                {'success': False, 'error': 'Lỗi lưu hồ sơ:', 'details': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(updated_by=request.user)
        log_activity(request.user, 'profile_update', target_model='Profile', target_id=profile.id)
        return Response({'success': True, 'data': serializer.data})


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    """Officer: view any profile, edit fields directly."""
    permission_classes = [IsOfficer]

    def get_queryset(self):
        return Profile.objects.select_related(
            'user', 'officer_in_charge', 'ethnic_group', 'religion',
            'edu_level', 'political_level', 'current_ward', 'hometown_ward',
            'birth_place_ward', 'temporary_ward', 'photo_file',
        ).filter(deleted_at__isnull=True)

    def get_serializer_class(self):
        return ProfileDetailSerializer

    def update(self, request, *args, **kwargs):
        # Officers review profiles via field notes only — they must not overwrite citizen data.
        if request.user.role_code == 'can_bo_bxd':
            return Response(
                {'success': False,
                 'error': 'Cán bộ không được chỉnh sửa dữ liệu hồ sơ. '
                          'Vui lòng dùng tính năng nhận xét để yêu cầu quần chúng tự sửa.'},
                status=status.HTTP_403_FORBIDDEN
            )
        kwargs['partial'] = True
        profile = self.get_object()
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=request.user)

        # Log each changed field in edit history
        _log_field_changes(request, profile, request.data)
        return Response({'success': True, 'data': serializer.data})


def _log_field_changes(request, profile, changed_data):
    from apps.exports.models import ProfileEditHistory
    section_map = {
        'full_name': 'secA', 'dob': 'secA', 'gender': 'secA',
        'occupation': 'secA', 'current_address': 'secA',
        'political_history_text': 'secD', 'self_assessment_text': 'secJ',
    }
    for field, new_val in changed_data.items():
        if hasattr(profile, field):
            old_val = getattr(profile, field)
            if str(old_val) != str(new_val):
                ProfileEditHistory.objects.create(
                    profile=profile,
                    edited_by=request.user,
                    section=section_map.get(field, 'secA'),
                    field_name=field,
                    old_value=str(old_val) if old_val is not None else '',
                    new_value=str(new_val) if new_val is not None else '',
                )


class ProfileWorkflowView(generics.GenericAPIView):
    """Unified workflow action endpoint."""
    serializer_class = ProfileWorkflowSerializer
    permission_classes = [IsOfficerOrApplicant]

    def get_profile(self):
        if self.request.user.role_code == 'quan_chung':
            return Profile.objects.get(user=self.request.user, deleted_at__isnull=True)
        return Profile.objects.get(pk=self.kwargs['pk'], deleted_at__isnull=True)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            profile = self.get_profile()
        except Profile.DoesNotExist:
            return Response({'success': False, 'error': 'Hồ sơ không tồn tại.'}, status=404)

        action = serializer.validated_data['action']
        comment = serializer.validated_data.get('comment', '')

        def _target_status_for_action(current_status, workflow_action):
            # Keep one "approve" button in UI while still honoring internal staged flow.
            if workflow_action == 'approve':
                if current_status == Profile.Status.SUBMITTED:
                    return Profile.Status.PENDING
                if current_status == Profile.Status.PENDING:
                    return Profile.Status.UNDER_REVIEW
                return Profile.Status.APPROVED
            return ACTION_TO_STATUS.get(workflow_action)

        # Validate role permissions
        if action == 'submit' and request.user.role_code not in ('quan_chung',):
            return Response({'success': False, 'error': 'Chỉ quần chúng mới được nộp hồ sơ.'}, status=403)
        if action == 'withdraw' and request.user.role_code not in ('quan_chung', 'admin'):
            return Response({'success': False, 'error': 'Không có quyền rút hồ sơ.'}, status=403)
        if action in ('approve', 'reject', 'return', 'complete', 'request_verify'):
            if request.user.role_code not in ('can_bo_bxd', 'admin'):
                return Response({'success': False, 'error': 'Chỉ cán bộ mới được thực hiện thao tác này.'}, status=403)
        # Granular OfficerPermission checks for can_bo_bxd
        if action in ('return', 'reject') and not _has_officer_perm(request.user, 'can_review_profiles'):
            return Response({'success': False, 'error': 'Bạn chưa được cấp quyền trả lại/từ chối hồ sơ.'}, status=403)
        if action in ('approve', 'complete', 'request_verify') and not _has_officer_perm(request.user, 'can_approve_profiles'):
            return Response({'success': False, 'error': 'Bạn chưa được cấp quyền phê duyệt hồ sơ.'}, status=403)

        new_status = _target_status_for_action(profile.status, action)
        if new_status:
            allowed = VALID_TRANSITIONS.get(profile.status, [])
            if new_status not in allowed:
                return Response({
                    'success': False,
                    'error': f'Không thể chuyển từ "{profile.get_status_display()}" sang "{Profile.Status(new_status).label}".'
                }, status=400)

        # Guard: block submit if required fields are missing
        if action == 'submit':
            missing = []
            if not profile.full_name:
                missing.append('Họ tên')
            if not profile.dob:
                missing.append('Ngày sinh')
            if not profile.gender:
                missing.append('Giới tính')
            if missing:
                return Response({
                    'success': False,
                    'error': f'Hồ sơ chưa điền đầy đủ thông tin bắt buộc: {", ".join(missing)}.'
                }, status=400)

        old_status = profile.status
        now = timezone.now()

        # Apply status changes
        if action == 'submit':
            profile.status = Profile.Status.SUBMITTED
            profile.submitted_at = now
        elif action == 'approve':
            if old_status == Profile.Status.SUBMITTED:
                profile.status = Profile.Status.PENDING
            elif old_status == Profile.Status.PENDING:
                profile.status = Profile.Status.UNDER_REVIEW
            else:
                profile.status = Profile.Status.APPROVED
                profile.approved_at = now
                profile.approved_by = request.user
        elif action == 'return':
            profile.status = Profile.Status.RETURNED
            profile.last_returned_at = now
            profile.return_reason = serializer.validated_data.get('return_reason', comment)
        elif action == 'reject':
            profile.status = Profile.Status.REJECTED
            profile.rejected_at = now
            profile.rejected_reason = serializer.validated_data.get('rejected_reason', comment)
        elif action == 'complete':
            profile.status = Profile.Status.COMPLETED
            profile.completed_at = now
        elif action == 'withdraw':
            profile.status = Profile.Status.WITHDRAWN
        elif action == 'request_verify':
            profile.status = Profile.Status.VERIFYING

        profile.updated_by = request.user
        profile.save()

        # Create review record
        ProfileReview.objects.create(
            profile=profile,
            reviewer=request.user,
            action=action,
            from_status=old_status,
            to_status=profile.status,
            comment=comment,
        )

        log_activity(
            request.user, action, target_model='Profile', target_id=profile.id,
            description=f'{profile.full_name}: {old_status} → {profile.status}'
        )

        return Response({'success': True, 'data': ProfileListSerializer(profile).data})


class ProfileReviewListView(generics.ListAPIView):
    serializer_class = ProfileReviewSerializer
    permission_classes = [IsOfficerOrApplicant]

    def get_queryset(self):
        profile_id = self.kwargs['profile_id']
        if self.request.user.role_code == 'quan_chung':
            return ProfileReview.objects.filter(
                profile_id=profile_id, profile__user=self.request.user
            ).order_by('-created_at')
        return ProfileReview.objects.filter(profile_id=profile_id).select_related(
            'reviewer'
        ).order_by('-created_at')


class CommitteeCommentView(generics.RetrieveUpdateAPIView):
    serializer_class = CommitteeCommentSerializer
    permission_classes = [IsOfficer]

    def get_object(self):
        profile_id  = self.kwargs['profile_id']
        comment_type = self.request.query_params.get('type', 'chi_uy')
        obj, _ = CommitteeComment.objects.get_or_create(
            profile_id=profile_id, type=comment_type
        )
        return obj

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=request.user)
        return Response({'success': True, 'data': serializer.data})


class AssignOfficerView(generics.GenericAPIView):
    permission_classes = [IsOfficer]

    def post(self, request, pk):
        from apps.accounts.models import User
        try:
            profile = Profile.objects.get(pk=pk, deleted_at__isnull=True)
            officer = User.objects.get(pk=request.data['officer_id'], role__code__in=['can_bo_bxd', 'admin'])
        except (Profile.DoesNotExist, User.DoesNotExist, KeyError):
            return Response({'success': False, 'error': 'Không tìm thấy hồ sơ hoặc cán bộ.'}, status=404)

        profile.officer_in_charge = officer
        profile.save(update_fields=['officer_in_charge'])

        ProfileOfficerAssignment.objects.create(
            profile=profile, officer=officer, assigned_by=request.user,
            note=request.data.get('note', '')
        )
        log_activity(request.user, 'assign_officer', target_model='Profile', target_id=profile.id)
        return Response({'success': True, 'message': f'Đã phân công {officer.full_name}.'})


@api_view(['GET'])
@permission_classes([IsOfficer])
def dashboard_kpi(request):
    qs = Profile.objects.filter(deleted_at__isnull=True)
    status_counts = {s.value: 0 for s in Profile.Status}
    for item in qs.values('status').annotate(c=Count('id')):
        status_counts[item['status']] = item['c']

    total = qs.count()
    avg_ai = qs.aggregate(avg=Avg('ai_score'))['avg'] or 0

    # Recent activity
    recent_reviews = ProfileReview.objects.select_related('profile', 'reviewer').order_by('-created_at')[:10]
    recent_data = ProfileReviewSerializer(recent_reviews, many=True).data

    # Urgent profiles (returned with overdue verifications or high-priority)
    urgent = Profile.objects.filter(
        status__in=[Profile.Status.RETURNED, Profile.Status.VERIFYING],
        deleted_at__isnull=True
    ).values('id', 'full_name', 'status', 'ai_score')[:5]

    return Response({
        'success': True,
        'data': {
            'kpi': {
                'total': total,
                'avg_ai_score': round(float(avg_ai), 1),
                **status_counts,
            },
            'recent_activity': recent_data,
            'urgent_profiles': list(urgent),
        }
    })


@api_view(['GET'])
@permission_classes([IsOfficer])
def ai_scan_results(request, pk):
    from apps.auditlogs.models import AIScanResult
    results = AIScanResult.objects.filter(profile_id=pk).order_by('section', '-created_at')
    data = [
        {
            'id': r.id, 'section': r.section, 'issue_type': r.issue_type,
            'message': r.message, 'field_path': r.field_path,
            'resolved': r.resolved, 'created_at': r.created_at,
        }
        for r in results
    ]
    try:
        profile = Profile.objects.get(pk=pk)
        score = profile.ai_score
    except Profile.DoesNotExist:
        score = None
    return Response({'success': True, 'data': {'score': score, 'issues': data}})


class ProfileFieldNoteView(generics.GenericAPIView):
    """GET/POST per-field review notes for a profile.

    GET  — accessible to the owning citizen (to see feedback) and officers.
    POST — officers only; bulk-upserts a list of {field_key, note, resolved} objects.
    """
    permission_classes = [IsOfficerOrApplicant]
    serializer_class   = ProfileFieldNoteSerializer

    def _get_profile(self, pk, request):
        if request.user.role_code == 'quan_chung':
            return Profile.objects.get(pk=pk, user=request.user, deleted_at__isnull=True)
        return Profile.objects.get(pk=pk, deleted_at__isnull=True)

    def get(self, request, pk):
        try:
            profile = self._get_profile(pk, request)
        except Profile.DoesNotExist:
            return Response({'success': False, 'error': 'Hồ sơ không tồn tại.'}, status=404)
        notes = ProfileFieldNote.objects.filter(profile=profile).exclude(note='')
        return Response({'success': True, 'data': ProfileFieldNoteSerializer(notes, many=True).data})

    @transaction.atomic
    def post(self, request, pk):
        if request.user.role_code not in ('can_bo_bxd', 'admin'):
            return Response({'success': False, 'error': 'Chỉ cán bộ mới có thể thêm nhận xét.'}, status=403)
        if not _has_officer_perm(request.user, 'can_review_profiles'):
            return Response({'success': False, 'error': 'Bạn chưa được cấp quyền xem & trả lại hồ sơ.'}, status=403)
        try:
            profile = Profile.objects.get(pk=pk, deleted_at__isnull=True)
        except Profile.DoesNotExist:
            return Response({'success': False, 'error': 'Hồ sơ không tồn tại.'}, status=404)

        notes_data = request.data if isinstance(request.data, list) else request.data.get('notes', [])
        saved = []
        deleted_keys = []
        for item in notes_data:
            field_key  = str(item.get('field_key', '')).strip()
            note_text  = str(item.get('note', '')).strip()
            resolved   = bool(item.get('resolved', False))
            if not field_key:
                continue
            if not note_text:
                # Empty note = admin cleared it → delete the record
                ProfileFieldNote.objects.filter(profile=profile, field_key=field_key).delete()
                deleted_keys.append(field_key)
            else:
                obj, _ = ProfileFieldNote.objects.update_or_create(
                    profile=profile,
                    field_key=field_key,
                    defaults={'note': note_text, 'reviewer': request.user, 'resolved': resolved},
                )
                saved.append(ProfileFieldNoteSerializer(obj).data)

        log_activity(request.user, 'field_notes_save', target_model='Profile', target_id=profile.id,
                     description=f'Lưu {len(saved)} nhận xét, xóa {len(deleted_keys)} nhận xét cho hồ sơ {profile.full_name}')
        return Response({'success': True, 'data': saved, 'deleted': deleted_keys})
