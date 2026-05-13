from django.db import models


class StatsMonthly(models.Model):
    year               = models.SmallIntegerField()
    month              = models.SmallIntegerField()
    unit_id            = models.IntegerField(null=True, blank=True)
    count_draft        = models.IntegerField(default=0)
    count_submitted    = models.IntegerField(default=0)
    count_under_review = models.IntegerField(default=0)
    count_approved     = models.IntegerField(default=0)
    count_rejected     = models.IntegerField(default=0)
    count_archived     = models.IntegerField(default=0)
    count_total        = models.IntegerField(default=0)
    computed_at        = models.DateTimeField(auto_now=True)

    class Meta:
        db_table    = 'stats_monthly'
        unique_together = [('year', 'month', 'unit_id')]
        verbose_name = 'Thống kê tháng'
        verbose_name_plural = 'Thống kê tháng'

    def __str__(self):
        return f'{self.year}/{self.month:02d}'


class ReportExport(models.Model):
    class ReportType(models.TextChoices):
        MONTHLY   = 'monthly',   'Báo cáo tháng'
        QUARTERLY = 'quarterly', 'Báo cáo quý'
        ANNUAL    = 'annual',    'Báo cáo năm'
        CUSTOM    = 'custom',    'Tùy chỉnh'

    class Format(models.TextChoices):
        EXCEL = 'excel', 'Excel'
        PDF   = 'pdf',   'PDF'
        WORD  = 'word',  'Word'

    created_by   = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='report_exports')
    report_type  = models.CharField(max_length=20, choices=ReportType.choices)
    format       = models.CharField(max_length=10, choices=Format.choices, default=Format.EXCEL)
    params       = models.JSONField(null=True, blank=True)
    file_name    = models.CharField(max_length=500, null=True, blank=True)
    file_size    = models.PositiveIntegerField(null=True, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'report_exports'
        verbose_name = 'Xuất báo cáo'
        verbose_name_plural = 'Xuất báo cáo'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.report_type} – {self.file_name}'
