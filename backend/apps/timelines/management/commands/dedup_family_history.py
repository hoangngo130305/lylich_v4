"""
Management command: xóa các history entries trùng lặp của family members.

Nguyên nhân: bug cũ cho phép nút "Nộp hồ sơ" / "Lưu nháp" được nhấn nhiều lần
đồng thời, mỗi lần tạo thêm một bộ history entries mới mà không xóa bộ cũ.

Cách chạy:
    python manage.py dedup_family_history              # dry-run (chỉ báo cáo)
    python manage.py dedup_family_history --apply      # thực sự xóa trùng
    python manage.py dedup_family_history --profile 5  # chỉ profile ID=5
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from apps.timelines.models import HistoryEntry


class Command(BaseCommand):
    help = "Xóa history entries trùng lặp của family members (giữ bản có sort_order nhỏ nhất)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--apply",
            action="store_true",
            help="Thực sự xóa; mặc định chỉ dry-run.",
        )
        parser.add_argument(
            "--profile",
            type=int,
            default=None,
            help="Chỉ xử lý một profile_id cụ thể.",
        )

    def handle(self, *args, **options):
        apply = options["apply"]
        profile_filter = options["profile"]

        qs = HistoryEntry.objects.filter(
            entry_type="family",
            family_member__isnull=False,
        ).select_related("family_member")

        if profile_filter:
            qs = qs.filter(profile_id=profile_filter)

        # Group by (profile_id, family_member_id, from_year, from_month, to_year, to_month, description)
        from collections import defaultdict
        groups = defaultdict(list)
        for entry in qs.order_by("family_member_id", "sort_order", "id"):
            key = (
                entry.profile_id,
                entry.family_member_id,
                entry.from_year,
                entry.from_month,
                entry.to_year,
                entry.to_month,
                (entry.description or "").strip(),
                entry.is_present,
                entry.is_deceased,
            )
            groups[key].append(entry)

        total_duplicates = 0
        ids_to_delete = []
        for key, entries in groups.items():
            if len(entries) <= 1:
                continue
            # Keep first (lowest sort_order / lowest id), delete the rest
            keep = entries[0]
            dupes = entries[1:]
            total_duplicates += len(dupes)
            for d in dupes:
                ids_to_delete.append(d.id)
            self.stdout.write(
                f"  profile={key[0]} fam_member={key[1]} "
                f"{key[2]}/{key[3]}–{key[4]}/{key[5]} "
                f'"{(key[6] or "")[:40]}" '
                f"→ giữ id={keep.id}, xóa {[d.id for d in dupes]}"
            )

        self.stdout.write(
            self.style.WARNING(
                f"\nTổng: {total_duplicates} entries trùng lặp "
                f"({'sẽ bị xóa' if apply else 'dry-run — chưa xóa'})."
            )
        )

        if apply and ids_to_delete:
            with transaction.atomic():
                deleted, _ = HistoryEntry.objects.filter(id__in=ids_to_delete).delete()
            self.stdout.write(self.style.SUCCESS(f"Đã xóa {deleted} entries trùng lặp."))
        elif not apply:
            self.stdout.write("Chạy lại với --apply để thực sự xóa.")
