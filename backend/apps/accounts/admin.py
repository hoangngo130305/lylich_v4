from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.admin import ModelAdmin
from .models import User, Role, LoginHistory, PasswordReset, AccountRequest


@admin.register(Role)
class RoleAdmin(ModelAdmin):
    list_display  = ['id', 'code', 'name', 'created_at']
    search_fields = ['code', 'name']
    readonly_fields = ['created_at']


@admin.register(User)
class UserAdmin(ModelAdmin, BaseUserAdmin):
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
    # BaseUserAdmin compat
    filter_horizontal = []
    list_display_links = ['id', 'full_name']


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
