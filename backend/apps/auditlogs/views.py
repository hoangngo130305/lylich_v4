from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.accounts.permissions import IsAdmin, IsOfficer
from .models import ActivityLog, AIScanResult
from .serializers import ActivityLogSerializer, AIScanResultSerializer


class ActivityLogListView(generics.ListAPIView):
    serializer_class   = ActivityLogSerializer
    permission_classes = [IsAdmin]
    filter_backends    = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields   = ['action', 'target_model', 'user']
    search_fields      = ['description', 'user__full_name']
    ordering_fields    = ['created_at']
    ordering           = ['-created_at']

    def get_queryset(self):
        qs = ActivityLog.objects.select_related('user')
        user_id = self.request.query_params.get('user_id')
        if user_id:
            qs = qs.filter(user_id=user_id)
        return qs


class AIScanResultListView(generics.ListCreateAPIView):
    serializer_class   = AIScanResultSerializer
    permission_classes = [IsOfficer]
    filter_backends    = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields   = ['profile', 'severity', 'status', 'section']
    ordering_fields    = ['created_at', 'severity']
    ordering           = ['-created_at']

    def get_queryset(self):
        return AIScanResult.objects.select_related('profile', 'scanned_by', 'resolved_by')

    def perform_create(self, serializer):
        serializer.save(scanned_by=self.request.user)


class AIScanResultDetailView(generics.RetrieveUpdateAPIView):
    serializer_class   = AIScanResultSerializer
    permission_classes = [IsOfficer]
    queryset           = AIScanResult.objects.select_related('profile', 'scanned_by', 'resolved_by')

    def perform_update(self, serializer):
        from django.utils import timezone
        data = {}
        if serializer.validated_data.get('status') == AIScanResult.Status.RESOLVED:
            data = {'resolved_by': self.request.user, 'resolved_at': timezone.now()}
        serializer.save(**data)
