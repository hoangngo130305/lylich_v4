from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import ProfileEditHistory, ProfileCorrectionRequest, ProfileCorrectionItem, WordExportLog


@admin.register(ProfileEditHistory)
class ProfileEditHistoryAdmin(ModelAdmin):
    list_display  = ['id', 'profile', 'edited_by', 'section', 'field_name', 'created_at']
    list_filter   = ['section']
    search_fields = ['profile__full_name', 'field_name']
    readonly_fields = [f.name for f in ProfileEditHistory._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class CorrectionItemInline(TabularInline):
    model  = ProfileCorrectionItem
    extra  = 0
    fields = ['section', 'field_name', 'description', 'status', 'corrected_at', 'corrected_note']


@admin.register(ProfileCorrectionRequest)
class ProfileCorrectionRequestAdmin(ModelAdmin):
    list_display  = ['id', 'profile', 'created_by', 'status', 'created_at']
    list_filter   = ['status']
    search_fields = ['profile__full_name']
    readonly_fields = ['created_at', 'updated_at', 'resolved_at']
    raw_id_fields   = ['profile', 'created_by', 'resolved_by']
    inlines         = [CorrectionItemInline]


@admin.register(WordExportLog)
class WordExportLogAdmin(ModelAdmin):
    list_display  = ['id', 'profile', 'exported_by', 'template_name', 'file_name', 'file_size', 'created_at']
    list_filter   = ['template_name']
    search_fields = ['profile__full_name', 'file_name']
    readonly_fields = [f.name for f in WordExportLog._meta.fields]
    raw_id_fields   = ['profile', 'exported_by', 'file']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
