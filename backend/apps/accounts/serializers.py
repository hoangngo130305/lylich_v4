from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Role, LoginHistory, AccountRequest, OfficerPermission, get_officer_permissions


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'code', 'name']


class OfficerPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficerPermission
        fields = [
            'can_create_accounts', 'can_review_profiles', 'can_approve_profiles',
            'can_export_word', 'can_send_notifications', 'can_view_reports',
        ]


class UserPublicSerializer(serializers.ModelSerializer):
    role        = RoleSerializer(read_only=True)
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'full_name', 'phone', 'email', 'role', 'status',
                  'avatar_path', 'last_login_at', 'created_at', 'is_superuser', 'permissions',
                  'chi_bo', 'dang_bo']

    def get_permissions(self, obj):
        return get_officer_permissions(obj)


class UserDetailSerializer(serializers.ModelSerializer):
    role        = RoleSerializer(read_only=True)
    role_id     = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), source='role', write_only=True, required=False
    )
    profile_status     = serializers.SerializerMethodField()
    officer_permission = OfficerPermissionSerializer(read_only=True)
    permissions        = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'full_name', 'phone', 'email', 'cccd', 'zalo_uid',
            'chi_bo', 'dang_bo',
            'role', 'role_id', 'status', 'avatar_path',
            'email_verified', 'phone_verified',
            'last_login_at', 'login_attempts', 'locked_until',
            'created_by_id', 'created_at', 'updated_at',
            'profile_status', 'is_superuser',
            'officer_permission', 'permissions',
        ]
        read_only_fields = ['id', 'last_login_at', 'login_attempts', 'created_at', 'updated_at']

    def get_profile_status(self, obj):
        try:
            return obj.profile.status
        except Exception:
            return None

    def get_permissions(self, obj):
        return get_officer_permissions(obj)


class OfficerCreateSerializer(serializers.Serializer):
    """Used by superadmin to create new officer accounts."""
    full_name  = serializers.CharField(max_length=255)
    phone      = serializers.CharField(max_length=20)
    email      = serializers.EmailField(required=False, allow_blank=True)
    password   = serializers.CharField(min_length=8, write_only=True)
    role_code  = serializers.ChoiceField(choices=['admin', 'can_bo_bxd'])
    # permissions
    can_create_accounts    = serializers.BooleanField(default=False)
    can_review_profiles    = serializers.BooleanField(default=False)
    can_approve_profiles   = serializers.BooleanField(default=False)
    can_export_word        = serializers.BooleanField(default=False)
    can_send_notifications = serializers.BooleanField(default=False)
    can_view_reports       = serializers.BooleanField(default=False)

    def validate_phone(self, value):
        if User.objects.filter(phone=value).exists():
            raise serializers.ValidationError('Số điện thoại đã được sử dụng.')
        return value


class OfficerUpdateSerializer(serializers.Serializer):
    full_name  = serializers.CharField(max_length=255, required=False)
    email      = serializers.EmailField(required=False, allow_blank=True)
    status     = serializers.ChoiceField(choices=User.Status.choices, required=False)
    role_code  = serializers.ChoiceField(choices=['admin', 'can_bo_bxd'], required=False)


class RegisterSerializer(serializers.ModelSerializer):
    password  = serializers.CharField(write_only=True, min_length=8)
    role_code = serializers.CharField(default='quan_chung', write_only=True)

    class Meta:
        model = User
        fields = ['full_name', 'phone', 'email', 'cccd', 'password', 'role_code']

    def validate_phone(self, value):
        if User.objects.filter(phone=value).exists():
            raise serializers.ValidationError('Số điện thoại đã được đăng ký.')
        return value

    def validate_cccd(self, value):
        if value and User.objects.filter(cccd=value).exists():
            raise serializers.ValidationError('CCCD đã được đăng ký.')
        return value

    def create(self, validated_data):
        role_code = validated_data.pop('role_code', 'quan_chung')
        password  = validated_data.pop('password')
        role, _   = Role.objects.get_or_create(code=role_code, defaults={'name': role_code})
        user      = User(role=role, **validated_data)
        user.set_password(password)
        user.status = User.Status.PENDING
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=8)

    def validate(self, data):
        user = self.context['request'].user
        if not user.check_password(data['old_password']):
            raise serializers.ValidationError({'old_password': 'Mật khẩu cũ không đúng.'})
        return data


class ResetPasswordRequestSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)

    def validate_phone(self, value):
        try:
            self.user = User.objects.get(phone=value, deleted_at__isnull=True)
        except User.DoesNotExist:
            raise serializers.ValidationError('Số điện thoại không tồn tại.')
        return value


class ResetPasswordConfirmSerializer(serializers.Serializer):
    token        = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=8)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'phone'

    def validate(self, attrs):
        phone    = attrs.get('phone', '')
        password = attrs.get('password', '')

        try:
            user = User.objects.select_related('role').get(phone=phone, deleted_at__isnull=True)
        except User.DoesNotExist:
            raise serializers.ValidationError({'detail': 'Tài khoản không tồn tại.'})

        if user.status == User.Status.LOCKED:
            if user.locked_until and user.locked_until > timezone.now():
                raise serializers.ValidationError({
                    'detail': f'Tài khoản bị khóa đến {user.locked_until.strftime("%H:%M %d/%m/%Y")}.'
                })
            else:
                user.status = User.Status.ACTIVE
                user.login_attempts = 0
                user.save(update_fields=['status', 'login_attempts'])

        if not user.is_active:
            raise serializers.ValidationError({'detail': 'Tài khoản chưa được kích hoạt.'})

        if not user.check_password(password):
            user.increment_login_attempts()
            LoginHistory.objects.create(
                user=user, status=LoginHistory.LoginStatus.FAILED,
                fail_reason='Sai mật khẩu'
            )
            raise serializers.ValidationError({'detail': 'Mật khẩu không đúng.'})

        user.reset_login_attempts()
        LoginHistory.objects.create(user=user, status=LoginHistory.LoginStatus.SUCCESS)

        refresh = RefreshToken.for_user(user)
        refresh['role']         = user.role.code
        refresh['full_name']    = user.full_name
        refresh['is_superuser'] = user.is_superuser
        refresh['permissions']  = get_officer_permissions(user)

        return {
            'refresh': str(refresh),
            'access':  str(refresh.access_token),
            'user':    UserPublicSerializer(user).data,
        }


class SuperAdminLoginSerializer(CustomTokenObtainPairSerializer):
    """Like regular login but only allows is_superuser users."""

    def validate(self, attrs):
        data = super().validate(attrs)
        user_data = data['user']
        if not user_data.get('is_superuser'):
            raise serializers.ValidationError({'detail': 'Tài khoản này không có quyền truy cập trang quản trị cấp cao.'})
        return data


class AccountRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountRequest
        fields = [
            'id', 'full_name', 'cccd', 'dob', 'phone', 'email',
            'chi_bo', 'dang_bo',
            'officer_in_charge', 'notify_sms', 'notify_email', 'notify_zalo',
            'status', 'fail_reason', 'notes', 'created_at', 'processed_at',
        ]
        read_only_fields = ['id', 'status', 'created_at', 'processed_at']

    def create(self, validated_data):
        validated_data['requested_by'] = self.context['request'].user
        return super().create(validated_data)


class AccountRequestCreateSerializer(serializers.ModelSerializer):
    """Used by officers to create accounts for applicants."""

    class Meta:
        model = AccountRequest
        fields = ['full_name', 'cccd', 'dob', 'phone', 'email',
                  'chi_bo', 'dang_bo',
                  'officer_in_charge', 'notes']

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError('Email Gmail là bắt buộc để gửi thông tin đăng nhập.')
        return value

    def create(self, validated_data):
        validated_data['requested_by'] = self.context['request'].user
        validated_data['notify_email'] = True
        validated_data['notify_sms'] = False
        validated_data['notify_zalo'] = False
        req = super().create(validated_data)
        return req


class LoginHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginHistory
        fields = ['id', 'status', 'fail_reason', 'ip_address', 'created_at']
