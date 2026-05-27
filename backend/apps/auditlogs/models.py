from django.db import models


class ActivityLog(models.Model):
    class Action(models.TextChoices):
        CREATE   = 'create',   'Tạo mới'
        UPDATE   = 'update',   'Cập nhật'
        DELETE   = 'delete',   'Xóa'
        VIEW     = 'view',     'Xem'
        EXPORT   = 'export',   'Xuất'
        LOGIN    = 'login',    'Đăng nhập'
        LOGOUT   = 'logout',   'Đăng xuất'
        APPROVE  = 'approve',  'Duyệt'
        REJECT   = 'reject',   'Từ chối'
        SUBMIT   = 'submit',   'Nộp'
        SEND     = 'send',     'Gửi'

    user         = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL,
                                      related_name='activity_logs')
    action       = models.CharField(max_length=50, choices=Action.choices)
    target_model = models.CharField(max_length=80, null=True, blank=True)
    target_id    = models.BigIntegerField(null=True, blank=True)
    description  = models.TextField(null=True, blank=True)
    ip_address   = models.GenericIPAddressField(null=True, blank=True)
    user_agent   = models.CharField(max_length=500, null=True, blank=True)
    extra        = models.JSONField(null=True, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activity_logs'
        verbose_name = 'Nhật ký hoạt động'
        verbose_name_plural = 'Nhật ký hoạt động'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['target_model', 'target_id']),
            models.Index(fields=['action']),
        ]

    def __str__(self):
        return f'{self.user} – {self.action} – {self.target_model}:{self.target_id}'


class AIScanResult(models.Model):
    class Severity(models.TextChoices):
        INFO    = 'info',    'Thông tin'
        WARNING = 'warning', 'Cảnh báo'
        ERROR   = 'error',   'Lỗi'

    class Status(models.TextChoices):
        OPEN     = 'open',     'Chưa xử lý'
        RESOLVED = 'resolved', 'Đã xử lý'
        IGNORED  = 'ignored',  'Bỏ qua'

    profile     = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='ai_scan_results')
    scanned_by  = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name='ai_scans')
    section     = models.CharField(max_length=80)
    field_name  = models.CharField(max_length=120, null=True, blank=True)
    issue_type  = models.CharField(max_length=80)
    description = models.TextField()
    severity    = models.CharField(max_length=10, choices=Severity.choices, default=Severity.WARNING)
    status      = models.CharField(max_length=10, choices=Status.choices, default=Status.OPEN)
    resolved_by = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name='resolved_ai_scans', db_column='resolved_by')
    resolved_at = models.DateTimeField(null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ai_scan_results'
        verbose_name = 'Kết quả quét AI'
        verbose_name_plural = 'Kết quả quét AI'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['profile', 'status']),
            models.Index(fields=['severity']),
        ]

    def __str__(self):
        return f'{self.profile} – {self.section} – {self.severity}'
