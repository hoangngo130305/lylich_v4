from django.contrib import admin
from django.db.models import DateField
from django.forms.widgets import DateInput
from django.http import HttpResponse
from unfold.admin import ModelAdmin, TabularInline
from .models import Profile, ProfileReview, CommitteeComment, ProfileOfficerAssignment
import zipfile
import io
import re

_DATE_WIDGET = DateInput(attrs={'type': 'text', 'placeholder': 'dd/mm/yyyy'}, format='%d/%m/%Y')


class ProfileReviewInline(TabularInline):
    model = ProfileReview
    extra = 0
    readonly_fields = ['reviewer', 'action', 'from_status', 'to_status', 'comment', 'created_at']
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False


class CommitteeCommentInline(TabularInline):
    model = CommitteeComment
    extra = 0
    readonly_fields = ['created_at', 'updated_at']


@admin.action(description='Xuất Word Mẫu 2-KNĐ (hàng loạt)')
def export_word_bulk(modeladmin, request, queryset):
    from apps.exports.word_builder import build_profile_docx as build_lylich_docx
    from apps.exports.models import WordExportLog

    profiles = queryset.select_related(
        'user', 'ethnic_group', 'religion', 'edu_level', 'political_level',
        'officer_in_charge', 'current_ward', 'birth_place_ward', 'hometown_ward',
    ).prefetch_related(
        'committee_comments', 'family_members', 'history_entries',
        'work_history', 'education_history', 'awards', 'overseas_travels',
    )

    if profiles.count() == 1:
        profile = profiles.first()
        try:
            buf = build_lylich_docx(profile)
            content = buf.read()
            safe_name = re.sub(r'[^\w\-]', '_', profile.full_name or 'profile')
            file_name = f'SoYeuLyLich_{safe_name}.docx'
            WordExportLog.objects.create(
                profile=profile, exported_by=request.user,
                template_name='Mẫu 2-KNĐ', file_name=file_name, file_size=len(content),
            )
            response = HttpResponse(content, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
        except Exception as e:
            import traceback
            print(f"[EXPORT ERROR] Failed to export {profile.id}: {e}\n{traceback.format_exc()}")
            raise

    zip_buf = io.BytesIO()
    error_count = 0
    with zipfile.ZipFile(zip_buf, 'w', zipfile.ZIP_DEFLATED) as zf:
        for profile in profiles:
            try:
                buf = build_lylich_docx(profile)
                content = buf.read()
                safe_name = re.sub(r'[^\w\-]', '_', profile.full_name or f'profile_{profile.id}')
                file_name = f'SoYeuLyLich_{safe_name}.docx'
                zf.writestr(file_name, content)
                WordExportLog.objects.create(
                    profile=profile, exported_by=request.user,
                    template_name='Mẫu 2-KNĐ', file_name=file_name, file_size=len(content),
                )
            except Exception as e:
                error_count += 1
                import traceback
                print(f"[EXPORT ERROR] Failed to export profile {profile.id}: {e}\n{traceback.format_exc()}")
                continue
    zip_buf.seek(0)
    response = HttpResponse(zip_buf.read(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="LyLich_export.zip"'
    return response


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    actions = [export_word_bulk]

    formfield_overrides = {
        DateField: {'widget': _DATE_WIDGET},
    }

    def _ward_display(self, obj, field_name):
        ward = getattr(obj, field_name, None)
        return str(ward) if ward else '—'

    def submitted_date_display(self, obj):
        if obj.submitted_at:
            try:
                return obj.submitted_at.strftime('%d/%m/%Y %H:%M')
            except (ValueError, TypeError, AttributeError):
                return '—'
        return '—'
    submitted_date_display.short_description = 'Ngày nộp'

    def hometown_ward_display(self, obj):
        return self._ward_display(obj, 'hometown_ward')
    hometown_ward_display.short_description = 'Quê quán (Xã → Tỉnh)'

    def birth_place_ward_display(self, obj):
        return self._ward_display(obj, 'birth_place_ward')
    birth_place_ward_display.short_description = 'Nơi sinh (Xã → Tỉnh)'

    def current_ward_display(self, obj):
        return self._ward_display(obj, 'current_ward')
    current_ward_display.short_description = 'Nơi thường trú (Xã → Tỉnh)'

    list_display  = [
        'id', 'profile_number', 'full_name', 'gender', 'dob',
        'status', 'ai_score', 'officer_in_charge', 'submitted_date_display',
    ]
    list_filter   = ['status', 'gender', 'marital_status', 'ethnic_group', 'religion']
    search_fields = ['full_name', 'profile_number', 'user__phone', 'user__cccd']
    readonly_fields = [
        'ai_score', 'ai_last_scanned_at', 'ai_issues_json',
        'submitted_at', 'approved_at', 'approved_by', 'completed_at',
        'last_returned_at', 'rejected_at', 'created_at', 'updated_at', 'deleted_at',
        'hometown_ward_display', 'birth_place_ward_display', 'current_ward_display',
        'submitted_date_display',
    ]
    raw_id_fields = ['user', 'officer_in_charge', 'approved_by', 'photo_file',
                     'ethnic_group', 'religion', 'edu_level', 'political_level',
                     'current_ward', 'hometown_ward', 'birth_place_ward', 'temporary_ward']
    inlines = [ProfileReviewInline, CommitteeCommentInline]
    ordering = ['-created_at']

    fieldsets = (
        ('Thông tin cơ bản (Phần A)', {
            'fields': (
                'user', 'profile_number', 'officer_in_charge',
                'full_name', 'full_name_other', 'gender', 'dob',
                'birth_place_province_text', 'birth_place_old_name', 'birth_place_detail',
                'birth_place_ward', 'birth_place_ward_display',
                'ethnic_group', 'ethnic_group_other', 'religion', 'religion_other', 'religious_title',
                'hometown_detail', 'hometown_ward', 'hometown_ward_display',
                'current_address_number', 'current_address_street', 'current_address',
                'current_ward', 'current_ward_display',
                'temporary_ward', 'temporary_address_number', 'temporary_address_street',
            )
        }),
        ('Trình độ', {
            'fields': (
                'general_edu_level', 'edu_level', 'edu_specialization', 'edu_school', 'edu_major',
                'highest_degree', 'academic_degree_major', 'academic_title', 'academic_title_level',
                'political_level', 'political_level_detail',
                'foreign_language_name', 'foreign_language_level', 'it_level', 'ethnic_language',
            ),
            'classes': ('collapse',),
        }),
        ('Nghề nghiệp & Đoàn thể', {
            'fields': ('occupation', 'workplace', 'job_title', 'youth_union_date', 'youth_union_place'),
            'classes': ('collapse',),
        }),
        ('Lịch sử chính trị / Tự nhận xét', {
            'fields': ('political_history_text', 'self_assessment_text', 'self_assessment_word_count'),
            'classes': ('collapse',),
        }),
        ('Trạng thái & AI', {
            'fields': ('status', 'ai_score', 'ai_last_scanned_at', 'return_reason', 'rejected_reason'),
        }),
        ('Thời gian', {
            'fields': ('submitted_at', 'approved_at', 'completed_at', 'created_at', 'updated_at', 'deleted_at'),
            'classes': ('collapse',),
        }),
    )


@admin.register(ProfileReview)
class ProfileReviewAdmin(ModelAdmin):
    def review_date_display(self, obj):
        if obj.created_at:
            try:
                return obj.created_at.strftime('%d/%m/%Y %H:%M')
            except (ValueError, TypeError, AttributeError):
                return '—'
        return '—'
    review_date_display.short_description = 'Ngày'

    list_display  = ['id', 'profile', 'reviewer', 'action', 'from_status', 'to_status', 'review_date_display']
    list_filter   = ['action']
    search_fields = ['profile__full_name', 'reviewer__full_name']
    readonly_fields = ['created_at', 'review_date_display']
    raw_id_fields   = ['profile', 'reviewer']

    def has_change_permission(self, request, obj=None):
        return False
