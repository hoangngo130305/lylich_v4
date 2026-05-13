import os
import mimetypes
from rest_framework import serializers
from django.conf import settings
from .models import UploadedFile


class UploadedFileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = UploadedFile
        fields = ['id', 'category', 'original_name', 'mime_type',
                  'file_size', 'url', 'created_at']
        read_only_fields = ['id', 'original_name', 'mime_type', 'file_size', 'url', 'created_at']

    def get_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f'{settings.MEDIA_URL}{obj.stored_path}')
        return obj.url


class FileUploadSerializer(serializers.Serializer):
    file     = serializers.FileField()
    category = serializers.ChoiceField(choices=UploadedFile.Category.choices,
                                       default=UploadedFile.Category.OTHER)
    profile_id = serializers.IntegerField(required=False, allow_null=True)

    def validate_file(self, value):
        max_size = getattr(settings, 'MAX_UPLOAD_SIZE', 10 * 1024 * 1024)
        if value.size > max_size:
            raise serializers.ValidationError(
                f'File quá lớn. Tối đa {max_size // (1024*1024)}MB.'
            )
        allowed_types = [
            'image/jpeg', 'image/png', 'image/gif', 'image/webp',
            'application/pdf',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'application/msword',
            'application/vnd.ms-excel',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        ]
        mime, _ = mimetypes.guess_type(value.name)
        if mime not in allowed_types:
            raise serializers.ValidationError(
                f'Định dạng file không được hỗ trợ: {mime}'
            )
        return value
