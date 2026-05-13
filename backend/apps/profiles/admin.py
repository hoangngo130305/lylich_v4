from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Profile, ProfileReview, CommitteeComment, ProfileOfficerAssignment


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


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display  = [
        'id', 'profile_number', 'full_name', 'gender', 'dob',
        'status', 'ai_score', 'officer_in_charge', 'submitted_at', 'created_at',
    ]
    list_filter   = ['status', 'gender', 'marital_status', 'ethnic_group', 'religion']
    search_fields = ['full_name', 'profile_number', 'user__phone', 'user__cccd']
    readonly_fields = [
        'ai_score', 'ai_last_scanned_at', 'ai_issues_json',
        'submitted_at', 'approved_at', 'approved_by', 'completed_at',
        'last_returned_at', 'rejected_at', 'created_at', 'updated_at', 'deleted_at',
    ]
    raw_id_fields = ['user', 'officer_in_charge', 'approved_by', 'photo_file',
                     'ethnic_group', 'religion', 'edu_level', 'political_level',
                     'current_ward', 'hometown_ward', 'birth_place_ward', 'temporary_ward']
    inlines = [ProfileReviewInline, CommitteeCommentInline]
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

    fieldsets = (
        ('Thông tin cơ bản (Phần A)', {
            'fields': (
                'user', 'profile_number', 'officer_in_charge',
                'full_name', 'full_name_other', 'gender', 'dob',
                'birth_place_province_text', 'birth_place_old_name', 'birth_place_detail', 'birth_place_ward',
                'ethnic_group', 'ethnic_group_other', 'religion', 'religion_other', 'religious_title',
                'hometown_detail', 'hometown_ward',
                'current_address_number', 'current_address_street', 'current_address', 'current_ward',
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
    list_display  = ['id', 'profile', 'reviewer', 'action', 'from_status', 'to_status', 'created_at']
    list_filter   = ['action']
    search_fields = ['profile__full_name', 'reviewer__full_name']
    readonly_fields = ['created_at']
    raw_id_fields   = ['profile', 'reviewer']

    def has_change_permission(self, request, obj=None):
        return False
