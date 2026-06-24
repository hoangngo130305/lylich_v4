from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'
    verbose_name = 'Tài khoản & Phân quyền'

    def ready(self):
        # Patch unfold's _flatten_context to handle Context objects in dicts.
        # Django admin's submit_row returns a Context (not a dict), which ends up
        # in context.dicts via context.new(ctx). unfold's safe path only covers
        # Django < 5, but the bug also affects Django 5.x. See Django #35417.
        try:
            from django.template.context import BaseContext
            from unfold.templatetags import unfold as unfold_tags

            def _safe_flatten_context(context):
                flat = {}
                for d in context.dicts:
                    if isinstance(d, BaseContext):
                        flat.update(_safe_flatten_context(d))
                    elif isinstance(d, dict):
                        flat.update(d)
                return flat

            unfold_tags._flatten_context = _safe_flatten_context
        except Exception:
            pass
