"""
Xoa vinh vien mot danh sach tai khoan quan chung (theo so dien thoai) da duoc
xac nhan thu cong - dung cho viec don du lieu test/seed tren server that.

Mac dinh chi XEM TRUOC (dry-run), khong xoa gi ca:
    python manage.py delete_accounts

Chi khi them --confirm moi thuc su xoa:
    python manage.py delete_accounts --confirm
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models.deletion import ProtectedError

PHONES = [
    "0567845673",  # Ngo Dinh Hoang
    "0835641288",  # pham H Minh
    "0453423456",  # test1
    "0675674543",  # KHAILE
    "0919775034",  # pham van minh
    "0956352457",  # dbdfd
    "0919775012",  # phamhoangminh1
    "0999215939",  # TEST-KHONG ND
    "0999451618",  # PHAM HOANG MINH
    "0835641299",  # phamhoangminh
    "0999195072",  # NGUYEN THI LIMH
    "0999203977",  # Ho so moi 12/05/2026 17:28
    "0999272221",  # Ho so moi 12/05/2026 17:27
    "0999435644",  # Test Tao Nhanh 2
    "0901111011",  # Ngo Dinh Hoang (seed)
    "0901111010",  # Truong Thi Hang (seed)
    "0901111009",  # Tran Thi Hoa (seed)
    "0901111008",  # Bui Quang Huy (seed)
    "0901111007",  # Vo Thi Lan (seed)
    "0901111006",  # Hoang Van Duc (seed)
    "0901111005",  # Dinh Thi Nhung (seed)
    "0901111004",  # Nguyen Van Binh (seed)
    "0901111003",  # Pham Thi Dung (seed)
    "0901111002",  # Tran Minh Tuan (seed)
    "0901111001",  # Le Thi Mai (seed)
    "0967561234",  # Nguyen Van Anh
    "0987675612",  # Nguyen Van A
    "0945671234",  # test
]


class Command(BaseCommand):
    help = 'Xoa cac tai khoan quan chung theo danh sach so dien thoai da xac nhan (mac dinh dry-run)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--confirm', action='store_true',
            help='Thuc su xoa. Khong co co nay thi lenh chi hien danh sach se bi xoa, khong xoa gi.',
        )

    def handle(self, *args, **options):
        from apps.accounts.models import User
        from apps.uploads.models import UploadedFile

        users = User.objects.filter(phone__in=PHONES).select_related('profile')
        found_phones = set(users.values_list('phone', flat=True))
        missing = [p for p in PHONES if p not in found_phones]

        self.stdout.write(f'Tim thay {users.count()}/{len(PHONES)} tai khoan trong danh sach:')
        for u in users:
            profile = getattr(u, 'profile', None)
            status = profile.status if profile else '(chua co ho so)'
            self.stdout.write(f'  - {u.full_name!r:30} | {u.phone} | trang thai ho so: {status}')

        if missing:
            self.stdout.write(self.style.WARNING(
                f'\nKhong tim thay {len(missing)} so dien thoai trong he thong (co the da bi xoa truoc do): {missing}'
            ))

        if not users.exists():
            self.stdout.write(self.style.WARNING('\nKhong co gi de xoa.'))
            return

        if not options['confirm']:
            self.stdout.write(self.style.WARNING(
                '\n>>> DAY LA CHE DO XEM TRUOC (dry-run) - CHUA XOA GI CA. <<<\n'
                'Kiem tra lai danh sach o tren cho dung, roi chay lai voi --confirm de thuc su xoa:\n'
                '    python manage.py delete_accounts --confirm'
            ))
            return

        with transaction.atomic():
            deleted_files_count, _ = UploadedFile.objects.filter(uploader__in=users).delete()
            deleted_total, cleared_protected = self._force_delete(users)

        extra = (
            f' (da don truoc {cleared_protected} ban ghi lien quan bi rang buoc PROTECT: '
            f'lich su duyet, file xuat Word...)' if cleared_protected else ''
        )
        self.stdout.write(self.style.SUCCESS(
            f'\nDa xoa xong: {deleted_total} ban ghi lien quan '
            f'(tai khoan, ho so, gia dinh, gop y, lich su duyet...), '
            f'{deleted_files_count} file da upload.{extra}'
        ))

    def _force_delete(self, queryset, max_attempts=10):
        """Delete a queryset, automatically clearing any PROTECT-blocking related
        objects (audit/history rows referencing these users as the "actor") first,
        instead of having to enumerate every such model by hand. Retries until the
        real delete succeeds or we give up after max_attempts (safety valve against
        an infinite loop if something is misbehaving)."""
        cleared = 0
        for _ in range(max_attempts):
            try:
                deleted_total, _by_model = queryset.delete()
                return deleted_total, cleared
            except ProtectedError as e:
                protected_objects = e.protected_objects
                by_model = {}
                for obj in protected_objects:
                    by_model.setdefault(type(obj), []).append(obj.pk)
                for model, pks in by_model.items():
                    self.stdout.write(
                        f'  (don truoc {len(pks)} ban ghi {model.__name__} dang chan xoa)'
                    )
                    n, _ = model.objects.filter(pk__in=pks).delete()
                    cleared += n
        raise RuntimeError(
            f'Da thu {max_attempts} lan van con ban ghi PROTECT chan xoa — dung lai de tranh vong lap vo tan.'
        )
