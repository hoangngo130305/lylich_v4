from django.db import models


class EthnicGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'ref_ethnic_groups'
        verbose_name = 'Dân tộc'
        verbose_name_plural = 'Dân tộc'
        ordering = ['name']

    def __str__(self):
        return self.name


class Religion(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'ref_religions'
        verbose_name = 'Tôn giáo'
        verbose_name_plural = 'Tôn giáo'
        ordering = ['name']

    def __str__(self):
        return self.name


class EducationLevel(models.Model):
    code = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=120)
    sort = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'ref_education_levels'
        verbose_name = 'Trình độ học vấn'
        verbose_name_plural = 'Trình độ học vấn'
        ordering = ['sort']

    def __str__(self):
        return self.name


class PoliticalLevel(models.Model):
    code = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=120)

    class Meta:
        db_table = 'ref_political_levels'
        verbose_name = 'Trình độ chính trị'
        verbose_name_plural = 'Trình độ chính trị'
        ordering = ['name']

    def __str__(self):
        return self.name


class AdministrativeUnit(models.Model):
    class UnitType(models.TextChoices):
        PROVINCE = 'province', 'Tỉnh/Thành phố'
        DISTRICT = 'district', 'Huyện/Quận'
        WARD     = 'ward',     'Xã/Phường/Thị trấn'
        HAMLET   = 'hamlet',   'Ấp/Thôn/Bản'

    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='children', db_column='parent_id'
    )
    type = models.CharField(max_length=20, choices=UnitType.choices)
    code = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'ref_administrative_units'
        verbose_name = 'Đơn vị hành chính'
        verbose_name_plural = 'Đơn vị hành chính'
        indexes = [
            models.Index(fields=['parent_id']),
            models.Index(fields=['type']),
        ]

    def __str__(self):
        return f'{self.get_type_display()} {self.name}'
