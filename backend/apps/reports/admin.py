from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import StatsMonthly, ReportExport


@admin.register(StatsMonthly)
class StatsMonthlyAdmin(ModelAdmin):
    list_display  = ['year', 'month', 'count_total', 'count_approved', 'count_submitted', 'count_under_review', 'computed_at']
    list_filter   = ['year']
    ordering      = ['-year', '-month']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(ReportExport)
class ReportExportAdmin(ModelAdmin):
    list_display  = ['id', 'created_by', 'report_type', 'format', 'file_name', 'file_size', 'created_at']
    list_filter   = ['report_type', 'format']
    readonly_fields = [f.name for f in ReportExport._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
