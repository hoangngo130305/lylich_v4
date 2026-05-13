from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import VerificationRequest, VerificationReminderLog


class ReminderInline(TabularInline):
    model = VerificationReminderLog
    extra = 0
    readonly_fields = ['sent_by', 'channel', 'note', 'created_at']
    can_delete = False


@admin.register(VerificationRequest)
class VerificationRequestAdmin(ModelAdmin):
    list_display  = ['id', 'profile', 'agency_name', 'urgency', 'status', 'deadline', 'reminder_count']
    list_filter   = ['status', 'urgency']
    search_fields = ['agency_name', 'profile__full_name']
    readonly_fields = ['created_at', 'updated_at', 'received_at', 'completed_at', 'reminder_count']
    raw_id_fields   = ['profile', 'created_by', 'updated_by', 'result_file']
    inlines = [ReminderInline]
