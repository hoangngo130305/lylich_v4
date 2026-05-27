from rest_framework.permissions import BasePermission


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
