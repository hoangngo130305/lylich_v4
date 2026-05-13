from django.db import models


class ProfileEditHistory(models.Model):
    profile     = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='edit_history')
    edited_by   = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='edits')
    section     = models.CharField(max_length=80)
    field_name  = models.CharField(max_length=120)
    old_value   = models.TextField(null=True, blank=True)
    new_value   = models.TextField(null=True, blank=True)
    edit_reason = models.CharField(max_length=500, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'profile_edit_history'
        verbose_name = 'Lịch sử chỉnh sửa'
        verbose_name_plural = 'Lịch sử chỉnh sửa'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['profile', '-created_at']),
            models.Index(fields=['section']),
        ]

    def __str__(self):
        return f'{self.profile} – {self.field_name}'


class ProfileCorrectionRequest(models.Model):
    class Status(models.TextChoices):
        OPEN        = 'open',        'Chờ bổ sung'
        IN_PROGRESS = 'in_progress', 'Đang bổ sung'
        RESOLVED    = 'resolved',    'Đã bổ sung'
        DISMISSED   = 'dismissed',   'Đã đóng'

    profile      = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='correction_requests')
    created_by   = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='created_corrections')
    status       = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    overall_note = models.TextField(null=True, blank=True)
    resolved_by  = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL,
                                      related_name='resolved_corrections', db_column='resolved_by')
    resolved_at  = models.DateTimeField(null=True, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profile_correction_requests'
        verbose_name = 'Yêu cầu bổ sung'
        verbose_name_plural = 'Yêu cầu bổ sung'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['profile', 'status']),
        ]

    def __str__(self):
        return f'Correction {self.id} – {self.profile} – {self.status}'


class ProfileCorrectionItem(models.Model):
    class ItemStatus(models.TextChoices):
        PENDING   = 'pending',   'Chờ bổ sung'
        CORRECTED = 'corrected', 'Đã bổ sung'
        WAIVED    = 'waived',    'Bỏ qua'

    request        = models.ForeignKey(ProfileCorrectionRequest, on_delete=models.CASCADE, related_name='items')
    section        = models.CharField(max_length=80)
    field_name     = models.CharField(max_length=120, null=True, blank=True)
    description    = models.TextField()
    status         = models.CharField(max_length=20, choices=ItemStatus.choices, default=ItemStatus.PENDING)
    corrected_at   = models.DateTimeField(null=True, blank=True)
    corrected_note = models.TextField(null=True, blank=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profile_correction_items'
        verbose_name = 'Mục yêu cầu bổ sung'
        verbose_name_plural = 'Mục yêu cầu bổ sung'

    def __str__(self):
        return f'{self.section}/{self.field_name} – {self.status}'


class WordExportLog(models.Model):
    profile       = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='word_exports')
    exported_by   = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='word_exports')
    template_name = models.CharField(max_length=120, null=True, blank=True)
    file          = models.ForeignKey('uploads.UploadedFile', null=True, blank=True,
                                       on_delete=models.SET_NULL, related_name='word_export_logs',
                                       db_column='file_id')
    file_name     = models.CharField(max_length=500, null=True, blank=True)
    file_size     = models.PositiveIntegerField(null=True, blank=True)
    sections_json = models.JSONField(null=True, blank=True)
    created_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'word_export_logs'
        verbose_name = 'Xuất Word'
        verbose_name_plural = 'Xuất Word'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.profile} – {self.file_name}'
