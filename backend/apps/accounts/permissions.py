from rest_framework.permissions import BasePermission


def _has_officer_perm(user, flag: str) -> bool:
    """True for superusers and 'admin' role; for 'can_bo_bxd' checks the OfficerPermission flag."""
    if not (user and user.is_authenticated):
        return False
    if user.is_superuser or getattr(user, 'role_code', None) == 'admin':
        return True
    if getattr(user, 'role_code', None) != 'can_bo_bxd':
        return False
    try:
        return bool(getattr(user.officer_permission, flag, False))
    except Exception:
        return False


class IsSuperAdmin(BasePermission):
    """Only Django superusers (createsuperuser) can access."""
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated
            and request.user.is_superuser
        )


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated
            and request.user.role_code == 'admin'
        )


class IsOfficer(BasePermission):
    """Can Bo Ban Xay Dung Dang"""
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated
            and request.user.role_code in ('admin', 'can_bo_bxd')
        )


class IsApplicant(BasePermission):
    """Quan Chung"""
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated
            and request.user.role_code == 'quan_chung'
        )


class IsOfficerOrApplicant(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated
            and request.user.role_code in ('admin', 'can_bo_bxd', 'quan_chung')
        )


class IsOwnerOrOfficer(BasePermission):
    """Object-level: applicant can only access own profile; officer can access all."""
    def has_object_permission(self, request, view, obj):
        if request.user.role_code in ('admin', 'can_bo_bxd'):
            return True
        if hasattr(obj, 'user_id'):
            return obj.user_id == request.user.id
        if hasattr(obj, 'profile') and hasattr(obj.profile, 'user_id'):
            return obj.profile.user_id == request.user.id
        return False


# ── Granular OfficerPermission enforcement ────────────────────────────────────

class CanCreateAccounts(BasePermission):
    def has_permission(self, request, view):
        return _has_officer_perm(request.user, 'can_create_accounts')


class CanReviewProfiles(BasePermission):
    def has_permission(self, request, view):
        return _has_officer_perm(request.user, 'can_review_profiles')


class CanApproveProfiles(BasePermission):
    def has_permission(self, request, view):
        return _has_officer_perm(request.user, 'can_approve_profiles')


class CanExportWord(BasePermission):
    def has_permission(self, request, view):
        return _has_officer_perm(request.user, 'can_export_word')


class CanSendNotifications(BasePermission):
    def has_permission(self, request, view):
        return _has_officer_perm(request.user, 'can_send_notifications')


class CanViewReports(BasePermission):
    def has_permission(self, request, view):
        return _has_officer_perm(request.user, 'can_view_reports')

