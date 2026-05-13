from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ActivityLog, AIScanResult


@admin.register(ActivityLog)
class ActivityLogAdmin(ModelAdmin):
    list_display  = ['id', 'user', 'action', 'target_model', 'target_id', 'ip_address', 'created_at']
    list_filter   = ['action', 'target_model']
    search_fields = ['user__full_name', 'description', 'ip_address']
    readonly_fields = [f.name for f in ActivityLog._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(AIScanResult)
class AIScanResultAdmin(ModelAdmin):
    list_display  = ['id', 'profile', 'section', 'issue_type', 'severity', 'status', 'created_at']
    list_filter   = ['severity', 'status', 'section']
    search_fields = ['profile__full_name', 'description', 'issue_type']
    readonly_fields = ['created_at', 'resolved_at']
    raw_id_fields   = ['profile', 'scanned_by', 'resolved_by']
