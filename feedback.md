2. Các hạng mục chưa đạt
A. Sơ lược
1. Mục Ngày vào Đoàn
🔴 Chưa đạt
Yêu cầu:
•	Định dạng dd/mm/yyyy
•	Có tùy chọn "Không"
Thực tế:
•	Đã đổi định dạng ngày
•	Chưa có tùy chọn "Không"
•	Người dùng chỉ có thể bỏ trống
________________________________________
2. Mục Ngày vào Đảng
🟡 Đạt một phần
Quần chúng: Đạt
Admin: Chưa đạt
Admin vẫn hiển thị định dạng:
YYYY-MM-DD
________________________________________
I. Thân nhân
1. Trạng thái Đảng viên
🔴 Chưa đạt
Dropdown hiện chỉ có:
•	Không phải Đảng viên
•	Có - Đảng viên
Thiếu:
-- Chọn --
hoặc giá trị rỗng.
________________________________________
2. Anh/Chị/Em ruột
🔴 Chưa đạt
Quần chúng
•	Có trường Quốc tịch
•	Chưa có địa chỉ cư trú theo đơn vị hành chính
Admin
•	Thiếu hoàn toàn trường Quốc tịch
________________________________________
3. Giao diện hiển thị
🔴 Chưa đạt
Các tiêu đề:
•	Cha ruột
•	Mẹ ruột
•	Vợ/Chồng
vẫn chưa được in đậm để phân nhóm dữ liệu rõ ràng.
________________________________________
Admin
1. Hiển thị địa chỉ hành chính
🔴 Chưa đạt
Trường:
Hometown ward
chỉ hiển thị tên xã/phường, không hiển thị kèm huyện và tỉnh.
________________________________________
2. Danh mục Trình độ phổ thông
🔴 Chưa đạt
Danh mục:
Tiểu học
vẫn còn tồn tại trong Master Data.
________________________________________
3. Dân tộc và Tôn giáo thân nhân
🔴 Chưa đạt
Hiện vẫn là ô nhập text tự do, chưa dùng danh mục chuẩn như giao diện Quần chúng.
________________________________________
4. Lịch sử thân nhân
🔴 Chưa đạt
Không hiển thị bảng lịch sử của:
•	Cha
•	Mẹ
•	Vợ/Chồng
trên giao diện quản trị.
________________________________________
II. DANH SÁCH LỖI NGHIÊM TRỌNG CẦN XỬ LÝ
🔥 BUG 01 - Crash chức năng Xuất Word
Mức độ
🚨 Blocker
Hiện tượng
Khi thực hiện:
Xuất Word Mẫu 2-KNĐ (hàng loạt)
hệ thống trả về lỗi:
ImportError: cannot import name 'build_lylich_docx'
from 'apps.exports.word_builder'
Phạm vi ảnh hưởng
•	Không thể xuất hồ sơ
•	Không thể nghiệm thu chức năng
Nguyên nhân nghi ngờ
Sai lệch giữa:
admin.py
và
word_builder.py
Đề xuất xử lý
•	Bổ sung hàm build_lylich_docx
hoặc
•	Đồng bộ lại câu lệnh import trong admin.py
________________________________________
🔥 BUG 02 - Không thể thêm Anh/Chị/Em thứ 4 trở lên
Mức độ
🚨 Blocker
Hiện tượng
Mục Anh/Chị/Em chỉ hiển thị:
•	3.1
•	3.2
•	3.3
Không có nút:
+ Thêm anh/chị/em
Hậu quả
Người có trên 3 anh/chị/em không thể kê khai đầy đủ.
Đề xuất xử lý
Bổ sung nút:
[ + Thêm anh/chị/em ]
và cơ chế thêm động tương tự các bảng lịch sử.
________________________________________
🔥 BUG 03 - Thiếu lịch sử thân nhân trên Admin
Mức độ
🟥 Nghiêm trọng
Hiện tượng
Admin không thể xem hoặc chỉnh sửa lịch sử hoạt động của thân nhân.
Đề xuất xử lý
Bổ sung:
class FamilyMemberHistoryInline(admin.TabularInline):
và khai báo vào:
FamilyMemberAdmin.inlines
