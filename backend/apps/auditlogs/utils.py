from .models import ActivityLog


def log_activity(user, action, target_model=None, target_id=None, description=None,
                 request=None, extra=None):
    ip_address = None
    user_agent = None

    if request is not None:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(',')[0].strip()
        else:
            ip_address = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT', '')[:500]

    ActivityLog.objects.create(
        user=user if (user and user.is_authenticated) else None,
        action=action,
        target_model=target_model,
        target_id=target_id,
        description=description,
        ip_address=ip_address,
        user_agent=user_agent,
        extra=extra,
    )
