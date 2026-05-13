from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import UploadedFile


@admin.register(UploadedFile)
class UploadedFileAdmin(ModelAdmin):
    list_display  = ['id', 'original_name', 'category', 'uploader', 'file_size', 'created_at']
    list_filter   = ['category']
    search_fields = ['original_name', 'uploader__full_name']
    readonly_fields = ['created_at', 'uploader', 'stored_path', 'mime_type', 'file_size']
    raw_id_fields   = ['uploader', 'profile']
