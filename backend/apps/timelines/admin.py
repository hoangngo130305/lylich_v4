from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import HistoryEntry, WorkHistory, EducationHistory, Award, OverseasTravel, OverseasRelative


@admin.register(HistoryEntry)
class HistoryEntryAdmin(ModelAdmin):
    list_display  = ['id', 'profile', 'entry_type', 'from_year', 'to_year', 'description']
    list_filter   = ['entry_type']
    search_fields = ['profile__full_name', 'description']
    raw_id_fields = ['profile', 'family_member']


@admin.register(WorkHistory)
class WorkHistoryAdmin(ModelAdmin):
    list_display  = ['id', 'profile', 'employer', 'job_title', 'from_year', 'to_year']
    search_fields = ['profile__full_name', 'employer']
    raw_id_fields = ['profile']


@admin.register(Award)
class AwardAdmin(ModelAdmin):
    list_display  = ['id', 'profile', 'type', 'level', 'issued_year', 'content']
    list_filter   = ['type']
    search_fields = ['profile__full_name', 'content']
    raw_id_fields = ['profile']
