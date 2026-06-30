import logging
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import FamilyMember
from .serializers import FamilyMemberSerializer
from apps.accounts.permissions import IsOwnerOrOfficer, IsOfficerOrApplicant

logger = logging.getLogger(__name__)


class FamilyMemberListCreateView(generics.ListCreateAPIView):
    serializer_class = FamilyMemberSerializer
    permission_classes = [IsOfficerOrApplicant]
    pagination_class = None

    def get_queryset(self):
        profile_id = self.kwargs['profile_id']
        base_qs = FamilyMember.objects.prefetch_related(
            'history_entries'
        )
        if self.request.user.role_code == 'quan_chung':
            return base_qs.filter(
                profile_id=profile_id,
                profile__user=self.request.user,
                deleted_at__isnull=True
            )
        return base_qs.filter(
            profile_id=profile_id, deleted_at__isnull=True
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            logger.error(
                "[FAM_400] profile_id=%s | data=%s | errors=%s",
                kwargs.get('profile_id'), dict(request.data), serializer.errors
            )
            raise ValidationError(serializer.errors)
        self.perform_create(serializer)
        from rest_framework import status
        from rest_framework.response import Response
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(profile_id=self.kwargs['profile_id'], updated_by=self.request.user)


class FamilyMemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FamilyMemberSerializer
    permission_classes = [IsOfficerOrApplicant]

    def get_queryset(self):
        if self.request.user.role_code == 'quan_chung':
            return FamilyMember.objects.filter(
                profile__user=self.request.user, deleted_at__isnull=True
            )
        return FamilyMember.objects.filter(deleted_at__isnull=True)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        from django.utils import timezone
        obj.deleted_at = timezone.now()
        obj.save(update_fields=['deleted_at'])
        return Response({'success': True, 'message': 'Đã xóa thành viên gia đình.'})
