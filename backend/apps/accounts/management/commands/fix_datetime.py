"""
python manage.py fix_datetime           — scan and fix invalid datetime values
python manage.py fix_datetime --dry-run — report only, no writes

What it fixes
─────────────
MySQL can store '0000-00-00 00:00:00' when a NOT NULL datetime is inserted
without a value (old sql_mode without STRICT).  Django with USE_TZ=True
cannot convert those rows and raises:
  ValueError: Database returned an invalid datetime value.

This command:
  1. Scans every DateTimeField in all installed models.
  2. Uses a raw SQL query to detect '0000-00-00 00:00:00' values
     (those never appear in a Django QuerySet — Django crashes before then).
  3. NULLs them out (if nullable) or sets them to a safe sentinel
     (e.g. 2000-01-01 00:00:00) if NOT NULL.
"""
from django.core.management.base import BaseCommand
from django.apps import apps
from django.db import connection, models as django_models


_SENTINEL = '2000-01-01 00:00:00'


class Command(BaseCommand):
    help = 'Scan and repair invalid (0000-00-00) datetime values in all tables'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true',
                            help='Only report; do not fix anything')

    def handle(self, *args, **options):
        dry = options['dry_run']
        total_fixed = 0

        for model in apps.get_models():
            table = model._meta.db_table
            dt_fields = [
                f for f in model._meta.get_fields()
                if isinstance(f, (django_models.DateTimeField,))
                   and not f.many_to_many
                   and not f.one_to_many
                   and hasattr(f, 'column')
            ]
            if not dt_fields:
                continue

            for field in dt_fields:
                col     = field.column
                nullable = field.null

                check_sql = (
                    f"SELECT COUNT(*) FROM `{table}` "
                    f"WHERE `{col}` = '0000-00-00 00:00:00'"
                )
                try:
                    with connection.cursor() as cur:
                        cur.execute(check_sql)
                        count = cur.fetchone()[0]
                except Exception as exc:
                    self.stderr.write(f'  SKIP {table}.{col}: {exc}')
                    continue

                if count == 0:
                    continue

                self.stdout.write(
                    f'  FOUND {count} bad row(s): `{table}`.`{col}`'
                )

                if dry:
                    continue

                if nullable:
                    fix_sql = (
                        f"UPDATE `{table}` SET `{col}` = NULL "
                        f"WHERE `{col}` = '0000-00-00 00:00:00'"
                    )
                    action = 'SET NULL'
                else:
                    fix_sql = (
                        f"UPDATE `{table}` SET `{col}` = '{_SENTINEL}' "
                        f"WHERE `{col}` = '0000-00-00 00:00:00'"
                    )
                    action = f'SET {_SENTINEL}'

                with connection.cursor() as cur:
                    cur.execute(fix_sql)
                    rows = cur.rowcount

                total_fixed += rows
                self.stdout.write(
                    self.style.SUCCESS(f'    → Fixed {rows} row(s) ({action})')
                )

        if dry:
            self.stdout.write(self.style.WARNING(
                'Dry-run complete — no changes written.'
            ))
        else:
            self.stdout.write(self.style.SUCCESS(
                f'Done — {total_fixed} row(s) fixed across all tables.'
            ))
