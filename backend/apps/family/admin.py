from django import forms
from django.contrib import admin
from django.db.models import DateField
from django.forms.widgets import DateInput
from unfold.admin import ModelAdmin, TabularInline
from .models import FamilyMember

ETHNIC_CHOICES = [
    ('', '-- Chọn --'),
    ('Kinh', 'Kinh'), ('Tày', 'Tày'), ('Thái', 'Thái'), ('Mường', 'Mường'),
    ('Khmer', 'Khmer'), ('Nùng', 'Nùng'), ('HMông', 'HMông'), ('Dao', 'Dao'),
    ('Gia Rai', 'Gia Rai'), ('Ê Đê', 'Ê Đê'), ('Ba Na', 'Ba Na'),
    ('Xơ Đăng', 'Xơ Đăng'), ('Sán Chay', 'Sán Chay'), ('Cơ Ho', 'Cơ Ho'),
    ('Chăm', 'Chăm'), ('Sán Dìu', 'Sán Dìu'), ('Hrê', 'Hrê'),
    ('Mnông', 'Mnông'), ('Ra Glai', 'Ra Glai'), ('Xinh Mun', 'Xinh Mun'),
    ('Khác', 'Khác (nhập bên dưới)'),
]

RELIGION_CHOICES = [
    ('', '-- Chọn --'),
    ('Không', 'Không'),
    ('Phật giáo', 'Phật giáo'), ('Công giáo', 'Công giáo'),
    ('Cao Đài', 'Cao Đài'), ('Hòa Hảo', 'Hòa Hảo'),
    ('Tin Lành', 'Tin Lành'), ('Hồi giáo', 'Hồi giáo'),
    ('Khác', 'Khác (nhập bên dưới)'),
]

_KNOWN_ETHNIC = {c[0] for c in ETHNIC_CHOICES if c[0]}
_KNOWN_RELIGION = {c[0] for c in RELIGION_CHOICES if c[0]}


class FamilyMemberAdminForm(forms.ModelForm):
    ethnic_group_select = forms.ChoiceField(
        choices=ETHNIC_CHOICES, required=False,
        label='Dân tộc',
        help_text='Chọn "Khác" rồi nhập vào ô Dân tộc (khác) bên dưới.',
    )
    religion_select = forms.ChoiceField(
        choices=RELIGION_CHOICES, required=False,
        label='Tôn giáo',
        help_text='Chọn "Khác" rồi nhập vào ô Tôn giáo (khác) bên dưới.',
    )

    class Meta:
        model = FamilyMember
        fields = '__all__'
        widgets = {
            'dob': DateInput(attrs={'type': 'text', 'placeholder': 'dd/mm/yyyy'}, format='%d/%m/%Y'),
            'party_join_date': DateInput(attrs={'type': 'text', 'placeholder': 'dd/mm/yyyy'}, format='%d/%m/%Y'),
            'ethnic_group_text': forms.TextInput(attrs={'placeholder': 'Nhập tên dân tộc khác…'}),
            'religion_text': forms.TextInput(attrs={'placeholder': 'Nhập tên tôn giáo khác…'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            val = instance.ethnic_group_text or ''
            self.fields['ethnic_group_select'].initial = val if val in _KNOWN_ETHNIC else ('Khác' if val else '')
            val_r = instance.religion_text or ''
            self.fields['religion_select'].initial = val_r if val_r in _KNOWN_RELIGION else ('Khác' if val_r else '')

    def clean(self):
        cleaned = super().clean()
        ethnic_sel = cleaned.get('ethnic_group_select', '')
        if ethnic_sel and ethnic_sel != 'Khác':
            cleaned['ethnic_group_text'] = ethnic_sel
        rel_sel = cleaned.get('religion_select', '')
        if rel_sel and rel_sel != 'Khác':
            cleaned['religion_text'] = rel_sel
        return cleaned


def _build_history_inline():
    from apps.timelines.models import HistoryEntry

    class HistoryEntryInline(TabularInline):
        model = HistoryEntry
        fk_name = 'family_member'
        extra = 1
        fields = ['from_year', 'from_month', 'to_year', 'to_month', 'is_present', 'description', 'sort_order']
        verbose_name = 'Giai đoạn lịch sử'
        verbose_name_plural = 'Quá trình lịch sử thân nhân'

        def get_queryset(self, request):
            return super().get_queryset(request).filter(entry_type='family')

        def save_formset(self, request, form, formset, change):
            instances = formset.save(commit=False)
            for obj in instances:
                obj.entry_type = 'family'
                obj.profile_id = form.instance.profile_id
                obj.save()
            for obj in formset.deleted_objects:
                obj.delete()
            formset.save_m2m()

    return HistoryEntryInline


@admin.register(FamilyMember)
class FamilyMemberAdmin(ModelAdmin):
    form = FamilyMemberAdminForm
    inlines = [_build_history_inline()]

    formfield_overrides = {
        DateField: {'widget': DateInput(attrs={'type': 'text', 'placeholder': 'dd/mm/yyyy'}, format='%d/%m/%Y')},
    }

    list_display  = ['id', 'profile', 'relationship', 'full_name', 'birth_year', 'is_party_member']
    list_filter   = ['relationship', 'is_party_member', 'is_deceased']
    search_fields = ['full_name', 'profile__full_name']
    raw_id_fields = ['profile', 'updated_by']
    readonly_fields = ['created_at', 'updated_at', 'deleted_at']

    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': (
                'profile', 'relationship', 'sort_order',
                'full_name', 'gender', 'dob', 'birth_year',
            ),
        }),
        ('Địa chỉ & Quê quán', {
            'fields': ('birth_province_text', 'birth_place', 'hometown_province_text', 'hometown', 'current_address'),
        }),
        ('Dân tộc & Tôn giáo', {
            'fields': ('ethnic_group_select', 'ethnic_group_text', 'religion_select', 'religion_text'),
            'description': 'Chọn từ danh sách. Nếu chọn "Khác", hãy nhập tên vào ô bên dưới.',
        }),
        ('Nghề nghiệp', {
            'fields': ('occupation', 'workplace', 'job_title'),
        }),
        ('Tình trạng', {
            'fields': ('is_deceased', 'deceased_year', 'deceased_cause'),
        }),
        ('Đảng viên', {
            'fields': (
                'is_party_member', 'party_join_year', 'party_chi_bo', 'party_dang_bo',
                'party_awards_text', 'party_years_count',
                'party_join_date', 'party_join_place',
            ),
            'classes': ('collapse',),
        }),
        ('Khác', {
            'fields': ('nationality', 'child_school', 'notes', 'updated_by', 'deleted_at', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
