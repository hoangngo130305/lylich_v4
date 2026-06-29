from django.db import models


class HistoryEntry(models.Model):
    class EntryType(models.TextChoices):
        SELF   = 'self',   'Bản thân'
        FAMILY = 'family', 'Thành viên gia đình'

    profile       = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='history_entries')
    entry_type    = models.CharField(max_length=10, choices=EntryType.choices, default=EntryType.SELF)
    family_member = models.ForeignKey('family.FamilyMember', null=True, blank=True,
                                       on_delete=models.CASCADE, related_name='history_entries',
                                       db_column='family_member_id')
    from_month  = models.PositiveSmallIntegerField(null=True, blank=True)
    from_year   = models.PositiveSmallIntegerField(null=True, blank=True)
    to_month    = models.PositiveSmallIntegerField(null=True, blank=True)
    to_year     = models.PositiveSmallIntegerField(null=True, blank=True)
    is_present  = models.BooleanField(default=False)
    is_deceased = models.BooleanField(default=False)
    description = models.TextField(blank=True, default="")
    location    = models.CharField(max_length=500, null=True, blank=True)
    sort_order  = models.PositiveSmallIntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profile_history_entries'
        verbose_name = 'Lịch sử bản thân'
        verbose_name_plural = 'Lịch sử bản thân'
        ordering = ['from_year', 'from_month', 'sort_order']
        indexes = [
            models.Index(fields=['profile', 'entry_type']),
            models.Index(fields=['from_year', 'to_year']),
        ]

    def __str__(self):
        return f'{self.profile} – {self.from_year}/{self.from_month}'


class WorkHistory(models.Model):
    profile     = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='work_history')
    period_text = models.CharField(max_length=255, null=True, blank=True)
    from_month  = models.PositiveSmallIntegerField(null=True, blank=True)
    from_year   = models.PositiveSmallIntegerField(null=True, blank=True)
    to_month    = models.PositiveSmallIntegerField(null=True, blank=True)
    to_year     = models.PositiveSmallIntegerField(null=True, blank=True)
    is_present  = models.BooleanField(default=False)
    employer    = models.CharField(max_length=500)
    job_title   = models.CharField(max_length=255, null=True, blank=True)
    location    = models.CharField(max_length=500, null=True, blank=True)
    notes       = models.TextField(null=True, blank=True)
    sort_order  = models.PositiveSmallIntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profile_work_history'
        verbose_name = 'Lịch sử công tác'
        verbose_name_plural = 'Lịch sử công tác'
        ordering = ['from_year', 'from_month']

    def __str__(self):
        return f'{self.employer} – {self.job_title}'


class EducationHistory(models.Model):
    profile     = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='education_history')
    period_text = models.CharField(max_length=255, null=True, blank=True)
    from_month  = models.PositiveSmallIntegerField(null=True, blank=True)
    from_year   = models.PositiveSmallIntegerField(null=True, blank=True)
    to_month    = models.PositiveSmallIntegerField(null=True, blank=True)
    to_year     = models.PositiveSmallIntegerField(null=True, blank=True)
    is_present  = models.BooleanField(default=False)
    school      = models.CharField(max_length=500)
    major       = models.CharField(max_length=255, null=True, blank=True)
    edu_level   = models.CharField(max_length=100, null=True, blank=True)
    location    = models.CharField(max_length=500, null=True, blank=True)
    certificate = models.CharField(max_length=255, null=True, blank=True)
    notes       = models.TextField(null=True, blank=True)
    sort_order  = models.PositiveSmallIntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profile_education_history'
        verbose_name = 'Lịch sử học vấn'
        verbose_name_plural = 'Lịch sử học vấn'
        ordering = ['from_year', 'from_month']

    def __str__(self):
        return f'{self.school} – {self.major}'


class OrgParticipation(models.Model):
    profile    = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='org_participations')
    org_name   = models.CharField(max_length=500)
    join_month  = models.PositiveSmallIntegerField(null=True, blank=True)
    join_year   = models.PositiveSmallIntegerField(null=True, blank=True)
    leave_month = models.PositiveSmallIntegerField(null=True, blank=True)
    leave_year  = models.PositiveSmallIntegerField(null=True, blank=True)
    is_present  = models.BooleanField(default=False)
    role_in_org = models.CharField(max_length=255, null=True, blank=True)
    notes       = models.TextField(null=True, blank=True)
    sort_order  = models.PositiveSmallIntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profile_org_participation'
        verbose_name = 'Tham gia tổ chức'
        verbose_name_plural = 'Tham gia tổ chức'

    def __str__(self):
        return self.org_name


class Award(models.Model):
    class AwardType(models.TextChoices):
        AWARD      = 'award',      'Khen thưởng'
        DISCIPLINE = 'discipline', 'Kỷ luật'

    profile     = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='awards')
    type        = models.CharField(max_length=20, choices=AwardType.choices)
    period_text = models.CharField(max_length=255, null=True, blank=True)
    level       = models.CharField(max_length=100, null=True, blank=True)
    issued_month = models.PositiveSmallIntegerField(null=True, blank=True)
    issued_year  = models.PositiveSmallIntegerField(null=True, blank=True)
    issuer      = models.CharField(max_length=255, null=True, blank=True)
    content     = models.TextField()
    sort_order  = models.PositiveSmallIntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profile_awards'
        verbose_name = 'Khen thưởng / Kỷ luật'
        verbose_name_plural = 'Khen thưởng / Kỷ luật'
        ordering = ['issued_year', 'issued_month']

    def __str__(self):
        return f'{self.get_type_display()}: {self.content[:50]}'


class OverseasTravel(models.Model):
    profile        = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='overseas_travels')
    period_text    = models.CharField(max_length=255, null=True, blank=True)
    from_month     = models.PositiveSmallIntegerField(null=True, blank=True)
    from_year      = models.PositiveSmallIntegerField(null=True, blank=True)
    to_month       = models.PositiveSmallIntegerField(null=True, blank=True)
    to_year        = models.PositiveSmallIntegerField(null=True, blank=True)
    country        = models.CharField(max_length=200)
    purpose        = models.CharField(max_length=500, null=True, blank=True)
    sponsoring_org = models.CharField(max_length=500, null=True, blank=True)
    notes          = models.TextField(null=True, blank=True)
    sort_order     = models.PositiveSmallIntegerField(default=0)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profile_overseas_travel'
        verbose_name = 'Ra nước ngoài'
        verbose_name_plural = 'Ra nước ngoài'

    def __str__(self):
        return f'{self.country} – {self.purpose}'


class OverseasRelative(models.Model):
    profile      = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='overseas_relatives')
    full_name    = models.CharField(max_length=255)
    relationship = models.CharField(max_length=100, null=True, blank=True)
    country      = models.CharField(max_length=200)
    address      = models.CharField(max_length=500, null=True, blank=True)
    occupation   = models.CharField(max_length=255, null=True, blank=True)
    notes        = models.TextField(null=True, blank=True)
    sort_order   = models.PositiveSmallIntegerField(default=0)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profile_overseas_relatives'
        verbose_name = 'Người thân ở nước ngoài'
        verbose_name_plural = 'Người thân ở nước ngoài'

    def __str__(self):
        return f'{self.full_name} – {self.country}'
