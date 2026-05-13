from rest_framework import serializers
from .models import ActivityLog, AIScanResult


class ActivityLogSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.full_name', read_only=True, default=None)

    class Meta:
        model = ActivityLog
        fields = ['id', 'user', 'user_name', 'action', 'target_model', 'target_id',
                  'description', 'ip_address', 'extra', 'created_at']
        read_only_fields = fields


class AIScanResultSerializer(serializers.ModelSerializer):
    scanned_by_name  = serializers.CharField(source='scanned_by.full_name',  read_only=True, default=None)
    resolved_by_name = serializers.CharField(source='resolved_by.full_name', read_only=True, default=None)

    class Meta:
        model = AIScanResult
        fields = ['id', 'profile', 'scanned_by', 'scanned_by_name', 'section', 'field_name',
                  'issue_type', 'description', 'severity', 'status',
                  'resolved_by', 'resolved_by_name', 'resolved_at', 'created_at']
        read_only_fields = ['id', 'created_at', 'scanned_by_name', 'resolved_by_name']
