from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


class Role(models.Model):
    code        = models.CharField(max_length=40, unique=True)
    name        = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'roles'
        verbose_name = 'Vai trò'
        verbose_name_plural = 'Vai trò'

    def __str__(self):
        return self.name

    # Helper properties
    @property
    def is_admin(self):
        return self.code == 'admin'

    @property
    def is_officer(self):
        return self.code == 'can_bo_bxd'

    @property
    def is_applicant(self):
        return self.code == 'quan_chung'


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('Số điện thoại là bắt buộc')
        user = self.model(phone=phone, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('status', 'active')
        admin_role, _ = Role.objects.get_or_create(
            code='admin', defaults={'name': 'Quản trị hệ thống'}
        )
        extra_fields.setdefault('role', admin_role)
        return self.create_user(phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class Status(models.TextChoices):
        ACTIVE   = 'active',   'Hoạt động'
        INACTIVE = 'inactive', 'Không hoạt động'
        LOCKED   = 'locked',   'Bị khóa'
        PENDING  = 'pending',  'Chờ kích hoạt'

    role             = models.ForeignKey(Role, on_delete=models.PROTECT, related_name='users', db_column='role_id')
    full_name        = models.CharField(max_length=255)
    phone            = models.CharField(max_length=20, unique=True)
    email            = models.EmailField(max_length=255, null=True, blank=True)
    cccd             = models.CharField(max_length=12, unique=True, null=True, blank=True)
    zalo_uid         = models.CharField(max_length=100, null=True, blank=True)
    chi_bo           = models.CharField(max_length=255, null=True, blank=True, verbose_name='Chi bộ')
    dang_bo          = models.CharField(max_length=255, null=True, blank=True, verbose_name='Đảng bộ')

    otp_code         = models.CharField(max_length=8, null=True, blank=True)
    otp_expires_at   = models.DateTimeField(null=True, blank=True)

    avatar_path      = models.CharField(max_length=500, null=True, blank=True)
    status           = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    email_verified   = models.BooleanField(default=False)
    phone_verified   = models.BooleanField(default=False)

    last_login_at    = models.DateTimeField(null=True, blank=True)
    login_attempts   = models.PositiveSmallIntegerField(default=0)
    locked_until     = models.DateTimeField(null=True, blank=True)

    created_by       = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                          related_name='created_users', db_column='created_by')
    updated_by       = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                          related_name='updated_users', db_column='updated_by')
    deleted_at       = models.DateTimeField(null=True, blank=True)

    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    # Django required fields
    is_staff         = models.BooleanField(default=False)

    USERNAME_FIELD   = 'phone'
    REQUIRED_FIELDS  = ['full_name']

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'Người dùng'
        verbose_name_plural = 'Người dùng'
        indexes = [
            models.Index(fields=['role']),
            models.Index(fields=['status']),
            models.Index(fields=['full_name']),
            models.Index(fields=['deleted_at']),
            models.Index(fields=['zalo_uid']),
        ]

    def __str__(self):
        return f'{self.full_name} ({self.phone})'

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.status = self.Status.INACTIVE
        self.save(update_fields=['deleted_at', 'status'])

    @property
    def is_active(self):
        return self.status == self.Status.ACTIVE and self.deleted_at is None

    @property
    def role_code(self):
        return self.role.code if self.role_id else None

    def increment_login_attempts(self):
        self.login_attempts += 1
        if self.login_attempts >= 5:
            self.status = self.Status.LOCKED
            self.locked_until = timezone.now() + timezone.timedelta(minutes=30)
        self.save(update_fields=['login_attempts', 'status', 'locked_until'])

    def reset_login_attempts(self):
        self.login_attempts = 0
        self.last_login_at = timezone.now()
        self.save(update_fields=['login_attempts', 'last_login_at'])


class OfficerPermission(models.Model):
    """Granular feature permissions for admin/can_bo_bxd users.
    Managed by superuser via the super-admin interface.
    """
    user                   = models.OneToOneField(User, on_delete=models.CASCADE,
                                                  related_name='officer_permission')
    can_create_accounts    = models.BooleanField(default=False, verbose_name='Cấp tài khoản quần chúng')
    can_review_profiles    = models.BooleanField(default=False, verbose_name='Xem & trả lại hồ sơ')
    can_approve_profiles   = models.BooleanField(default=False, verbose_name='Phê duyệt hồ sơ')
    can_export_word        = models.BooleanField(default=False, verbose_name='Xuất file Word')
    can_send_notifications = models.BooleanField(default=False, verbose_name='Gửi thông báo')
    can_view_reports       = models.BooleanField(default=False, verbose_name='Xem báo cáo')
    created_at             = models.DateTimeField(auto_now_add=True)
    updated_at             = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'officer_permissions'
        verbose_name = 'Phân quyền cán bộ'
        verbose_name_plural = 'Phân quyền cán bộ'

    def __str__(self):
        return f'Permissions for {self.user}'

    def as_dict(self):
        return {
            'can_create_accounts':    self.can_create_accounts,
            'can_review_profiles':    self.can_review_profiles,
            'can_approve_profiles':   self.can_approve_profiles,
            'can_export_word':        self.can_export_word,
            'can_send_notifications': self.can_send_notifications,
            'can_view_reports':       self.can_view_reports,
        }


class Officer(User):
    """Proxy model for managing officers via Django admin."""
    class Meta:
        proxy = True
        verbose_name = 'Cán bộ Đảng'
        verbose_name_plural = 'Quản lý Cán bộ Đảng'


def get_officer_permissions(user) -> dict:
    """Return effective feature permissions for a user."""
    if user.is_superuser:
        return {k: True for k in [
            'can_create_accounts', 'can_review_profiles', 'can_approve_profiles',
            'can_export_word', 'can_send_notifications', 'can_view_reports',
        ]}
    try:
        return user.officer_permission.as_dict()
    except OfficerPermission.DoesNotExist:
        # Legacy admin without explicit record → full access
        if getattr(user, 'role_code', None) == 'admin':
            return {k: True for k in [
                'can_create_accounts', 'can_review_profiles', 'can_approve_profiles',
                'can_export_word', 'can_send_notifications', 'can_view_reports',
            ]}
        return {k: False for k in [
            'can_create_accounts', 'can_review_profiles', 'can_approve_profiles',
            'can_export_word', 'can_send_notifications', 'can_view_reports',
        ]}


class LoginHistory(models.Model):
    class LoginStatus(models.TextChoices):
        SUCCESS = 'success', 'Thành công'
        FAILED  = 'failed',  'Thất bại'
        LOCKED  = 'locked',  'Bị khóa'

    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_history')
    ip_address  = models.GenericIPAddressField(null=True, blank=True)
    user_agent  = models.CharField(max_length=500, null=True, blank=True)
    status      = models.CharField(max_length=20, choices=LoginStatus.choices, default=LoginStatus.SUCCESS)
    fail_reason = models.CharField(max_length=255, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'login_history'
        verbose_name = 'Lịch sử đăng nhập'
        verbose_name_plural = 'Lịch sử đăng nhập'
        indexes = [
            models.Index(fields=['user', 'created_at']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return f'{self.user} – {self.status} – {self.created_at}'


class PasswordReset(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_resets')
    token       = models.CharField(max_length=255)
    expires_at  = models.DateTimeField()
    used_at     = models.DateTimeField(null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'password_resets'
        verbose_name = 'Đặt lại mật khẩu'
        verbose_name_plural = 'Đặt lại mật khẩu'

    def __str__(self):
        return f'PasswordReset for {self.user}'

    @property
    def is_valid(self):
        from django.utils import timezone
        return self.used_at is None and self.expires_at > timezone.now()


class AccountRequest(models.Model):
    class Status(models.TextChoices):
        PENDING   = 'pending',   'Chờ xử lý'
        CREATED   = 'created',   'Đã tạo'
        FAILED    = 'failed',    'Thất bại'
        CANCELLED = 'cancelled', 'Đã hủy'

    requested_by      = models.ForeignKey(User, on_delete=models.PROTECT, related_name='account_requests')
    full_name         = models.CharField(max_length=255)
    cccd              = models.CharField(max_length=12)
    dob               = models.DateField()
    phone             = models.CharField(max_length=20)
    email             = models.EmailField(null=True, blank=True)
    chi_bo            = models.CharField(max_length=255, null=True, blank=True, verbose_name='Chi bộ')
    dang_bo           = models.CharField(max_length=255, null=True, blank=True, verbose_name='Đảng bộ')
    officer_in_charge = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL,
                                          related_name='assigned_requests', db_column='officer_in_charge')
    notify_sms        = models.BooleanField(default=True)
    notify_email      = models.BooleanField(default=False)
    notify_zalo       = models.BooleanField(default=False)
    status            = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_user      = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL,
                                          related_name='created_from_request', db_column='user_id')
    fail_reason       = models.CharField(max_length=500, null=True, blank=True)
    notes             = models.TextField(null=True, blank=True)
    created_at        = models.DateTimeField(auto_now_add=True)
    processed_at      = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'account_requests'
        verbose_name = 'Yêu cầu cấp tài khoản'
        verbose_name_plural = 'Yêu cầu cấp tài khoản'
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['cccd']),
        ]

    def __str__(self):
        return f'AccountRequest: {self.full_name} – {self.status}'
