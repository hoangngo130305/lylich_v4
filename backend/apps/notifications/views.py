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
from apps.accounts.permissions import IsOfficer, IsOfficerOrApplicant, CanSendNotifications
from apps.auditlogs.utils import log_activity


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsOfficerOrApplicant]

    def get_queryset(self):
        # scope=sent — officers viewing "Lịch sử gửi gần đây" (notifications sent
        # to quần chúng by any officer), instead of the default "my inbox" view.
        scope = self.request.query_params.get('scope')
        if scope == 'sent' and getattr(self.request.user, 'role_code', None) in ('admin', 'can_bo_bxd'):
            qs = Notification.objects.filter(sender__isnull=False)
        else:
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
@permission_classes([CanSendNotifications])
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
    log_activity(request.user, 'notify_send', target_model='Notification', target_id=n.id)
    return Response({'success': True, 'data': NotificationSerializer(n).data})


def _bulk_group_querysets():
    """Returns the (Profile queryset, extra User queryset) definitions for each
    bulk-reminder audience. Shared by bulk_send() and bulk_group_counts()."""
    from datetime import timedelta
    from apps.profiles.models import Profile
    now = timezone.now()
    return {
        'late_submit_7d': Profile.objects.filter(
            status=Profile.Status.DRAFT, deleted_at__isnull=True,
            created_at__lte=now - timedelta(days=7),
        ).select_related('user'),
        'returned_stale_3d': Profile.objects.filter(
            status=Profile.Status.RETURNED, deleted_at__isnull=True,
            updated_at__lte=now - timedelta(days=3),
        ).select_related('user'),
        'all_draft':     Profile.objects.filter(status=Profile.Status.DRAFT, deleted_at__isnull=True).select_related('user'),
        'all_returned':  Profile.objects.filter(status=Profile.Status.RETURNED, deleted_at__isnull=True).select_related('user'),
        'all_submitted': Profile.objects.filter(status=Profile.Status.SUBMITTED, deleted_at__isnull=True).select_related('user'),
    }


def _new_no_login_users():
    from apps.accounts.models import User
    return User.objects.filter(role__code='quan_chung', deleted_at__isnull=True, last_login_at__isnull=True)


def _safe_profile(user):
    try:
        return user.profile
    except Exception:
        return None


@api_view(['GET'])
@permission_classes([CanSendNotifications])
def bulk_group_counts(request):
    """Live counts for the 3 quick-reminder audience checkboxes on Trung tâm thông báo."""
    groups = _bulk_group_querysets()
    return Response({
        'success': True,
        'data': {
            'late_submit_7d':    groups['late_submit_7d'].count(),
            'returned_stale_3d': groups['returned_stale_3d'].count(),
            'new_no_login':      _new_no_login_users().count(),
        }
    })


@api_view(['POST'])
@permission_classes([CanSendNotifications])
def bulk_send(request):
    serializer = BulkSendSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    d = serializer.validated_data
    group = d['group']

    if group == 'new_no_login':
        recipients = [(u, _safe_profile(u)) for u in _new_no_login_users()]
    else:
        groups = _bulk_group_querysets()
        if group in groups:
            profiles = groups[group]
        else:
            from apps.profiles.models import Profile
            profiles = Profile.objects.filter(deleted_at__isnull=True).select_related('user')
        recipients = [(p.user, p) for p in profiles if p.user_id]

    batch = NotificationBatch.objects.create(
        created_by=request.user,
        channel=d['channel'],
        type='bulk_' + group,
        custom_body=d['body'],
        template_id=d.get('template_id'),
        total_count=len(recipients),
        status=NotificationBatch.Status.SENDING,
    )

    sent = 0
    for user, profile in recipients:
        try:
            Notification.objects.create(
                batch=batch,
                sender=request.user,
                recipient=user,
                profile=profile,
                channel=d['channel'],
                type=Notification.Type.BULK_REMINDER,
                body=d['body'].replace('{{full_name}}', user.full_name),
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

    log_activity(request.user, 'bulk_notify', description=f'Gửi {sent} thông báo nhóm {group}')
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
@permission_classes([IsOfficerOrApplicant])
def notification_stats(request):
    from django.db.models import Q
    user = request.user
    # Applicants only see their own unread count
    if getattr(user, 'role_code', None) not in ('admin', 'can_bo_bxd'):
        unread_count = Notification.objects.filter(recipient=user, is_read=False).count()
        return Response({
            'success': True,
            'data': {
                'unread_count': unread_count,
            }
        })
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
