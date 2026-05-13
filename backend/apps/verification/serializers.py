from rest_framework import serializers
from .models import VerificationRequest, VerificationReminderLog


class VerificationReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationReminderLog
        fields = ['id', 'channel', 'note', 'sent_by_id', 'created_at']
        read_only_fields = ['id', 'sent_by_id', 'created_at']


class VerificationRequestSerializer(serializers.ModelSerializer):
    status_display  = serializers.CharField(source='get_status_display', read_only=True)
    urgency_display = serializers.CharField(source='get_urgency_display', read_only=True)
    profile_name    = serializers.CharField(source='profile.full_name', read_only=True)
    reminders       = VerificationReminderSerializer(many=True, read_only=True)

    class Meta:
        model = VerificationRequest
        fields = '__all__'
        read_only_fields = ['id', 'created_by', 'reminder_count', 'last_reminded_at',
                            'received_at', 'completed_at', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
