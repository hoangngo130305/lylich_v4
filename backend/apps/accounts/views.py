import secrets
import string
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from django.db import transaction
from rest_framework import generics, status, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from .models import User, Role, PasswordReset, AccountRequest, LoginHistory
from .serializers import (
    CustomTokenObtainPairSerializer, RegisterSerializer, UserDetailSerializer,
    ChangePasswordSerializer, ResetPasswordRequestSerializer,
    ResetPasswordConfirmSerializer, AccountRequestSerializer,
    AccountRequestCreateSerializer, LoginHistorySerializer, UserPublicSerializer,
)
from .permissions import IsOfficer, IsAdmin, IsOfficerOrApplicant
from apps.auditlogs.utils import log_activity


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(
                {'success': False, 'error': str(e)},
                status=status.HTTP_401_UNAUTHORIZED
            )
        data = serializer.validated_data
        return Response({'success': True, 'data': data}, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            log_activity(request.user, 'logout', description='Đăng xuất')
        except TokenError:
            pass
        return Response({'success': True, 'message': 'Đã đăng xuất.'})


class TokenRefreshViewCustom(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            return Response({'success': True, 'data': response.data})
        return response


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {'success': True, 'data': UserPublicSerializer(user).data},
            status=status.HTTP_201_CREATED
        )


class MeView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save(update_fields=['password'])
        log_activity(request.user, 'change_password', description='Đổi mật khẩu')
        return Response({'success': True, 'message': 'Đổi mật khẩu thành công.'})


class PasswordResetRequestView(generics.GenericAPIView):
    serializer_class = ResetPasswordRequestSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        token = secrets.token_urlsafe(32)
        PasswordReset.objects.create(
            user=user, token=token,
            expires_at=timezone.now() + timezone.timedelta(hours=2)
        )
        # In production: send SMS/email with token
        return Response({'success': True, 'message': 'OTP đặt lại mật khẩu đã được gửi.'})


class PasswordResetConfirmView(generics.GenericAPIView):
    serializer_class = ResetPasswordConfirmSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            reset = PasswordReset.objects.get(token=serializer.validated_data['token'])
        except PasswordReset.DoesNotExist:
            return Response({'success': False, 'error': 'Token không hợp lệ.'}, status=400)
        if not reset.is_valid:
            return Response({'success': False, 'error': 'Token đã hết hạn.'}, status=400)
        reset.user.set_password(serializer.validated_data['new_password'])
        reset.user.save(update_fields=['password'])
        reset.used_at = timezone.now()
        reset.save(update_fields=['used_at'])
        return Response({'success': True, 'message': 'Đặt lại mật khẩu thành công.'})


# ── Officer: User management ─────────────────────────────────────────────────

class UserListView(generics.ListCreateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsOfficer]
    filterset_fields  = ['role__code', 'status']
    search_fields     = ['full_name', 'phone', 'cccd']
    ordering_fields   = ['full_name', 'created_at', 'last_login_at']

    def get_queryset(self):
        qs = User.objects.select_related('role').prefetch_related('profile').filter(
            deleted_at__isnull=True
        )
        # Support ordering=-date_joined as alias for -created_at (frontend compat)
        ordering = self.request.query_params.get('ordering', '-created_at')
        if 'date_joined' in ordering:
            ordering = ordering.replace('date_joined', 'created_at')
        return qs.order_by(ordering)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsOfficer]

    def get_queryset(self):
        return User.objects.select_related('role').filter(deleted_at__isnull=True)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.soft_delete()
        log_activity(request.user, 'user_delete', target_model='User', target_id=user.id)
        return Response({'success': True, 'message': 'Tài khoản đã bị vô hiệu hóa.'})


class AccountRequestListView(generics.ListCreateAPIView):
    permission_classes = [IsOfficer]
    filterset_fields  = ['status']
    search_fields     = ['full_name', 'phone', 'cccd']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AccountRequestCreateSerializer
        return AccountRequestSerializer

    def get_queryset(self):
        return AccountRequest.objects.select_related(
            'requested_by', 'officer_in_charge', 'created_user'
        ).order_by('-created_at')

    def _generate_initial_password(self, length=12):
        alphabet = string.ascii_letters + string.digits + '@#$%'
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    def _send_account_email(self, request_obj, raw_password):
        if not request_obj.email:
            raise ValueError('Thiếu email người nhận để gửi thông tin tài khoản.')
        if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
            raise ValueError('SMTP chưa được cấu hình đầy đủ (thiếu EMAIL_HOST_USER/EMAIL_HOST_PASSWORD).')

        subject = 'Tài khoản kê khai lý lịch đã được cấp'
        body = (
            f"Kính gửi {request_obj.full_name},\n\n"
            "Tài khoản kê khai lý lịch của bạn đã được tạo thành công.\n"
            f"Số điện thoại đăng nhập: {request_obj.phone}\n"
            f"Mật khẩu khởi tạo: {raw_password}\n\n"
            "Vui lòng đăng nhập và đổi mật khẩu ngay sau lần đăng nhập đầu tiên.\n"
            "Trân trọng."
        )
        from_email = settings.DEFAULT_FROM_EMAIL or settings.EMAIL_HOST_USER
        send_mail(
            subject,
            body,
            from_email,
            [request_obj.email],
            fail_silently=False,
        )

    @transaction.atomic
    def perform_create(self, serializer):
        req = serializer.save()
        try:
            role, _ = Role.objects.get_or_create(
                code='quan_chung',
                defaults={'name': 'Quần chúng xin vào Đảng'}
            )
            initial_password = self._generate_initial_password()
            user = User.objects.create_user(
                phone=req.phone,
                password=initial_password,
                full_name=req.full_name,
                cccd=req.cccd,
                email=req.email,
                role=role,
                status=User.Status.ACTIVE,
                phone_verified=True,
                created_by=self.request.user,
            )

            self._send_account_email(req, initial_password)

            req.created_user = user
            req.status = AccountRequest.Status.CREATED
            req.fail_reason = None
            req.processed_at = timezone.now()
            req.save(update_fields=['created_user', 'status', 'fail_reason', 'processed_at'])

            log_activity(
                self.request.user, 'account_create',
                target_model='User', target_id=user.id,
                description=f'Tạo tài khoản cho {req.full_name}'
            )
        except Exception as e:
            req.status = AccountRequest.Status.FAILED
            req.fail_reason = str(e)
            req.processed_at = timezone.now()
            req.save(update_fields=['status', 'fail_reason', 'processed_at'])
            raise ValidationError({'detail': f'Tạo tài khoản thất bại: {e}'})


class AccountRequestDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = AccountRequestSerializer
    permission_classes = [IsOfficer]
    queryset = AccountRequest.objects.all()


class LoginHistoryListView(generics.ListAPIView):
    serializer_class = LoginHistorySerializer
    permission_classes = [IsOfficer]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        qs = LoginHistory.objects.select_related('user')
        if user_id:
            qs = qs.filter(user_id=user_id)
        return qs.order_by('-created_at')


@api_view(['POST'])
@permission_classes([IsOfficer])
def toggle_user_status(request, pk):
    try:
        user = User.objects.get(pk=pk, deleted_at__isnull=True)
    except User.DoesNotExist:
        return Response({'success': False, 'error': 'Không tìm thấy người dùng.'}, status=404)
    new_status = request.data.get('status', User.Status.ACTIVE)
    if new_status not in [c[0] for c in User.Status.choices]:
        return Response({'success': False, 'error': 'Trạng thái không hợp lệ.'}, status=400)
    user.status = new_status
    user.save(update_fields=['status'])
    log_activity(
        request.user, 'user_status_change',
        target_model='User', target_id=user.id,
        description=f'Đổi trạng thái → {new_status}'
    )
    return Response({'success': True, 'data': UserDetailSerializer(user).data})
