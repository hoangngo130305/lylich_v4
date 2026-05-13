from .models import ActivityLog


class RequestLogMiddleware:
    """Log every authenticated API request to activity_logs."""

    SKIP_PATHS = {'/api/v1/auth/token/refresh/', '/api/v1/notifications/stats/'}

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if (
            request.path.startswith('/api/')
            and request.path not in self.SKIP_PATHS
            and request.method in ('POST', 'PUT', 'PATCH', 'DELETE')
            and hasattr(request, 'user')
            and request.user.is_authenticated
        ):
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            ip = x_forwarded_for.split(',')[0].strip() if x_forwarded_for else request.META.get('REMOTE_ADDR')

            ActivityLog.objects.create(
                user=request.user,
                action=self._action_from_method(request.method),
                target_model=None,
                target_id=None,
                description=f'{request.method} {request.path}',
                ip_address=ip,
                user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
            )

        return response

    @staticmethod
    def _action_from_method(method):
        return {
            'POST':   ActivityLog.Action.CREATE,
            'PUT':    ActivityLog.Action.UPDATE,
            'PATCH':  ActivityLog.Action.UPDATE,
            'DELETE': ActivityLog.Action.DELETE,
        }.get(method, ActivityLog.Action.VIEW)
