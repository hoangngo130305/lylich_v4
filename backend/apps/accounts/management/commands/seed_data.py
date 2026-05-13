"""
python manage.py seed_data          — insert sample data (skip if already exists)
python manage.py seed_data --reset  — drop existing sample data first
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import transaction
import datetime


class Command(BaseCommand):
    help = 'Seed database với dữ liệu mẫu cho demo / phát triển'

    def add_arguments(self, parser):
        parser.add_argument('--reset', action='store_true', help='Xóa dữ liệu cũ trước khi seed')

    def handle(self, *args, **options):
        if options['reset']:
            self._reset()
        with transaction.atomic():
            self._seed_refs()
            users  = self._seed_users()
            profiles = self._seed_profiles(users)
            self._seed_reviews(users, profiles)
            self._seed_verifications(users, profiles)
            self._seed_notifications(users, profiles)
            self._seed_family(profiles)
            self._seed_timelines(profiles)
        self.stdout.write(self.style.SUCCESS('✅ Seed hoàn tất!'))

    # ──────────────────────────────────────────────────────────────────────
    def _reset(self):
        from apps.notifications.models import Notification
        from apps.verification.models import VerificationRequest
        from apps.profiles.models import ProfileReview, Profile
        from apps.accounts.models import User
        from apps.family.models import FamilyMember
        from apps.timelines.models import (
            HistoryEntry, WorkHistory, EducationHistory, Award,
            OverseasTravel, OverseasRelative, OrgParticipation,
        )

        self.stdout.write('Đang xóa dữ liệu cũ…')
        Notification.objects.all().delete()
        VerificationRequest.objects.all().delete()
        ProfileReview.objects.all().delete()
        HistoryEntry.objects.all().delete()
        WorkHistory.objects.all().delete()
        EducationHistory.objects.all().delete()
        Award.objects.all().delete()
        OverseasTravel.objects.all().delete()
        OverseasRelative.objects.all().delete()
        OrgParticipation.objects.all().delete()
        FamilyMember.objects.all().delete()
        Profile.objects.all().delete()
        # Chỉ xóa tài khoản được tạo bởi seed (090*), giữ nguyên tài khoản thật
        User.objects.filter(phone__startswith='090').delete()
        # Bỏ qua xóa reference tables (Role, EthnicGroup, v.v.) vì dùng get_or_create
        self.stdout.write('  Đã xóa.')

    # ──────────────────────────────────────────────────────────────────────
    def _seed_refs(self):
        from apps.accounts.models import Role
        from apps.common.models import EthnicGroup, Religion, EducationLevel, PoliticalLevel, AdministrativeUnit

        self.stdout.write('Đang tạo dữ liệu tham chiếu…')

        # Roles
        roles_data = [
            ('admin',       'Quản trị hệ thống',        'Toàn quyền hệ thống'),
            ('can_bo_bxd',  'Cán bộ Ban Xây dựng Đảng', 'Thẩm định và phê duyệt hồ sơ'),
            ('quan_chung',  'Quần chúng',                'Kê khai lý lịch xin vào Đảng'),
        ]
        for code, name, desc in roles_data:
            Role.objects.get_or_create(code=code, defaults={'name': name, 'description': desc})

        # Dân tộc
        ethnics = ['Kinh', 'Tày', 'Thái', 'Hoa', 'Khmer', 'Mường', 'Nùng', 'Hmông', 'Dao', 'Gia-rai', 'Khác']
        for e in ethnics:
            EthnicGroup.objects.get_or_create(name=e)

        # Tôn giáo
        religions = ['Không', 'Phật giáo', 'Công giáo', 'Cao Đài', 'Tin Lành', 'Hồi giáo', 'Khác']
        for r in religions:
            Religion.objects.get_or_create(name=r)

        # Trình độ học vấn
        edu_levels = [
            ('tieu_hoc',    'Tiểu học',        1),
            ('thcs',        'THCS (9/12)',      2),
            ('thpt',        '12/12',            3),
            ('trung_cap',   'Trung cấp',        4),
            ('cao_dang',    'Cao đẳng',         5),
            ('dai_hoc',     'Đại học',          6),
            ('thac_si',     'Thạc sĩ',          7),
            ('tien_si',     'Tiến sĩ',          8),
        ]
        for code, name, sort in edu_levels:
            EducationLevel.objects.get_or_create(code=code, defaults={'name': name, 'sort': sort})

        # Trình độ chính trị
        pol_levels = [
            ('so_cap',    'Sơ cấp chính trị'),
            ('trung_cap', 'Trung cấp chính trị'),
            ('cao_cap',   'Cao cấp chính trị'),
            ('cu_nhan',   'Cử nhân chính trị'),
        ]
        for code, name in pol_levels:
            PoliticalLevel.objects.get_or_create(code=code, defaults={'name': name})

        # Đơn vị hành chính (TP.HCM → Nhà Bè)
        tp_hcm, _ = AdministrativeUnit.objects.get_or_create(
            code='79', type='province',
            defaults={'name': 'TP. Hồ Chí Minh', 'parent': None}
        )
        nha_be, _ = AdministrativeUnit.objects.get_or_create(
            code='794', type='district',
            defaults={'name': 'Huyện Nhà Bè', 'parent': tp_hcm}
        )
        wards_data = [
            ('79401', 'Thị trấn Nhà Bè'),
            ('79402', 'Xã Phước Kiển'),
            ('79403', 'Xã Long Thới'),
            ('79404', 'Xã Nhơn Đức'),
            ('79405', 'Xã Phú Xuân'),
            ('79406', 'Xã Hiệp Phước'),
            ('79407', 'Xã Nhà Bè'),
        ]
        for code, name in wards_data:
            AdministrativeUnit.objects.get_or_create(
                code=code, type='ward',
                defaults={'name': name, 'parent': nha_be}
            )

        self.stdout.write('  Dữ liệu tham chiếu ✓')

    # ──────────────────────────────────────────────────────────────────────
    def _seed_users(self):
        from apps.accounts.models import User, Role

        self.stdout.write('Đang tạo users…')

        role_admin  = Role.objects.get(code='admin')
        role_officer = Role.objects.get(code='can_bo_bxd')
        role_qc     = Role.objects.get(code='quan_chung')

        # ── Admin ──────────────────────────────────────────────────────────
        admin, created = User.objects.get_or_create(
            phone='0900000001',
            defaults={
                'full_name': 'Quản trị viên',
                'role': role_admin,
                'status': 'active',
                'is_staff': True,
                'is_superuser': True,
                'email': 'admin@lylich.gov.vn',
            }
        )
        if created:
            admin.set_password('Admin@2026')
            admin.save()
            self.stdout.write('  admin: 0900000001 / Admin@2026')

        # ── Cán bộ BXD ─────────────────────────────────────────────────────
        officers_data = [
            ('0900000002', 'Nguyễn Thị Hương', 'huong@lylich.gov.vn'),
            ('0900000003', 'Trần Văn Khoa',    'khoa@lylich.gov.vn'),
        ]
        officers = []
        for phone, name, email in officers_data:
            u, created = User.objects.get_or_create(
                phone=phone,
                defaults={'full_name': name, 'role': role_officer, 'status': 'active', 'email': email}
            )
            if created:
                u.set_password('Officer@2026')
                u.save()
                self.stdout.write(f'  officer: {phone} / Officer@2026')
            officers.append(u)

        # ── Quần chúng ─────────────────────────────────────────────────────
        qc_data = [
            ('0901111001', 'Lê Thị Mai',       'lethi.mai@gmail.com',      '079095001001'),
            ('0901111002', 'Trần Minh Tuấn',   'tran.tuan@gmail.com',      '079093002002'),
            ('0901111003', 'Phạm Thị Dung',    'pham.dung@gmail.com',      '079097003003'),
            ('0901111004', 'Nguyễn Văn Bình',  'nguyen.binh@gmail.com',    '079095004004'),
            ('0901111005', 'Đinh Thị Nhung',   'dinh.nhung@gmail.com',     '079091005005'),
            ('0901111006', 'Hoàng Văn Đức',    'hoang.duc@gmail.com',      '079095006006'),
            ('0901111007', 'Võ Thị Lan',       'vo.lan@gmail.com',         '079096007007'),
            ('0901111008', 'Bùi Quang Huy',    'bui.huy@gmail.com',        '079091008008'),
            ('0901111009', 'Trương Thị Hằng',  'truong.hang@gmail.com',    '079095009009'),
            ('0901111010', 'Nguyễn Thị Bình An','nguyen.binh.an@gmail.com','079094010010'),
            ('0901111011', 'Ngô Đình Hoàng',   'ngo.dinh.hoang@gmail.com', '079092011011'),
        ]
        qc_users = []
        for phone, name, email, cccd in qc_data:
            u, created = User.objects.get_or_create(
                phone=phone,
                defaults={'full_name': name, 'role': role_qc, 'status': 'active', 'email': email, 'cccd': cccd}
            )
            if created:
                u.set_password('Qc@12345')
                u.save()
                self.stdout.write(f'  qc: {phone} / Qc@12345')
            qc_users.append(u)

        self.stdout.write('  Users ✓')
        return {'admin': admin, 'officers': officers, 'qc_users': qc_users}

    # ──────────────────────────────────────────────────────────────────────
    def _seed_profiles(self, users):
        from apps.profiles.models import Profile
        from apps.common.models import EthnicGroup, Religion, EducationLevel, AdministrativeUnit

        self.stdout.write('Đang tạo hồ sơ…')

        officer1, officer2 = users['officers'][0], users['officers'][1]
        kinh = EthnicGroup.objects.filter(name='Kinh').first()
        khong = Religion.objects.filter(name='Không').first()
        phat = Religion.objects.filter(name='Phật giáo').first()
        edu_dh = EducationLevel.objects.filter(code='dai_hoc').first()
        edu_thpt = EducationLevel.objects.filter(code='thpt').first()
        edu_tc = EducationLevel.objects.filter(code='trung_cap').first()
        ward_nhabe = AdministrativeUnit.objects.filter(code='79407').first()
        ward_pkien = AdministrativeUnit.objects.filter(code='79402').first()
        ward_lthuoi = AdministrativeUnit.objects.filter(code='79403').first()
        ward_hiephuoc = AdministrativeUnit.objects.filter(code='79406').first()  # Ấp 4 – Hiệp Phước

        now = timezone.now()

        profiles_data = [
            # (user_idx, profile_number, gender, dob, status, ai_score, submitted_offset_days,
            #  full_name_confirm, birth_detail, hometown_detail, current_address,
            #  occupation, workplace, job_title, edu_level, officer, ward, birth_ward,
            #  youth_union_date, self_assess_wc, religion)
            (0, 'HS-2026-001', 'female', '1990-03-15', 'submitted',   94, 22,
             'Lê Thị Mai',      'Xã Nhà Bè, Huyện Nhà Bè, TP. Hồ Chí Minh',
             'Xã Nhà Bè, TP. Hồ Chí Minh',   'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM',
             'Giáo viên tiểu học',             'Trường Tiểu học Nhà Bè A',          'Giáo viên',
             edu_dh, officer1, ward_nhabe, ward_nhabe, '2007-03-15', 220, khong),

            (1, 'HS-2026-002', 'male',   '1993-07-20', 'pending',     87, 23,
             'Trần Minh Tuấn',  'Xã Phước Kiển, Huyện Nhà Bè, TP. Hồ Chí Minh',
             'Xã Phước Kiển, TP. Hồ Chí Minh', 'Ấp 3, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM',
             'Nhân viên kỹ thuật',              'Công ty TNHH Xây dựng ABC',         'Nhân viên kỹ thuật',
             edu_dh, officer1, ward_pkien, ward_pkien, '2009-07-20', 205, khong),

            (2, 'HS-2026-003', 'female', '1997-11-05', 'returned',    61, 25,
             'Phạm Thị Dung',   'Xã Long Thới, Huyện Nhà Bè, TP. Hồ Chí Minh',
             'Xã Long Thới, TP. Hồ Chí Minh',  'Ấp 2, Xã Long Thới, Huyện Nhà Bè, TP.HCM',
             'Công nhân may',                   'Công ty CP Dệt May Nhà Bè',          'Công nhân',
             edu_thpt, officer2, ward_lthuoi, ward_lthuoi, '2013-11-05', 0, khong),

            (3, 'HS-2026-004', 'male',   '1995-04-28', 'returned',    72, 26,
             'Nguyễn Văn Bình', 'Xã Nhà Bè, Huyện Nhà Bè, TP. Hồ Chí Minh',
             'Xã Nhà Bè, TP. Hồ Chí Minh',    'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM',
             'Lái xe',                          'Công ty vận tải Nhà Bè',             'Lái xe',
             edu_thpt, officer1, ward_nhabe, ward_nhabe, '2011-04-28', 0, khong),

            (4, 'HS-2026-005', 'female', '1991-09-12', 'submitted',   91, 17,
             'Đinh Thị Nhung',  'Xã Nhà Bè, Huyện Nhà Bè, TP. Hồ Chí Minh',
             'Xã Nhà Bè, TP. Hồ Chí Minh',    'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM',
             'Y tá',                            'Trạm y tế xã Nhà Bè',                'Y tá',
             edu_tc, officer2, ward_nhabe, ward_nhabe, '2007-09-12', 195, phat),

            (5, None,          'male',   '1999-02-14', 'draft',        0,  0,
             'Hoàng Văn Đức',  'Xã Nhà Bè, Huyện Nhà Bè, TP. Hồ Chí Minh',
             'Xã Nhà Bè, TP. Hồ Chí Minh',    'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM',
             'Sinh viên',                       'Trường Đại học Nông Lâm TP.HCM',    'Sinh viên',
             edu_dh, officer1, ward_nhabe, ward_nhabe, '2015-02-14', 0, khong),

            (6, None,          'female', '1998-06-30', 'draft',        0,  0,
             'Võ Thị Lan',     'Xã Phước Kiển, Huyện Nhà Bè, TP. Hồ Chí Minh',
             'Xã Phước Kiển, TP. Hồ Chí Minh', 'Ấp 2, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM',
             'Kế toán',                         'UBND Xã Phước Kiển',                'Kế toán',
             edu_dh, officer2, ward_pkien, ward_pkien, '2014-06-30', 0, khong),

            (7, None,          'male',   '1996-12-08', 'draft',        0,  0,
             'Bùi Quang Huy',  'Xã Long Thới, Huyện Nhà Bè, TP. Hồ Chí Minh',
             'Xã Long Thới, TP. Hồ Chí Minh',  'Ấp 3, Xã Long Thới, Huyện Nhà Bè, TP.HCM',
             'Nông dân',                        'Hộ nông dân gia đình',               'Nông dân',
             edu_thpt, officer1, ward_lthuoi, ward_lthuoi, '2012-12-08', 0, khong),

            (8, 'HS-2026-009', 'female', '1994-08-22', 'verifying',   88, 30,
             'Trần Thị Hoa',    'Xã Hiệp Phước, Huyện Nhà Bè, TP. Hồ Chí Minh',
             'Xã Hiệp Phước, TP. Hồ Chí Minh',  'Ấp 4, Xã Hiệp Phước, Huyện Nhà Bè, TP.HCM',
             'Thợ mộc',                         'Xưởng mộc Nhà Bè',                   'Thợ mộc',
             edu_thpt, officer2, ward_hiephuoc, ward_hiephuoc, '2011-08-22', 210, khong),

              (9, 'HS-2026-010', 'female', '1994-08-22', 'completed',   98, 45,
               'Trương Thị Hằng', 'Xã Nhà Bè, Huyện Nhà Bè, TP. Hồ Chí Minh',
               'Xã Nhà Bè, TP. Hồ Chí Minh',    'Ấp 2, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM',
               'Giáo viên THCS',                  'Trường THCS Nhà Bè',                 'Giáo viên',
               edu_dh, officer1, ward_nhabe, ward_nhabe, '2010-08-22', 235, khong),

            (10, 'HS-2026-011', 'male',   '1985-06-15', 'submitted',   96, 8,
             'Ngô Đình Hoàng',  'Xã Phước Kiển, Huyện Nhà Bè, TP. Hồ Chí Minh',
             'Xã Phước Kiển, TP. Hồ Chí Minh',  'Ấp 2, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM',
             'Trưởng phòng kỹ thuật',            'Trung tâm Phát triển Quản lý Huyện',  'Trưởng phòng',
             edu_dh, officer1, ward_pkien, ward_pkien, '2003-06-15', 520, khong),
        ]

        created_profiles = []
        for idx, (ui, pnum, gender, dob, status, score, offset_days, *rest) in enumerate(profiles_data):
            (fname, birth_detail, hometown, cur_addr,
             occ, workplace, job_title, edu_level, officer, cur_ward, birth_ward,
             yu_date, self_wc, religion) = rest

            user = users['qc_users'][ui]
            if Profile.objects.filter(user=user).exists():
                created_profiles.append(Profile.objects.get(user=user))
                continue

            submitted_at = None
            if offset_days > 0:
                submitted_at = now - datetime.timedelta(days=offset_days)

            approved_at = None
            completed_at = None
            if status == 'approved':
                approved_at = submitted_at + datetime.timedelta(days=10) if submitted_at else None
            if status == 'completed':
                approved_at = submitted_at + datetime.timedelta(days=8) if submitted_at else None
                completed_at = submitted_at + datetime.timedelta(days=15) if submitted_at else None

            return_reason = None
            last_returned_at = None
            if status == 'returned':
                return_reason = 'Cần bổ sung thông tin lịch sử bản thân giai đoạn 2015–2018.'
                last_returned_at = now - datetime.timedelta(days=3)

            p = Profile.objects.create(
                user=user,
                officer_in_charge=officer,
                profile_number=pnum,
                full_name=fname,
                gender=gender,
                dob=dob,
                birth_place_detail=birth_detail,
                birth_place_ward=birth_ward,
                hometown_detail=hometown,
                current_address=cur_addr,
                current_ward=cur_ward,
                ethnic_group=kinh,
                religion=religion,
                edu_level=edu_level,
                occupation=occ,
                workplace=workplace,
                job_title=job_title,
                youth_union_date=yu_date if yu_date else None,
                ai_score=score if score > 0 else None,
                ai_last_scanned_at=now if score > 0 else None,
                status=status,
                submitted_at=submitted_at,
                approved_at=approved_at,
                completed_at=completed_at,
                return_reason=return_reason,
                last_returned_at=last_returned_at,
                self_assessment_word_count=self_wc if self_wc > 0 else None,
                created_by=officer,
                # ── Additional fields for complete profiles (esp. for NGO DINH HOANG) ──
                marital_status='married' if idx == 10 else 'single',
                marriage_date=now.date() - datetime.timedelta(days=5475) if idx == 10 else None,  # ~15 years ago
                general_edu_level='Đại học' if edu_level == edu_dh else 'Trung học phổ thông',
                edu_specialization='Quản lý công' if idx == 10 else 'Giáo dục',
                edu_school='Trường Đại học Kinh tế TP.HCM' if idx == 10 else 'Trường Đại học Sư phạm',
                edu_major='Quản lý công' if idx == 10 else 'Sư phạm các môn',
                edu_graduation_year=2007 if idx == 10 else 2012,
                foreign_languages='Tiếng Anh (trung cấp)' if idx == 10 else None,
                political_history_text='Đoàn viên Thanh niên Cộng sản Hồ Chí Minh từ năm 2004. Tham gia Đảng Cộng sản Việt Nam năm 2010. Nhiệt tình trong công tác, có kỷ luật cao.' if idx == 10 else None,
                awards_text='- Khen thưởng xuất sắc hoàn thành nhiệm vụ, năm 2015\n- Bằng khen của UBND Huyện Nhà Bè, năm 2018\n- Giải thưởng lao động xuất sắc, năm 2020' if idx == 10 else None,
                self_assessment_text='Bản thân là người có ý thức chính trị tốt, luôn tuân thủ kỷ luật Đảng và pháp luật nhà nước. Tận tâm với công việc, có khả năng quản lý tốt, sáng tạo trong thực hiện nhiệm vụ. Được cấp trên và đồng chí đánh giá cao. Sẵn sàng rèn luyện và nâng cao trình độ lý luận chính trị. Cam kết sẽ tiếp tục nâng cao năng lực, cống hiến cho Đảng và nhân dân.' if idx == 10 else None,
                declaration_name='Ngô Đình Hoàng' if idx == 10 else fname,
                declaration_date=submitted_at.date() if submitted_at else None,
            )
            created_profiles.append(p)
            self.stdout.write(f'  profile: {fname} [{status}]')

        self.stdout.write('  Profiles ✓')
        return created_profiles

    # ──────────────────────────────────────────────────────────────────────
    def _seed_reviews(self, users, profiles):
        from apps.profiles.models import ProfileReview

        self.stdout.write('Đang tạo lịch sử thẩm định…')

        officer1 = users['officers'][0]
        officer2 = users['officers'][1]
        now = timezone.now()

        reviews_data = [
            # (profile_idx, action, from_status, to_status, comment, days_ago, reviewer)
            (0, 'submit',  None,        'submitted',   'Quần chúng tự nộp hồ sơ.', 22, officer1),
            (1, 'submit',  None,        'submitted',   'Quần chúng tự nộp hồ sơ.', 23, officer1),
            (1, 'note',    'submitted', 'pending',     'Đã nhận hồ sơ, đang xem xét.', 20, officer1),
            (2, 'submit',  None,        'submitted',   'Quần chúng tự nộp hồ sơ.', 25, officer2),
            (2, 'return',  'submitted', 'returned',    'Thiếu thông tin lịch sử công tác giai đoạn 2019–2022. Yêu cầu bổ sung.', 3, officer2),
            (3, 'submit',  None,        'submitted',   'Quần chúng tự nộp hồ sơ.', 26, officer1),
            (3, 'return',  'submitted', 'returned',    'Cần bổ sung lịch sử gia đình phía cha.', 5, officer1),
            (4, 'submit',  None,        'submitted',   'Quần chúng tự nộp hồ sơ.', 17, officer2),
            (8, 'submit',  None,        'submitted',   'Quần chúng tự nộp hồ sơ.', 45, officer1),
            (8, 'approve', 'submitted', 'approved',    'Hồ sơ đầy đủ, chuyển xác minh.', 37, officer1),
            (8, 'complete','approved',  'completed',   'Xác minh hoàn tất, hồ sơ hoàn thiện.', 30, officer1),
            (9, 'submit',  None,        'submitted',   'Quần chúng tự nộp hồ sơ.', 35, officer2),
            (9, 'approve', 'submitted', 'approved',    'Hồ sơ đạt yêu cầu.', 25, officer2),
            (10, 'submit', None,        'submitted',   'Quần chúng tự nộp hồ sơ. Hồ sơ đầy đủ, chi tiết.', 8, officer1),
        ]

        for pi, action, fs, ts, comment, days_ago, reviewer in reviews_data:
            if pi >= len(profiles):
                continue
            p = profiles[pi]
            ts_dt = now - datetime.timedelta(days=days_ago)
            rev, created = ProfileReview.objects.get_or_create(
                profile=p, action=action, reviewer=reviewer,
                defaults={'from_status': fs, 'to_status': ts, 'comment': comment}
            )
            if created:
                # Override auto_now_add via update() to backdate activity feed
                ProfileReview.objects.filter(pk=rev.pk).update(created_at=ts_dt)

        self.stdout.write('  Reviews ✓')

    # ──────────────────────────────────────────────────────────────────────
    def _seed_verifications(self, users, profiles):
        from apps.verification.models import VerificationRequest

        self.stdout.write('Đang tạo yêu cầu xác minh…')

        officer1 = users['officers'][0]
        officer2 = users['officers'][1]
        now = timezone.now()
        today = now.date()

        verifs = [
            # (profile_idx, agency, content, urgency, status, sent_days_ago, deadline_days_from_today)
            (0, 'UBND xã Nhà Bè',       'Xác minh nơi cư trú và lịch sử công tác',    'normal', 'pending',  27, 3),
            (1, 'Công an xã Phước Kiển', 'Xác minh nhân thân, không tiền án tiền sự',  'normal', 'received', 30, 10),
            (2, 'UBND xã Long Thới',     'Xác minh hộ khẩu và khai sinh',              'urgent', 'overdue',  20, -3),
            (9, 'Bệnh viện Huyện Nhà Bè','Xác nhận quá trình công tác 2015–2026',      'normal', 'completed',35, 20),
        ]

        for pi, agency, content, urgency, status, sent_days_ago, deadline_offset in verifs:
            if pi >= len(profiles):
                continue
            p = profiles[pi]
            sent_date = (now - datetime.timedelta(days=sent_days_ago)).date()
            deadline = today + datetime.timedelta(days=deadline_offset)
            officer = officer1 if pi % 2 == 0 else officer2

            VerificationRequest.objects.get_or_create(
                profile=p,
                agency_name=agency,
                defaults={
                    'content':    content,
                    'urgency':    urgency,
                    'status':     status,
                    'sent_date':  sent_date,
                    'deadline':   deadline,
                    'created_by': officer,
                }
            )

        self.stdout.write('  Verifications ✓')

    # ──────────────────────────────────────────────────────────────────────
    def _seed_notifications(self, users, profiles):
        from apps.notifications.models import Notification

        self.stdout.write('Đang tạo thông báo…')

        officer1 = users['officers'][0]
        now = timezone.now()

        notif_data = [
            # (recipient_idx, profile_idx, channel, type_, subject, body, is_read, days_ago)
            (0, 0, 'sms',    'account_created',
             'Tài khoản kê khai đã được tạo',
             'Kính gửi Lê Thị Mai, tài khoản kê khai lý lịch Mẫu 2-KNĐ của bạn đã được tạo. Vui lòng đăng nhập và hoàn thiện hồ sơ.', True, 50),
            (0, 0, 'sms',    'profile_returned',
             'Thông báo trạng thái hồ sơ',
             'Kính gửi Lê Thị Mai, hồ sơ lý lịch đã được nhận. Đang trong quá trình thẩm định.', True, 22),
            (1, 1, 'sms',    'profile_returned',
             'Hồ sơ đang được xem xét',
             'Kính gửi Trần Minh Tuấn, hồ sơ lý lịch của bạn đang được Ban Xây dựng Đảng xem xét.', False, 20),
            (2, 2, 'sms',    'profile_returned',
             'Yêu cầu bổ sung hồ sơ',
             'Kính gửi Phạm Thị Dung, hồ sơ cần bổ sung thêm thông tin. Vui lòng đăng nhập để xem chi tiết.', False, 3),
            (3, 3, 'sms',    'profile_returned',
             'Yêu cầu bổ sung hồ sơ',
             'Kính gửi Nguyễn Văn Bình, hồ sơ cần bổ sung lịch sử gia đình phía cha. Vui lòng cập nhật.', False, 5),
            (5, 5, 'sms',    'account_created',
             'Tài khoản kê khai đã được tạo',
             'Kính gửi Hoàng Văn Đức, tài khoản kê khai lý lịch của bạn đã được tạo.', True, 19),
            (8, 8, 'email',  'profile_approved',
             'Hồ sơ lý lịch đã hoàn thiện',
             'Kính gửi Trương Thị Hằng, hồ sơ lý lịch Mẫu 2-KNĐ đã được hoàn thiện và lưu trữ.', True, 30),
            (9, 9, 'sms',    'profile_approved',
             'Hồ sơ đã được phê duyệt',
             'Kính gửi Nguyễn Thị Bình An, hồ sơ lý lịch đã được phê duyệt. Chúc mừng bạn.', True, 25),
        ]

        for ri, pi, channel, ntype, subject, body, is_read, days_ago in notif_data:
            if ri >= len(users['qc_users']) or pi >= len(profiles):
                continue
            recipient = users['qc_users'][ri]
            profile   = profiles[pi]
            sent_at   = now - datetime.timedelta(days=days_ago)
            notif, created = Notification.objects.get_or_create(
                recipient=recipient,
                subject=subject,
                defaults={
                    'sender':      officer1,
                    'profile':     profile,
                    'channel':     channel,
                    'type':        ntype,
                    'body':        body,
                    'is_read':     is_read,
                    'read_at':     sent_at + datetime.timedelta(hours=2) if is_read else None,
                    'sent_status': 'sent',
                    'sent_at':     sent_at,
                }
            )
            if created:
                Notification.objects.filter(pk=notif.pk).update(created_at=sent_at)

        self.stdout.write('  Notifications ✓')

    # ──────────────────────────────────────────────────────────────────────
    def _seed_family(self, profiles):
        from apps.family.models import FamilyMember

        self.stdout.write('Đang tạo thành viên gia đình…')

        # Seed family data for profile 0 (Lê Thị Mai)
        if profiles and len(profiles) > 0:
            p = profiles[0]
            if not FamilyMember.objects.filter(profile=p).exists():
                members = [
                    # (relationship, full_name, birth_year, birth_place, current_address,
                    #  ethnic, religion, occupation, is_party, party_year, notes)
                    ('cha_ruot', 'Lê Văn Hùng',   1962,
                     'Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM',
                     'Kinh', 'Không', 'Nông dân', False, None, None),

                    ('me_ruot', 'Nguyễn Thị Lan',  1965,
                     'Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM',
                     'Kinh', 'Không', 'Nội trợ', False, None, None),

                    ('ong_noi', 'Lê Văn Bảy',      1935,
                     'Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', '',
                     'Kinh', 'Không', 'Đã mất năm 2010', False, None, 'Mất năm 2010'),

                    ('ba_noi', 'Trần Thị Bé',      1940,
                     'Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', '',
                     'Kinh', 'Không', 'Đã mất năm 2018', False, None, 'Mất năm 2018'),

                    ('ong_ngoai', 'Nguyễn Văn Tư', 1938,
                     'Xã Long Thới, Huyện Nhà Bè, TP.HCM', '',
                     'Kinh', 'Không', 'Đã mất năm 2015', False, None, 'Mất năm 2015'),

                    ('ba_ngoai', 'Phạm Thị Tám',   1942,
                     'Xã Long Thới, Huyện Nhà Bè, TP.HCM', 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM',
                     'Kinh', 'Không', 'Hưu trí', False, None, None),

                    ('vo_chong', 'Trần Anh Minh',  1988,
                     'Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM',
                     'Kinh', 'Không', 'Công nhân – Công ty Nhà Bè', False, None, 'Kết hôn 15/06/2015'),

                    ('con', 'Trần Thị Ngọc',       2018,
                     'Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM',
                     'Kinh', 'Không', 'Học sinh', False, None, 'Đang học tiểu học'),

                    ('anh_chi_em_ruot', 'Lê Văn Nam', 1988,
                     'Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM',
                     'Kinh', 'Không', 'Công nhân', False, None, None),
                ]

                for sort, (rel, name, birth_yr, birth_place, cur_addr,
                           ethnic, religion, occ, is_party, party_yr, notes) in enumerate(members):
                    fm = FamilyMember.objects.create(
                        profile=p,
                        relationship=rel,
                        sort_order=sort,
                        full_name=name,
                        birth_year=birth_yr,
                        birth_place=birth_place,
                        current_address=cur_addr or None,
                        ethnic_group_text=ethnic,
                        religion_text=religion,
                        occupation=occ,
                        is_party_member=is_party,
                        party_join_year=party_yr,
                        notes=notes,
                    )
                    self.stdout.write(f'  family (p0): {rel} – {name}')

        # Seed family data for profile 10 (Ngô Đình Hoàng)
        if profiles and len(profiles) > 10:
            p = profiles[10]
            if not FamilyMember.objects.filter(profile=p).exists():
                members = [
                    ('cha_ruot', 'Ngô Văn Sáu',     1954,
                     'Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', '',
                     'Kinh', 'Không', 'Hưu trí', True, 2000, 'Mất năm 2020'),

                    ('me_ruot', 'Trần Thị Hoa',     1958,
                     'Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', 'Ấp 2, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM',
                     'Kinh', 'Không', 'Hưu trí', False, None, None),

                    ('vo_chong', 'Phạm Thị Liên',   1987,
                     'Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', 'Ấp 2, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM',
                     'Kinh', 'Không', 'Giáo viên', False, None, 'Kết hôn 20/08/2010'),

                    ('con', 'Ngô Minh Anh',         2012,
                     'Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', 'Ấp 2, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM',
                     'Kinh', 'Không', 'Học sinh', False, None, 'Con trai, năm sinh 2012'),

                    ('anh_chi_em_ruot', 'Ngô Đình Hạnh', 1980,
                     'Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', 'Ấp 2, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM',
                     'Kinh', 'Không', 'Cán bộ xã', True, 2008, None),

                    ('anh_chi_em_ruot', 'Ngô Đình Hiệp', 1983,
                     'Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', 'Ấp 2, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM',
                     'Kinh', 'Không', 'Kỹ sư', False, None, 'Em trai'),
                ]

                for sort, (rel, name, birth_yr, birth_place, cur_addr,
                           ethnic, religion, occ, is_party, party_yr, notes) in enumerate(members):
                    fm = FamilyMember.objects.create(
                        profile=p,
                        relationship=rel,
                        sort_order=sort,
                        full_name=name,
                        birth_year=birth_yr,
                        birth_place=birth_place,
                        current_address=cur_addr or None,
                        ethnic_group_text=ethnic,
                        religion_text=religion,
                        occupation=occ,
                        is_party_member=is_party,
                        party_join_year=party_yr,
                        notes=notes,
                    )
                    self.stdout.write(f'  family (p10): {rel} – {name}')

        self.stdout.write('  Family members ✓')

    # ──────────────────────────────────────────────────────────────────────
    def _seed_timelines(self, profiles):
        from apps.timelines.models import (
            HistoryEntry, WorkHistory, EducationHistory, Award
        )

        self.stdout.write('Đang tạo timeline/lịch sử…')
        if not profiles:
            return

        # ── Seed timelines for profile 0 (Lê Thị Mai) ──────────────────────
        p = profiles[0]
        if not HistoryEntry.objects.filter(profile=p).exists():
            self.stdout.write('  Tạo timeline cho Lê Thị Mai (p0)…')

            # Lịch sử bản thân
            history_rows = [
                (None,  1990, None,  1996, False, 'Còn nhỏ, sống với cha mẹ tại ấp 1, xã Nhà Bè, TP.HCM', 'Xã Nhà Bè, TP.HCM'),
                (9,     1996, 8,     2005, False, 'Học Tiểu học và THCS tại Trường THCS Nhà Bè', 'Xã Nhà Bè, TP.HCM'),
                (9,     2005, 6,     2008, False, 'Học THPT tại Trường THPT Nhà Bè. Kết nạp Đoàn 15/3/2007', 'Xã Nhà Bè, TP.HCM'),
                (9,     2008, 6,     2012, False, 'Học Đại học Sư phạm TP.HCM, Khoa Giáo dục Tiểu học', 'TP. Hồ Chí Minh'),
                (8,     2012, None,  None, True,  'Giáo viên Trường Tiểu học Nhà Bè A, xã Nhà Bè, TP.HCM', 'Xã Nhà Bè, TP.HCM'),
            ]
            for i, (fm, fy, tm, ty, present, desc, loc) in enumerate(history_rows):
                HistoryEntry.objects.create(
                    profile=p, entry_type='self', sort_order=i,
                    from_month=fm, from_year=fy,
                    to_month=tm, to_year=ty, is_present=present,
                    description=desc, location=loc,
                )

            # Quá trình công tác
            work_rows = [
                (9, 2008, 6, 2012, False, 'Trường Đại học Sư phạm TP.HCM', 'Sinh viên', 'TP. Hồ Chí Minh'),
                (8, 2012, None, None, True, 'Trường Tiểu học Nhà Bè A', 'Giáo viên', 'Xã Nhà Bè, TP.HCM'),
            ]
            for i, (fm, fy, tm, ty, present, employer, job_title, loc) in enumerate(work_rows):
                WorkHistory.objects.create(
                    profile=p, sort_order=i,
                    from_month=fm, from_year=fy,
                    to_month=tm, to_year=ty, is_present=present,
                    employer=employer, job_title=job_title, location=loc,
                )

            # Quá trình học vấn
            edu_rows = [
                (9, 2008, 6, 2012, False, 'Đại học Sư phạm TP.HCM', 'Giáo dục Tiểu học', 'Cử nhân'),
                (3, 2020, 12, 2020, False, 'Trung tâm Bồi dưỡng CT Huyện Nhà Bè', 'Lý luận chính trị Sơ cấp', 'Chứng chỉ'),
            ]
            for i, (fm, fy, tm, ty, present, school, major, cert) in enumerate(edu_rows):
                EducationHistory.objects.create(
                    profile=p, sort_order=i,
                    from_month=fm, from_year=fy,
                    to_month=tm, to_year=ty, is_present=present,
                    school=school, major=major, certificate=cert,
                )

            # Khen thưởng
            Award.objects.create(
                profile=p, type='award', sort_order=0,
                issued_year=2022, issuer='UBND Huyện Nhà Bè',
                level='Cấp huyện',
                content='Giáo viên dạy giỏi cấp huyện năm học 2021–2022',
            )
            self.stdout.write('  Timeline p0 ✓')

        # ── Seed timelines for profile 10 (Ngô Đình Hoàng) ────────────────
        if len(profiles) > 10:
            p = profiles[10]
            if not HistoryEntry.objects.filter(profile=p).exists():
                self.stdout.write('  Tạo timeline cho Ngô Đình Hoàng (p10)…')

                # Lịch sử bản thân
                history_rows = [
                    (None,  1985, None,  1991, False, 'Tuổi thơ sống với cha mẹ tại ấp 2, xã Phước Kiển, TP.HCM', 'Xã Phước Kiển, TP.HCM'),
                    (9,     1991, 8,     1999, False, 'Học Tiểu học và THCS tại Trường THCS Phước Kiển', 'Xã Phước Kiển, TP.HCM'),
                    (9,     1999, 6,     2003, False, 'Học THPT tại Trường THPT Phước Kiển. Kết nạp Đoàn 1/4/2001. Đảng viên từ 3/10/2003', 'Xã Phước Kiển, TP.HCM'),
                    (9,     2003, 7,     2007, False, 'Học Đại học Kinh tế TP.HCM, chuyên ngành Quản lý công', 'TP. Hồ Chí Minh'),
                    (9,     2007, 5,     2015, False, 'Công tác tại Trung tâm Phát triển Huyện Nhà Bè, Phòng Kỹ thuật và Đầu tư', 'Huyện Nhà Bè'),
                    (6,     2015, None,  None, True,  'Trưởng Phòng Kỹ thuật, Trung tâm Phát triển Quản lý Huyện Nhà Bè', 'Huyện Nhà Bè'),
                ]
                for i, (fm, fy, tm, ty, present, desc, loc) in enumerate(history_rows):
                    HistoryEntry.objects.create(
                        profile=p, entry_type='self', sort_order=i,
                        from_month=fm, from_year=fy,
                        to_month=tm, to_year=ty, is_present=present,
                        description=desc, location=loc,
                    )

                # Quá trình công tác
                work_rows = [
                    (9, 2003, 7, 2007, False, 'Đại học Kinh tế TP.HCM', 'Sinh viên', 'TP. Hồ Chí Minh'),
                    (9, 2007, 5, 2015, False, 'Trung tâm Phát triển Huyện Nhà Bè', 'Chuyên viên', 'Huyện Nhà Bè'),
                    (6, 2015, 3, 2019, False, 'Trung tâm Phát triển Huyện Nhà Bè', 'Phó Trưởng phòng', 'Huyện Nhà Bè'),
                    (4, 2019, None, None, True, 'Trung tâm Phát triển Quản lý Huyện Nhà Bè', 'Trưởng Phòng Kỹ thuật', 'Huyện Nhà Bè'),
                ]
                for i, (fm, fy, tm, ty, present, employer, job_title, loc) in enumerate(work_rows):
                    WorkHistory.objects.create(
                        profile=p, sort_order=i,
                        from_month=fm, from_year=fy,
                        to_month=tm, to_year=ty, is_present=present,
                        employer=employer, job_title=job_title, location=loc,
                    )

                # Quá trình học vấn
                edu_rows = [
                    (9, 2003, 7, 2007, False, 'Đại học Kinh tế TP.HCM', 'Quản lý công', 'Cử nhân'),
                    (3, 2018, 11, 2018, False, 'Trung tâm Bồi dưỡng Chính trị Huyện', 'Lý luận Mác-Lê-Nin và Tư tưởng HCM', 'Chứng chỉ'),
                    (9, 2021, 6, 2022, False, 'Học viện Chính trị Quốc phòng', 'Lý luận chính trị trung cấp', 'Chứng chỉ'),
                ]
                for i, (fm, fy, tm, ty, present, school, major, cert) in enumerate(edu_rows):
                    EducationHistory.objects.create(
                        profile=p, sort_order=i,
                        from_month=fm, from_year=fy,
                        to_month=tm, to_year=ty, is_present=present,
                        school=school, major=major, certificate=cert,
                    )

                # Khen thưởng
                awards = [
                    ('award', 2015, 'Huyện Nhà Bè', 'Cấp huyện', 'Khen thưởng xuất sắc hoàn thành nhiệm vụ'),
                    ('award', 2018, 'UBND Huyện Nhà Bè', 'Cấp huyện', 'Bằng khen của UBND Huyện Nhà Bè'),
                    ('award', 2020, 'Huyện Nhà Bè', 'Cấp huyện', 'Giải thưởng lao động xuất sắc'),
                ]
                for i, (atype, year, issuer, level, content) in enumerate(awards):
                    Award.objects.create(
                        profile=p, type=atype, sort_order=i,
                        issued_year=year, issuer=issuer,
                        level=level, content=content,
                    )
                self.stdout.write('  Timeline p10 ✓')

        self.stdout.write('  Timelines ✓')
