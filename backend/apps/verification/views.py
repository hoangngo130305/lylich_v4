from django.utils import timezone
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import VerificationRequest, VerificationReminderLog
from .serializers import VerificationRequestSerializer
from apps.accounts.permissions import IsOfficer
from apps.auditlogs.utils import log_activity


class VerificationListCreateView(generics.ListCreateAPIView):
    serializer_class = VerificationRequestSerializer
    permission_classes = [IsOfficer]
    filterset_fields  = ['status', 'urgency', 'profile']
    search_fields     = ['agency_name', 'profile__full_name']
    ordering_fields   = ['deadline', 'urgency', 'created_at']

    def get_queryset(self):
        return VerificationRequest.objects.select_related(
            'profile', 'created_by'
        ).order_by('-created_at')

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        log_activity(self.request.user, 'verify_send', target_model='VerificationRequest', target_id=obj.id)


class VerificationDetailView(generics.RetrieveUpdateAPIView):
    serializer_class  = VerificationRequestSerializer
    permission_classes = [IsOfficer]
    queryset = VerificationRequest.objects.all()

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


@api_view(['POST'])
@permission_classes([IsOfficer])
def send_reminder(request, pk):
    try:
        vr = VerificationRequest.objects.get(pk=pk)
    except VerificationRequest.DoesNotExist:
        return Response({'success': False, 'error': 'Không tìm thấy.'}, status=404)

    VerificationReminderLog.objects.create(
        verification=vr,
        sent_by=request.user,
        channel=request.data.get('channel', 'email'),
        note=request.data.get('note', ''),
    )
    vr.reminder_count += 1
    vr.last_reminded_at = timezone.now()
    vr.save(update_fields=['reminder_count', 'last_reminded_at'])

    log_activity(request.user, 'verify_remind', target_model='VerificationRequest', target_id=vr.id)
    return Response({'success': True, 'message': 'Đã ghi nhận lần nhắc.'})


@api_view(['POST'])
@permission_classes([IsOfficer])
def mark_received(request, pk):
    try:
        vr = VerificationRequest.objects.get(pk=pk)
    except VerificationRequest.DoesNotExist:
        return Response({'success': False, 'error': 'Không tìm thấy.'}, status=404)

    vr.status = VerificationRequest.Status.RECEIVED
    vr.received_at = timezone.now()
    vr.result_summary = request.data.get('result_summary', '')
    vr.updated_by = request.user
    vr.save(update_fields=['status', 'received_at', 'result_summary', 'updated_by'])

    log_activity(request.user, 'verify_receive', target_model='VerificationRequest', target_id=vr.id)
    return Response({'success': True, 'data': VerificationRequestSerializer(vr).data})


@api_view(['GET'])
@permission_classes([IsOfficer])
def verification_stats(request):
    from django.db.models import Count
    qs = VerificationRequest.objects.values('status').annotate(count=Count('id'))
    stats = {item['status']: item['count'] for item in qs}
    overdue = VerificationRequest.objects.filter(status='overdue').count()
    return Response({
        'success': True,
        'data': {
            'total':    VerificationRequest.objects.count(),
            'pending':  stats.get('pending', 0),
            'received': stats.get('received', 0),
            'overdue':  overdue,
            **stats,
        }
    })
