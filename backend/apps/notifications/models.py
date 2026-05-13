from django.db import models


class NotificationTemplate(models.Model):
    class Channel(models.TextChoices):
        ZALO_OA = 'zalo_oa', 'Zalo OA'
        SMS     = 'sms',     'SMS'
        EMAIL   = 'email',   'Email'
        IN_APP  = 'in_app',  'Trong ứng dụng'

    code       = models.CharField(max_length=80, unique=True)
    name       = models.CharField(max_length=255)
    channel    = models.CharField(max_length=20, choices=Channel.choices)
    subject    = models.CharField(max_length=500, null=True, blank=True)
    body       = models.TextField(help_text='Hỗ trợ {{variable}} placeholders')
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notification_templates'
        verbose_name = 'Mẫu thông báo'
        verbose_name_plural = 'Mẫu thông báo'

    def __str__(self):
        return f'{self.name} ({self.channel})'


class NotificationBatch(models.Model):
    class Status(models.TextChoices):
        DRAFT     = 'draft',     'Bản nháp'
        SENDING   = 'sending',   'Đang gửi'
        COMPLETED = 'completed', 'Hoàn tất'
        FAILED    = 'failed',    'Thất bại'

    created_by        = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='notification_batches')
    channel           = models.CharField(max_length=20, choices=NotificationTemplate.Channel.choices)
    type              = models.CharField(max_length=80)
    recipient_filter  = models.JSONField(null=True, blank=True)
    template          = models.ForeignKey(NotificationTemplate, null=True, blank=True,
                                          on_delete=models.SET_NULL, related_name='batches')
    custom_body       = models.TextField(null=True, blank=True)
    total_count       = models.PositiveIntegerField(default=0)
    sent_count        = models.PositiveIntegerField(default=0)
    failed_count      = models.PositiveIntegerField(default=0)
    status            = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    created_at        = models.DateTimeField(auto_now_add=True)
    completed_at      = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'notification_batches'
        verbose_name = 'Đợt gửi thông báo'
        verbose_name_plural = 'Đợt gửi thông báo'

    def __str__(self):
        return f'Batch {self.id} – {self.status}'


class Notification(models.Model):
    class Type(models.TextChoices):
        ACCOUNT_CREATED       = 'account_created',       'Tạo tài khoản'
        PROFILE_SUBMITTED     = 'profile_submitted',     'Nộp hồ sơ'
        PROFILE_APPROVED      = 'profile_approved',      'Phê duyệt hồ sơ'
        PROFILE_RETURNED      = 'profile_returned',      'Trả lại hồ sơ'
        PROFILE_REJECTED      = 'profile_rejected',      'Từ chối hồ sơ'
        PROFILE_COMPLETED     = 'profile_completed',     'Hoàn thiện hồ sơ'
        VERIFICATION_SENT     = 'verification_sent',     'Gửi xác minh'
        VERIFICATION_REMINDER = 'verification_reminder', 'Nhắc xác minh'
        VERIFICATION_RECEIVED = 'verification_received', 'Nhận kết quả xác minh'
        AI_ISSUE_DETECTED     = 'ai_issue_detected',     'AI phát hiện vấn đề'
        CORRECTION_REQUEST    = 'correction_request',    'Yêu cầu bổ sung'
        CORRECTION_RESOLVED   = 'correction_resolved',   'Đã bổ sung'
        BULK_REMINDER         = 'bulk_reminder',         'Nhắc hàng loạt'
        SYSTEM_ALERT          = 'system_alert',          'Cảnh báo hệ thống'
        CUSTOM                = 'custom',                'Tùy chỉnh'

    class SentStatus(models.TextChoices):
        PENDING   = 'pending',   'Chờ gửi'
        SENDING   = 'sending',   'Đang gửi'
        SENT      = 'sent',      'Đã gửi'
        DELIVERED = 'delivered', 'Đã nhận'
        FAILED    = 'failed',    'Thất bại'
        BOUNCED   = 'bounced',   'Bị trả về'

    template     = models.ForeignKey(NotificationTemplate, null=True, blank=True,
                                      on_delete=models.SET_NULL, related_name='notifications')
    batch        = models.ForeignKey(NotificationBatch, null=True, blank=True,
                                      on_delete=models.SET_NULL, related_name='notifications')
    sender       = models.ForeignKey('accounts.User', null=True, blank=True,
                                      on_delete=models.SET_NULL, related_name='sent_notifications')
    recipient    = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='notifications')
    profile      = models.ForeignKey('profiles.Profile', null=True, blank=True,
                                      on_delete=models.SET_NULL, related_name='notifications')
    channel      = models.CharField(max_length=20, choices=NotificationTemplate.Channel.choices)
    type         = models.CharField(max_length=40, choices=Type.choices)
    subject      = models.CharField(max_length=500, null=True, blank=True)
    body         = models.TextField()
    is_read      = models.BooleanField(default=False)
    read_at      = models.DateTimeField(null=True, blank=True)
    sent_status  = models.CharField(max_length=20, choices=SentStatus.choices, default=SentStatus.PENDING)
    sent_at      = models.DateTimeField(null=True, blank=True)
    delivery_ref = models.CharField(max_length=255, null=True, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notifications'
        verbose_name = 'Thông báo'
        verbose_name_plural = 'Thông báo'
        indexes = [
            models.Index(fields=['recipient', 'is_read']),
            models.Index(fields=['type']),
            models.Index(fields=['created_at']),
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.type} → {self.recipient}'

    def mark_read(self):
        from django.utils import timezone
        if not self.is_read:
            self.is_read = True
            self.read_at = timezone.now()
            self.save(update_fields=['is_read', 'read_at'])
