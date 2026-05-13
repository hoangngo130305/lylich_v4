from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import FamilyMember
from .serializers import FamilyMemberSerializer
from apps.accounts.permissions import IsOwnerOrOfficer, IsOfficerOrApplicant


class FamilyMemberListCreateView(generics.ListCreateAPIView):
    serializer_class = FamilyMemberSerializer
    permission_classes = [IsOfficerOrApplicant]

    def get_queryset(self):
        profile_id = self.kwargs['profile_id']
        if self.request.user.role_code == 'quan_chung':
            return FamilyMember.objects.filter(
                profile_id=profile_id,
                profile__user=self.request.user,
                deleted_at__isnull=True
            ).order_by('sort_order')
        return FamilyMember.objects.filter(
            profile_id=profile_id, deleted_at__isnull=True
        ).order_by('sort_order')

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
