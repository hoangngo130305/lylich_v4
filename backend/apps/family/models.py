from django.db import models
from django.db.models import Case, When, Value, IntegerField


class FamilyMember(models.Model):
    class Relationship(models.TextChoices):
        CHA_RUOT            = 'cha_ruot',            'Cha ruột'
        CHA_DUONG           = 'cha_duong',           'Cha dượng'
        ME_RUOT             = 'me_ruot',             'Mẹ ruột'
        ME_KE               = 'me_ke',               'Mẹ kế'
        ANH_CHI_EM_RUOT     = 'anh_chi_em_ruot',     'Anh/Chị/Em ruột'
        VO_CHONG            = 'vo_chong',            'Vợ/Chồng'
        CHONG_KE            = 'chong_ke',            'Chồng kế'
        VO_KE               = 'vo_ke',               'Vợ kế'
        CHA_CHONG_VO        = 'cha_chong_vo',        'Cha chồng/vợ'
        ME_CHONG_VO         = 'me_chong_vo',         'Mẹ chồng/vợ'
        ONG_NOI             = 'ong_noi',             'Ông nội'
        BA_NOI              = 'ba_noi',              'Bà nội'
        ONG_NGOAI           = 'ong_ngoai',           'Ông ngoại'
        BA_NGOAI            = 'ba_ngoai',            'Bà ngoại'
        ANH_CHI_EM_CHONG_VO = 'anh_chi_em_chong_vo', 'Anh/Chị/Em chồng/vợ'
        ONG_NOI_CHONG_VO    = 'ong_noi_chong_vo',    'Ông nội chồng/vợ'
        BA_NOI_CHONG_VO     = 'ba_noi_chong_vo',     'Bà nội chồng/vợ'
        ONG_NGOAI_CHONG_VO  = 'ong_ngoai_chong_vo',  'Ông ngoại chồng/vợ'
        BA_NGOAI_CHONG_VO   = 'ba_ngoai_chong_vo',   'Bà ngoại chồng/vợ'
        ONG_BA_KHAC         = 'ong_ba_khac',         'Ông/Bà khác'
        CON                 = 'con',                 'Con'

    class Gender(models.TextChoices):
        MALE   = 'male',   'Nam'
        FEMALE = 'female', 'Nữ'
        OTHER  = 'other',  'Khác'

    profile      = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='family_members')
    relationship = models.CharField(max_length=30, choices=Relationship.choices)
    sort_order   = models.PositiveSmallIntegerField(default=0)

    full_name  = models.CharField(max_length=255)
    gender     = models.CharField(max_length=10, choices=Gender.choices, null=True, blank=True)
    dob        = models.DateField(null=True, blank=True)
    birth_year = models.PositiveSmallIntegerField(null=True, blank=True)

    birth_province_text    = models.CharField(max_length=255, null=True, blank=True)
    birth_place            = models.CharField(max_length=500, null=True, blank=True)
    hometown_province_text = models.CharField(max_length=255, null=True, blank=True)
    hometown               = models.CharField(max_length=500, null=True, blank=True)
    current_address        = models.CharField(max_length=500, null=True, blank=True)

    ethnic_group_text  = models.CharField(max_length=100, null=True, blank=True)
    religion_text      = models.CharField(max_length=100, null=True, blank=True)
    religious_rank_text = models.CharField(max_length=100, null=True, blank=True)
    nationality        = models.CharField(max_length=100, null=True, blank=True)

    occupation = models.CharField(max_length=255, null=True, blank=True)
    workplace  = models.CharField(max_length=500, null=True, blank=True)
    job_title  = models.CharField(max_length=255, null=True, blank=True)

    is_deceased    = models.BooleanField(default=False)
    deceased_year  = models.PositiveSmallIntegerField(null=True, blank=True)
    deceased_cause = models.CharField(max_length=255, null=True, blank=True)

    # Đảng viên
    is_party_member  = models.BooleanField(default=False)
    party_join_year  = models.PositiveSmallIntegerField(null=True, blank=True)
    party_chi_bo     = models.CharField(max_length=255, null=True, blank=True)
    party_dang_bo    = models.CharField(max_length=255, null=True, blank=True)
    party_awards_text = models.TextField(null=True, blank=True)
    party_years_count = models.PositiveSmallIntegerField(null=True, blank=True)

    # Legacy
    political_status  = models.CharField(max_length=255, null=True, blank=True)
    party_join_date   = models.DateField(null=True, blank=True)
    party_join_place  = models.CharField(max_length=255, null=True, blank=True)
    awards_disciplines = models.TextField(null=True, blank=True)

    # Con dưới 18
    child_school = models.CharField(max_length=255, null=True, blank=True)

    custom_label = models.CharField(max_length=150, null=True, blank=True)

    notes      = models.TextField(null=True, blank=True)
    updated_by = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL,
                                    related_name='updated_family_members', db_column='updated_by')
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'family_members'
        verbose_name = 'Thành viên gia đình'
        verbose_name_plural = 'Thành viên gia đình'
        ordering = [
            Case(
                When(relationship='cha_ruot',            then=Value(1)),
                When(relationship='cha_duong',           then=Value(2)),
                When(relationship='me_ruot',             then=Value(3)),
                When(relationship='me_ke',               then=Value(4)),
                When(relationship='anh_chi_em_ruot',     then=Value(5)),
                When(relationship='vo_chong',            then=Value(6)),
                When(relationship='chong_ke',            then=Value(7)),
                When(relationship='vo_ke',               then=Value(8)),
                When(relationship='con',                 then=Value(9)),
                When(relationship='ong_noi',             then=Value(10)),
                When(relationship='ba_noi',              then=Value(11)),
                When(relationship='ong_ngoai',           then=Value(12)),
                When(relationship='ba_ngoai',            then=Value(13)),
                When(relationship='cha_chong_vo',        then=Value(14)),
                When(relationship='me_chong_vo',         then=Value(15)),
                When(relationship='anh_chi_em_chong_vo', then=Value(16)),
                When(relationship='ong_noi_chong_vo',    then=Value(17)),
                When(relationship='ba_noi_chong_vo',     then=Value(18)),
                When(relationship='ong_ngoai_chong_vo',  then=Value(19)),
                When(relationship='ba_ngoai_chong_vo',   then=Value(20)),
                When(relationship='ong_ba_khac',         then=Value(21)),
                default=Value(99),
                output_field=IntegerField(),
            ),
            'sort_order'
        ]
        indexes = [
            models.Index(fields=['profile', 'relationship']),
            models.Index(fields=['full_name']),
        ]

    def __str__(self):
        return f'{self.get_relationship_display()}: {self.full_name}'
