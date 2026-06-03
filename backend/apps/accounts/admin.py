from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.utils.html import format_html
from unfold.admin import ModelAdmin, StackedInline
from .models import User, Role, LoginHistory, PasswordReset, AccountRequest, OfficerPermission, Officer


class UserAddForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('phone', 'full_name', 'role', 'status')

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1', '')
        if not password1:
            raise ValidationError('Mật khẩu không được để trống.')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1', '')
        password2 = self.cleaned_data.get('password2', '')
        if not password2:
            raise ValidationError('Vui lòng xác nhận mật khẩu.')
        if password1 and password1 != password2:
            raise ValidationError('Hai mật khẩu không khớp.')
        return password2


@admin.register(Role)
class RoleAdmin(ModelAdmin):
    list_display  = ['id', 'code', 'name', 'created_at']
    search_fields = ['code', 'name']
    readonly_fields = ['created_at']


@admin.register(User)
class UserAdmin(ModelAdmin, BaseUserAdmin):
    add_form      = UserAddForm
    list_display  = ['id', 'full_name', 'phone', 'role', 'status', 'phone_verified', 'created_at']
    list_filter   = ['role', 'status', 'phone_verified', 'email_verified']
    search_fields = ['full_name', 'phone', 'email', 'cccd']
    readonly_fields = ['last_login', 'last_login_at', 'created_at', 'updated_at', 'deleted_at']
    ordering      = ['-created_at']
    fieldsets     = (
        ('Thông tin cơ bản', {
            'fields': ('full_name', 'phone', 'email', 'cccd', 'zalo_uid', 'role')
        }),
        ('Trạng thái', {
            'fields': ('status', 'phone_verified', 'email_verified',
                       'login_attempts', 'locked_until', 'deleted_at')
        }),
        ('Bảo mật', {
            'fields': ('password',),
            'classes': ('collapse',),
        }),
        ('Thời gian', {
            'fields': ('last_login_at', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'phone', 'role', 'password1', 'password2', 'status'),
        }),
    )
    filter_horizontal = []
    list_display_links = ['id', 'full_name']

    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except IntegrityError:
            from django.contrib import messages
            messages.error(request, f'Số điện thoại "{obj.phone}" đã được đăng ký trong hệ thống. Vui lòng dùng số khác.')

# ── Officer proxy model ───────────────────────────────────────────────────────
# Officer model is defined in models.py

class OfficerPermissionInline(StackedInline):
    model = OfficerPermission
    can_delete = False
    min_num = 1
    extra = 0
    verbose_name_plural = 'Phân quyền chức năng'
    fields = (
        ('can_create_accounts', 'can_review_profiles', 'can_approve_profiles'),
        ('can_export_word', 'can_send_notifications', 'can_view_reports'),
    )

    def has_delete_permission(self, request, obj=None):
        return False


def _bool_icon(val):
    icon = '✓' if val else '✗'
    color = '#16a34a' if val else '#dc2626'
    return format_html('<span style="color:{}; font-weight:bold">{}</span>', color, icon)


@admin.register(Officer)
class OfficerAdmin(ModelAdmin, BaseUserAdmin):
    list_display  = [
        'id', 'full_name', 'phone', 'role', 'status',
        'perm_create_accounts', 'perm_review_profiles', 'perm_approve_profiles',
        'perm_export_word', 'perm_send_notifications', 'perm_view_reports',
        'created_at',
    ]
    list_filter   = ['role', 'status']
    search_fields = ['full_name', 'phone', 'email']
    readonly_fields = ['last_login', 'last_login_at', 'created_at', 'updated_at', 'deleted_at']
    ordering      = ['full_name']
    inlines       = [OfficerPermissionInline]
    filter_horizontal = []
    list_display_links = ['id', 'full_name']

    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('full_name', 'phone', 'email', 'role')
        }),
        ('Trạng thái', {
            'fields': ('status', 'is_staff', 'is_superuser', 'deleted_at')
        }),
        ('Bảo mật', {
            'fields': ('password',),
            'classes': ('collapse',),
        }),
        ('Thời gian', {
            'fields': ('last_login_at', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'phone', 'email', 'role', 'password1', 'password2', 'status'),
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).filter(
            role__code__in=['admin', 'can_bo_bxd'],
            deleted_at__isnull=True,
        )

    def _perm(self, obj, field):
        try:
            return _bool_icon(getattr(obj.officer_permission, field))
        except OfficerPermission.DoesNotExist:
            return _bool_icon(obj.is_superuser or obj.role.code == 'admin')

    def perm_create_accounts(self, obj):
        return self._perm(obj, 'can_create_accounts')
    perm_create_accounts.short_description = 'Cấp TK'
    perm_create_accounts.allow_tags = True

    def perm_review_profiles(self, obj):
        return self._perm(obj, 'can_review_profiles')
    perm_review_profiles.short_description = 'Xem HS'
    perm_review_profiles.allow_tags = True

    def perm_approve_profiles(self, obj):
        return self._perm(obj, 'can_approve_profiles')
    perm_approve_profiles.short_description = 'Duyệt HS'
    perm_approve_profiles.allow_tags = True

    def perm_export_word(self, obj):
        return self._perm(obj, 'can_export_word')
    perm_export_word.short_description = 'Xuất Word'
    perm_export_word.allow_tags = True

    def perm_send_notifications(self, obj):
        return self._perm(obj, 'can_send_notifications')
    perm_send_notifications.short_description = 'Thông báo'
    perm_send_notifications.allow_tags = True

    def perm_view_reports(self, obj):
        return self._perm(obj, 'can_view_reports')
    perm_view_reports.short_description = 'Báo cáo'
    perm_view_reports.allow_tags = True

    def save_model(self, request, obj, form, change):
        if obj.role and obj.role.code == 'admin':
            obj.is_staff = True
        super().save_model(request, obj, form, change)


@admin.register(LoginHistory)
class LoginHistoryAdmin(ModelAdmin):
    list_display  = ['id', 'user', 'status', 'ip_address', 'fail_reason', 'created_at']
    list_filter   = ['status']
    search_fields = ['user__full_name', 'user__phone', 'ip_address']
    readonly_fields = ['user', 'status', 'ip_address', 'user_agent', 'fail_reason', 'created_at']
    date_hierarchy = 'created_at'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(AccountRequest)
class AccountRequestAdmin(ModelAdmin):
    list_display  = ['id', 'full_name', 'phone', 'cccd', 'status', 'requested_by', 'created_at']
    list_filter   = ['status', 'notify_sms', 'notify_zalo']
    search_fields = ['full_name', 'phone', 'cccd']
    readonly_fields = ['created_at', 'processed_at', 'created_user']
    raw_id_fields   = ['requested_by', 'officer_in_charge', 'created_user']
