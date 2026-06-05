from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import EthnicGroup, Religion, EducationLevel, PoliticalLevel, AdministrativeUnit


@admin.register(EthnicGroup)
class EthnicGroupAdmin(ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Religion)
class ReligionAdmin(ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(EducationLevel)
class EducationLevelAdmin(ModelAdmin):
    list_display = ['id', 'code', 'name', 'sort']
    list_editable = ['sort']
    search_fields = ['name', 'code']

    def get_queryset(self, request):
        return super().get_queryset(request).exclude(name__iexact='Tiểu học')


@admin.register(PoliticalLevel)
class PoliticalLevelAdmin(ModelAdmin):
    list_display = ['id', 'code', 'name']
    search_fields = ['name', 'code']


@admin.register(AdministrativeUnit)
class AdministrativeUnitAdmin(ModelAdmin):
    list_display = ['id', 'type', 'code', 'name', 'parent']
    list_filter = ['type']
    search_fields = ['name', 'code']
    raw_id_fields = ['parent']
