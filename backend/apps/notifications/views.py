from django.utils import timezone
from django.db.models import Count
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Notification, NotificationTemplate, NotificationBatch
from .serializers import (
    NotificationSerializer, NotificationTemplateSerializer,
    SendNotificationSerializer, BulkSendSerializer, NotificationBatchSerializer,
)
from apps.accounts.permissions import IsOfficer, IsOfficerOrApplicant
from apps.auditlogs.utils import log_activity


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsOfficerOrApplicant]

    def get_queryset(self):
        qs = Notification.objects.filter(recipient=self.request.user)
        unread = self.request.query_params.get('unread')
        if unread == 'true':
            qs = qs.filter(is_read=False)
        return qs.order_by('-created_at')


@api_view(['POST'])
@permission_classes([IsOfficerOrApplicant])
def mark_read(request, pk):
    try:
        n = Notification.objects.get(pk=pk, recipient=request.user)
        n.mark_read()
        return Response({'success': True})
    except Notification.DoesNotExist:
        return Response({'success': False}, status=404)


@api_view(['POST'])
@permission_classes([IsOfficerOrApplicant])
def mark_all_read(request):
    Notification.objects.filter(recipient=request.user, is_read=False).update(
        is_read=True, read_at=timezone.now()
    )
    return Response({'success': True, 'message': 'Đã đánh dấu tất cả là đã đọc.'})


@api_view(['POST'])
@permission_classes([IsOfficer])
def send_notification(request):
    serializer = SendNotificationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    d = serializer.validated_data
    n = Notification.objects.create(
        sender=request.user,
        recipient_id=d['recipient_id'],
        profile_id=d.get('profile_id'),
        channel=d['channel'],
        type=d['type'],
        subject=d.get('subject', ''),
        body=d['body'],
        sent_status=Notification.SentStatus.SENT,
        sent_at=timezone.now(),
        template_id=d.get('template_id'),
    )
    log_activity(request.user, 'notify_send', target_type='Notification', target_id=n.id)
    return Response({'success': True, 'data': NotificationSerializer(n).data})


@api_view(['POST'])
@permission_classes([IsOfficer])
def bulk_send(request):
    serializer = BulkSendSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    d = serializer.validated_data

    from apps.profiles.models import Profile
    from apps.accounts.models import User

    group_map = {
        'all_draft':     Profile.Status.DRAFT,
        'all_returned':  Profile.Status.RETURNED,
        'all_submitted': Profile.Status.SUBMITTED,
    }
    target_status = group_map.get(d['group'])
    if target_status:
        profiles = Profile.objects.filter(status=target_status, deleted_at__isnull=True).select_related('user')
    else:
        profiles = Profile.objects.filter(deleted_at__isnull=True).select_related('user')

    batch = NotificationBatch.objects.create(
        created_by=request.user,
        channel=d['channel'],
        type='bulk_' + d['group'],
        custom_body=d['body'],
        template_id=d.get('template_id'),
        total_count=profiles.count(),
        status=NotificationBatch.Status.SENDING,
    )

    sent = 0
    for p in profiles:
        try:
            Notification.objects.create(
                batch=batch,
                sender=request.user,
                recipient=p.user,
                profile=p,
                channel=d['channel'],
                type=Notification.Type.BULK_REMINDER,
                body=d['body'].replace('{{full_name}}', p.full_name),
                sent_status=Notification.SentStatus.SENT,
                sent_at=timezone.now(),
            )
            sent += 1
        except Exception:
            batch.failed_count += 1

    batch.sent_count = sent
    batch.status = NotificationBatch.Status.COMPLETED
    batch.completed_at = timezone.now()
    batch.save(update_fields=['sent_count', 'failed_count', 'status', 'completed_at'])

    log_activity(request.user, 'bulk_notify', description=f'Gửi {sent} thông báo nhóm {d["group"]}')
    return Response({'success': True, 'data': NotificationBatchSerializer(batch).data})


class NotificationTemplateListView(generics.ListCreateAPIView):
    serializer_class = NotificationTemplateSerializer
    permission_classes = [IsOfficer]
    queryset = NotificationTemplate.objects.filter(is_active=True)


class NotificationTemplateDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotificationTemplateSerializer
    permission_classes = [IsOfficer]
    queryset = NotificationTemplate.objects.all()


@api_view(['GET'])
@permission_classes([IsOfficer])
def notification_stats(request):
    from django.db.models import Q
    today = timezone.now().date()
    return Response({
        'success': True,
        'data': {
            'total_sent_today': Notification.objects.filter(
                sent_at__date=today
            ).count(),
            'unread_count': Notification.objects.filter(is_read=False).count(),
            'by_channel': list(
                Notification.objects.values('channel').annotate(count=Count('id'))
            ),
            'recent_batches': NotificationBatchSerializer(
                NotificationBatch.objects.order_by('-created_at')[:5], many=True
            ).data,
        }
    })
