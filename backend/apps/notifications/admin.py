from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Notification, NotificationTemplate, NotificationBatch


@admin.register(NotificationTemplate)
class NotificationTemplateAdmin(ModelAdmin):
    list_display  = ['id', 'code', 'name', 'channel', 'is_active', 'updated_at']
    list_filter   = ['channel', 'is_active']
    search_fields = ['code', 'name']


@admin.register(Notification)
class NotificationAdmin(ModelAdmin):
    list_display  = ['id', 'recipient', 'type', 'channel', 'is_read', 'sent_status', 'created_at']
    list_filter   = ['type', 'channel', 'is_read', 'sent_status']
    search_fields = ['recipient__full_name', 'body']
    readonly_fields = ['created_at', 'sent_at', 'read_at']
    raw_id_fields   = ['recipient', 'sender', 'profile', 'template', 'batch']


@admin.register(NotificationBatch)
class NotificationBatchAdmin(ModelAdmin):
    list_display  = ['id', 'type', 'channel', 'status', 'total_count', 'sent_count', 'created_at']
    list_filter   = ['status', 'channel']
    readonly_fields = ['created_at', 'completed_at', 'total_count', 'sent_count', 'failed_count']
