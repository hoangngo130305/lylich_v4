#!/usr/bin/env python
import os
import sys

# On Windows, the console's default codepage (cp1252) can't encode many
# Vietnamese characters (e.g. "Đ"), so any print() of Vietnamese text
# crashes with UnicodeEncodeError instead of just printing — which turns
# innocuous debug logging (e.g. in the DOCX export view) into a 500 error.
# Force UTF-8 stdout/stderr so logging can never crash a request.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
