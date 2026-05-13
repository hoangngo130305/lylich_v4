from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import FamilyMember


@admin.register(FamilyMember)
class FamilyMemberAdmin(ModelAdmin):
    list_display  = ['id', 'profile', 'relationship', 'full_name', 'birth_year', 'is_party_member']
    list_filter   = ['relationship', 'is_party_member', 'is_deceased']
    search_fields = ['full_name', 'profile__full_name']
    raw_id_fields = ['profile', 'updated_by']
    readonly_fields = ['created_at', 'updated_at', 'deleted_at']
