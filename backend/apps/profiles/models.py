from django.db import models
from django.utils import timezone


class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE   = 'male',   'Nam'
        FEMALE = 'female', 'Nữ'
        OTHER  = 'other',  'Khác'

    class MaritalStatus(models.TextChoices):
        SINGLE   = 'single',   'Độc thân'
        MARRIED  = 'married',  'Đã kết hôn'
        DIVORCED = 'divorced', 'Ly hôn'
        WIDOWED  = 'widowed',  'Góa'

    class ResidenceType(models.TextChoices):
        HO_KHAU = 'ho_khau', 'Hộ khẩu thường trú'
        TAM_TRU = 'tam_tru', 'Tạm trú'
        OTHER   = 'other',   'Khác'

    class Status(models.TextChoices):
        DRAFT        = 'draft',        'Đang kê khai'
        SUBMITTED    = 'submitted',    'Đã nộp'
        PENDING      = 'pending',      'Đang xem xét'
        UNDER_REVIEW = 'under_review', 'Đang thẩm định'
        RETURNED     = 'returned',     'Trả lại'
        VERIFYING    = 'verifying',    'Đang xác minh'
        APPROVED     = 'approved',     'Đã phê duyệt'
        COMPLETED    = 'completed',    'Hoàn thiện'
        REJECTED     = 'rejected',     'Từ chối'
        WITHDRAWN    = 'withdrawn',    'Rút hồ sơ'

    user              = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name='profile')
    officer_in_charge = models.ForeignKey('accounts.User', null=True, blank=True,
                                          on_delete=models.SET_NULL, related_name='managed_profiles',
                                          db_column='officer_in_charge_id')
    profile_number    = models.CharField(max_length=50, null=True, blank=True, unique=True)

    # ── Section A: Basic information ────────────────────────────────────────
    full_name            = models.CharField(max_length=255)
    full_name_other      = models.CharField(max_length=255, null=True, blank=True)
    gender               = models.CharField(max_length=10, choices=Gender.choices)
    dob                  = models.DateField()

    # Nơi sinh
    birth_place_province_text = models.CharField(max_length=255, null=True, blank=True)
    birth_place_old_name      = models.CharField(max_length=255, null=True, blank=True)
    birth_place_detail        = models.CharField(max_length=500, null=True, blank=True)
    birth_place_ward          = models.ForeignKey('common.AdministrativeUnit', null=True, blank=True,
                                                   on_delete=models.SET_NULL, related_name='birth_profiles',
                                                   db_column='birth_place_ward_id')

    # Dân tộc / Tôn giáo
    ethnic_group    = models.ForeignKey('common.EthnicGroup', null=True, blank=True, on_delete=models.SET_NULL,
                                         db_column='ethnic_group_id')
    ethnic_group_other = models.CharField(max_length=100, null=True, blank=True)
    religion        = models.ForeignKey('common.Religion', null=True, blank=True, on_delete=models.SET_NULL,
                                         db_column='religion_id')
    religion_other  = models.CharField(max_length=100, null=True, blank=True)
    religious_title = models.CharField(max_length=100, null=True, blank=True)

    # Quê quán
    hometown_detail  = models.CharField(max_length=500, null=True, blank=True)
    hometown_ward    = models.ForeignKey('common.AdministrativeUnit', null=True, blank=True,
                                          on_delete=models.SET_NULL, related_name='hometown_profiles',
                                          db_column='hometown_ward_id')

    # Thường trú
    current_address_number = models.CharField(max_length=100, null=True, blank=True)
    current_address_street = models.CharField(max_length=255, null=True, blank=True)
    current_address        = models.CharField(max_length=500, null=True, blank=True)
    current_ward           = models.ForeignKey('common.AdministrativeUnit', null=True, blank=True,
                                                on_delete=models.SET_NULL, related_name='current_profiles',
                                                db_column='current_ward_id')
    residence_type         = models.CharField(max_length=20, choices=ResidenceType.choices, null=True, blank=True)

    # Tạm trú
    temporary_ward           = models.ForeignKey('common.AdministrativeUnit', null=True, blank=True,
                                                   on_delete=models.SET_NULL, related_name='temporary_profiles',
                                                   db_column='temporary_ward_id')
    temporary_address_number = models.CharField(max_length=100, null=True, blank=True)
    temporary_address_street = models.CharField(max_length=255, null=True, blank=True)
    temporary_address        = models.CharField(max_length=500, null=True, blank=True)

    # ── Trình độ ───────────────────────────────────────────────────────────
    general_edu_level    = models.CharField(max_length=120, null=True, blank=True)
    edu_level            = models.ForeignKey('common.EducationLevel', null=True, blank=True,
                                              on_delete=models.SET_NULL, db_column='edu_level_id')
    edu_specialization   = models.CharField(max_length=255, null=True, blank=True)
    edu_school           = models.CharField(max_length=255, null=True, blank=True)
    edu_major            = models.CharField(max_length=255, null=True, blank=True)
    edu_graduation_year  = models.PositiveSmallIntegerField(null=True, blank=True)
    academic_degree_major = models.CharField(max_length=255, null=True, blank=True)
    highest_degree       = models.CharField(max_length=120, null=True, blank=True)
    academic_title_level = models.CharField(max_length=100, null=True, blank=True)
    academic_title       = models.CharField(max_length=120, null=True, blank=True)
    political_level      = models.ForeignKey('common.PoliticalLevel', null=True, blank=True,
                                              on_delete=models.SET_NULL, db_column='political_level_id')
    political_level_detail = models.CharField(max_length=255, null=True, blank=True)
    political_school     = models.CharField(max_length=255, null=True, blank=True)
    science_tech_qualifications = models.TextField(null=True, blank=True)
    foreign_language_name  = models.CharField(max_length=120, null=True, blank=True)
    foreign_language_level = models.CharField(max_length=120, null=True, blank=True)
    foreign_languages    = models.CharField(max_length=500, null=True, blank=True)
    it_level             = models.CharField(max_length=120, null=True, blank=True)
    ethnic_language      = models.CharField(max_length=255, null=True, blank=True)
    professional_certs   = models.TextField(null=True, blank=True)

    # ── Nghề nghiệp ────────────────────────────────────────────────────────
    occupation      = models.CharField(max_length=255, null=True, blank=True)
    workplace       = models.CharField(max_length=500, null=True, blank=True)
    workplace_address = models.CharField(max_length=500, null=True, blank=True)
    job_title       = models.CharField(max_length=255, null=True, blank=True)

    # ── Đoàn thể ───────────────────────────────────────────────────────────
    youth_union_date   = models.DateField(null=True, blank=True)
    youth_union_place  = models.CharField(max_length=255, null=True, blank=True)
    other_organizations = models.TextField(null=True, blank=True)

    # ── Kết nạp lại ────────────────────────────────────────────────────────
    rejoin_first_party_join_date    = models.DateField(null=True, blank=True)
    rejoin_first_party_join_place   = models.CharField(max_length=255, null=True, blank=True)
    rejoin_first_official_date      = models.DateField(null=True, blank=True)
    rejoin_introducer1_name         = models.CharField(max_length=255, null=True, blank=True)
    rejoin_introducer1_position     = models.CharField(max_length=255, null=True, blank=True)
    rejoin_introducer2_name         = models.CharField(max_length=255, null=True, blank=True)
    rejoin_introducer2_position     = models.CharField(max_length=255, null=True, blank=True)

    # ── Hôn nhân ───────────────────────────────────────────────────────────
    marital_status = models.CharField(max_length=20, choices=MaritalStatus.choices, null=True, blank=True)
    marriage_date  = models.DateField(null=True, blank=True)
    divorce_date   = models.DateField(null=True, blank=True)

    # ── Quân sự ────────────────────────────────────────────────────────────
    military_service          = models.BooleanField(default=False)
    military_start            = models.DateField(null=True, blank=True)
    military_end              = models.DateField(null=True, blank=True)
    military_rank             = models.CharField(max_length=100, null=True, blank=True)
    military_unit             = models.CharField(max_length=255, null=True, blank=True)
    military_discharge_reason = models.CharField(max_length=255, null=True, blank=True)

    # ── Lịch sử chính trị (Section D) ──────────────────────────────────────
    political_history_text = models.TextField(null=True, blank=True)

    # ── Khen thưởng / Kỷ luật summary ──────────────────────────────────────
    awards_text      = models.TextField(null=True, blank=True)
    disciplines_text = models.TextField(null=True, blank=True)

    # ── Tự nhận xét (Section J) ─────────────────────────────────────────────
    self_assessment_text       = models.TextField(null=True, blank=True)
    self_assessment_word_count = models.PositiveSmallIntegerField(null=True, blank=True)

    # ── Cam đoan (Section K) ─────────────────────────────────────────────────
    declaration_name  = models.CharField(max_length=255, null=True, blank=True)
    declaration_date  = models.DateField(null=True, blank=True)
    declarant_signature = models.CharField(max_length=255, null=True, blank=True)

    # ── Photo ────────────────────────────────────────────────────────────────
    photo_file = models.ForeignKey('uploads.UploadedFile', null=True, blank=True,
                                    on_delete=models.SET_NULL, related_name='profile_photos',
                                    db_column='photo_file_id')

    # ── AI ───────────────────────────────────────────────────────────────────
    ai_score          = models.PositiveSmallIntegerField(null=True, blank=True)
    ai_last_scanned_at = models.DateTimeField(null=True, blank=True)
    ai_issues_json    = models.JSONField(null=True, blank=True)

    # ── Workflow ─────────────────────────────────────────────────────────────
    status           = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    submitted_at     = models.DateTimeField(null=True, blank=True)
    approved_at      = models.DateTimeField(null=True, blank=True)
    approved_by      = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL,
                                          related_name='approved_profiles', db_column='approved_by')
    completed_at     = models.DateTimeField(null=True, blank=True)
    last_returned_at = models.DateTimeField(null=True, blank=True)
    return_reason    = models.TextField(null=True, blank=True)
    rejected_at      = models.DateTimeField(null=True, blank=True)
    rejected_reason  = models.TextField(null=True, blank=True)

    # ── Audit ─────────────────────────────────────────────────────────────────
    created_by = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL,
                                    related_name='created_profiles', db_column='created_by')
    updated_by = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL,
                                    related_name='updated_profiles', db_column='updated_by')
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profiles'
        verbose_name = 'Hồ sơ lý lịch'
        verbose_name_plural = 'Hồ sơ lý lịch'
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['full_name']),
            models.Index(fields=['dob']),
            models.Index(fields=['deleted_at']),
            models.Index(fields=['ai_score']),
            models.Index(fields=['submitted_at']),
        ]

    def __str__(self):
        return f'{self.full_name} – {self.get_status_display()}'

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save(update_fields=['deleted_at'])

    @property
    def is_editable_by_applicant(self):
        return self.status in (self.Status.DRAFT, self.Status.RETURNED)


class ProfileOfficerAssignment(models.Model):
    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='officer_assignments')
    officer     = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='profile_assignments')
    assigned_by = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name='made_assignments', db_column='assigned_by')
    note        = models.CharField(max_length=500, null=True, blank=True)
    assigned_at = models.DateTimeField(auto_now_add=True)
    revoked_at  = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'profile_officer_assignments'
        verbose_name = 'Phân công cán bộ'
        verbose_name_plural = 'Phân công cán bộ'

    def __str__(self):
        return f'{self.profile} ← {self.officer}'


class ProfileReview(models.Model):
    class Action(models.TextChoices):
        SUBMIT         = 'submit',         'Nộp hồ sơ'
        RETURN         = 'return',         'Trả lại'
        APPROVE        = 'approve',        'Phê duyệt'
        REJECT         = 'reject',         'Từ chối'
        REQUEST_VERIFY = 'request_verify', 'Yêu cầu xác minh'
        COMPLETE       = 'complete',       'Hoàn thiện'
        WITHDRAW       = 'withdraw',       'Rút hồ sơ'
        REOPEN         = 'reopen',         'Mở lại'
        NOTE           = 'note',           'Ghi chú'

    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews')
    reviewer    = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='reviews')
    action      = models.CharField(max_length=20, choices=Action.choices)
    from_status = models.CharField(max_length=40, null=True, blank=True)
    to_status   = models.CharField(max_length=40, null=True, blank=True)
    comment     = models.TextField(null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'profile_reviews'
        verbose_name = 'Lịch sử thẩm định'
        verbose_name_plural = 'Lịch sử thẩm định'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['profile', '-created_at']),
            models.Index(fields=['action']),
        ]

    def __str__(self):
        return f'{self.profile} – {self.action}'


class CommitteeComment(models.Model):
    class CommentType(models.TextChoices):
        CHI_UY       = 'chi_uy',       'Ý kiến Chi ủy'
        CAP_UY_CO_SO = 'cap_uy_co_so', 'Ý kiến Cấp ủy cơ sở'

    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='committee_comments')
    type        = models.CharField(max_length=20, choices=CommentType.choices)
    content     = models.TextField(null=True, blank=True)
    signed_by   = models.CharField(max_length=255, null=True, blank=True)
    signed_date = models.DateField(null=True, blank=True)
    updated_by  = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name='updated_comments', db_column='updated_by')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'committee_comments'
        verbose_name = 'Nhận xét Ủy ban'
        verbose_name_plural = 'Nhận xét Ủy ban'

    def __str__(self):
        return f'{self.profile} – {self.type}'


class ProfileFieldNote(models.Model):
    """Per-field or per-section review notes written by officers.
    Officers add notes requesting corrections; citizens see them when the profile is returned.
    """
    profile    = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='field_notes')
    field_key  = models.CharField(max_length=100)  # e.g. "secA", "secB", "full_name"
    note       = models.TextField(blank=True)
    reviewer   = models.ForeignKey('accounts.User', on_delete=models.PROTECT,
                                    related_name='field_notes_authored')
    resolved   = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table        = 'profile_field_notes'
        unique_together = [['profile', 'field_key']]
        verbose_name    = 'Nhận xét trường hồ sơ'
        verbose_name_plural = 'Nhận xét trường hồ sơ'
        ordering        = ['field_key']

    def __str__(self):
        return f'{self.profile_id}:{self.field_key}'
