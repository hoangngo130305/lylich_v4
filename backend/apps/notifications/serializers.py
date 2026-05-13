from rest_framework import serializers
from .models import Notification, NotificationTemplate, NotificationBatch


class NotificationTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationTemplate
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    type_display    = serializers.CharField(source='get_type_display', read_only=True)
    channel_display = serializers.CharField(source='get_channel_display', read_only=True)
    sender_name     = serializers.CharField(source='sender.full_name', read_only=True, default=None)
    profile_name    = serializers.CharField(source='profile.full_name', read_only=True, default=None)

    class Meta:
        model = Notification
        fields = [
            'id', 'type', 'type_display', 'channel', 'channel_display',
            'subject', 'body', 'is_read', 'read_at', 'sent_status', 'sent_at',
            'sender_name', 'profile_id', 'profile_name',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']


class SendNotificationSerializer(serializers.Serializer):
    recipient_id = serializers.IntegerField()
    profile_id   = serializers.IntegerField(required=False, allow_null=True)
    channel      = serializers.ChoiceField(choices=NotificationTemplate.Channel.choices)
    type         = serializers.ChoiceField(choices=Notification.Type.choices)
    subject      = serializers.CharField(required=False, allow_blank=True)
    body         = serializers.CharField()
    template_id  = serializers.IntegerField(required=False, allow_null=True)


class BulkSendSerializer(serializers.Serializer):
    group       = serializers.ChoiceField(choices=[
        ('all_draft', 'Tất cả đang kê khai'),
        ('all_returned', 'Tất cả hồ sơ trả lại'),
        ('all_submitted', 'Tất cả đã nộp'),
        ('custom', 'Tùy chỉnh'),
    ])
    channel     = serializers.ChoiceField(choices=NotificationTemplate.Channel.choices)
    body        = serializers.CharField()
    template_id = serializers.IntegerField(required=False, allow_null=True)


class NotificationBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationBatch
        fields = '__all__'
        read_only_fields = ['id', 'total_count', 'sent_count', 'failed_count', 'created_at', 'completed_at']
