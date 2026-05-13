from django.db import models


class VerificationRequest(models.Model):
    class Urgency(models.TextChoices):
        NORMAL   = 'normal',   'Thường'
        URGENT   = 'urgent',   'Khẩn'
        CRITICAL = 'critical', 'Rất khẩn'

    class Status(models.TextChoices):
        DRAFT     = 'draft',     'Chưa gửi'
        PENDING   = 'pending',   'Chờ phản hồi'
        RECEIVED  = 'received',  'Đã nhận kết quả'
        COMPLETED = 'completed', 'Hoàn tất'
        OVERDUE   = 'overdue',   'Quá hạn'
        CANCELLED = 'cancelled', 'Đã hủy'

    profile        = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='verifications')
    created_by     = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='created_verifications')
    agency_name    = models.CharField(max_length=500)
    agency_contact = models.CharField(max_length=500, null=True, blank=True)
    content        = models.TextField()
    urgency        = models.CharField(max_length=20, choices=Urgency.choices, default=Urgency.NORMAL)
    sent_date      = models.DateField(null=True, blank=True)
    deadline       = models.DateField(null=True, blank=True)
    status         = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    result_summary = models.TextField(null=True, blank=True)
    result_file    = models.ForeignKey('uploads.UploadedFile', null=True, blank=True, on_delete=models.SET_NULL,
                                        related_name='verification_results', db_column='result_file_id')
    reminder_count   = models.PositiveSmallIntegerField(default=0)
    last_reminded_at = models.DateTimeField(null=True, blank=True)
    received_at      = models.DateTimeField(null=True, blank=True)
    completed_at     = models.DateTimeField(null=True, blank=True)
    notes            = models.TextField(null=True, blank=True)
    updated_by       = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL,
                                          related_name='updated_verifications', db_column='updated_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'verification_requests'
        verbose_name = 'Yêu cầu xác minh'
        verbose_name_plural = 'Yêu cầu xác minh'
        indexes = [
            models.Index(fields=['profile', 'status']),
            models.Index(fields=['deadline']),
            models.Index(fields=['urgency']),
        ]

    def __str__(self):
        return f'{self.agency_name} – {self.status}'


class VerificationReminderLog(models.Model):
    class Channel(models.TextChoices):
        EMAIL    = 'email',     'Email'
        SMS      = 'sms',       'SMS'
        PHONE    = 'phone',     'Điện thoại'
        IN_PERSON= 'in_person', 'Trực tiếp'
        OTHER    = 'other',     'Khác'

    verification = models.ForeignKey(VerificationRequest, on_delete=models.CASCADE, related_name='reminders')
    sent_by      = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL,
                                      related_name='sent_reminders', db_column='sent_by')
    channel      = models.CharField(max_length=20, choices=Channel.choices, default=Channel.EMAIL)
    note         = models.TextField(null=True, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'verification_reminder_log'
        verbose_name = 'Nhật ký nhắc xác minh'
        verbose_name_plural = 'Nhật ký nhắc xác minh'

    def __str__(self):
        return f'Reminder for {self.verification}'
