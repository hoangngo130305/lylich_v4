import os
from django.db import models
from django.conf import settings


def upload_path(instance, filename):
    category = instance.category
    ext = os.path.splitext(filename)[1].lower()
    import uuid
    name = f'{uuid.uuid4().hex}{ext}'
    return f'uploads/{category}/{name}'


class UploadedFile(models.Model):
    class Category(models.TextChoices):
        PROFILE_PHOTO          = 'profile_photo',          'Ảnh hồ sơ'
        CCCD_FRONT             = 'cccd_front',             'CCCD mặt trước'
        CCCD_BACK              = 'cccd_back',              'CCCD mặt sau'
        CERTIFICATE            = 'certificate',            'Bằng cấp / Chứng chỉ'
        VERIFICATION_ATTACHMENT= 'verification_attachment','Tài liệu xác minh'
        REPORT_EXPORT          = 'report_export',          'Xuất báo cáo'
        WORD_EXPORT            = 'word_export',            'Xuất Word/DOCX'
        OTHER                  = 'other',                  'Khác'

    uploader      = models.ForeignKey(
        'accounts.User', on_delete=models.PROTECT, related_name='uploaded_files'
    )
    profile       = models.ForeignKey(
        'profiles.Profile', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='uploaded_files'
    )
    category      = models.CharField(max_length=40, choices=Category.choices, default=Category.OTHER)
    original_name = models.CharField(max_length=500)
    stored_path   = models.CharField(max_length=1000)
    mime_type     = models.CharField(max_length=127, null=True, blank=True)
    file_size     = models.PositiveIntegerField(null=True, blank=True, help_text='Bytes')
    created_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'uploaded_files'
        verbose_name = 'File đã tải lên'
        verbose_name_plural = 'File đã tải lên'
        indexes = [
            models.Index(fields=['uploader']),
            models.Index(fields=['profile']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return f'{self.original_name} ({self.category})'

    @property
    def url(self):
        return f'{settings.MEDIA_URL}{self.stored_path}'
