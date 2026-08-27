TÀI LIỆU HƯỚNG DẪN SỬ DỤNG
HỆ THỐNG QUẢN LÝ LÝ LỊCH ĐẢNG VIÊN

| | |
|---|---|
| **Tên tài liệu** | Tài liệu Hướng dẫn sử dụng |
| **Mã tài liệu** | HDSD_LYLICH |
| **Phiên bản** | 1.0 |
| **Dự án** | Hệ thống Quản lý Lý lịch Đảng viên |
| **Mã dự án** | LYLICH |

### BẢNG GHI NHẬN THAY ĐỔI

| Ngày thay đổi | Phiên bản | Mô tả thay đổi | Người lập |
|---|---|---|---|
| 28/07/2026 | 1.0 | Khởi tạo tài liệu — hướng dẫn đầy đủ 3 vai trò: Quản trị cấp cao, Ban Xây dựng Đảng, Quần chúng | |
| 28/07/2026 | 1.1 | Bổ sung đầy đủ các nhóm chức năng trang quản trị kỹ thuật (Django Admin) và trang Dashboard của Ban Xây dựng Đảng; thêm mục Danh sách chức năng ở đầu Phần III/IV; chuẩn hoá bố cục theo tài liệu mẫu | |
| | | | |

---

## MỤC LỤC

**PHẦN I. GIỚI THIỆU TỔNG QUAN**
1. Giới thiệu
2. Phạm vi tài liệu
3. Cách đọc tài liệu

**PHẦN II. GIỚI THIỆU CHUNG VỀ CHƯƠNG TRÌNH**
1. Mục đích của chương trình
2. Kết cấu chương trình — 3 vai trò sử dụng
3. Các thao tác chung khi sử dụng chương trình
   - 3.1. Đăng nhập vào hệ thống
   - 3.2. Các trạng thái hồ sơ (nhãn màu)
   - 3.3. Các nút thao tác thường gặp
   - 3.4. Thoát / Đăng xuất

**PHẦN III. HƯỚNG DẪN SỬ DỤNG — QUẢN TRỊ CẤP CAO (SUPERADMIN)**
1. Danh sách chức năng
2. Đăng nhập & vào trang quản trị kỹ thuật (Dashboard)
3. Quản lý người dùng
   - 3.1. Cán bộ Đảng — Tạo tài khoản cán bộ mới
   - 3.2. Phân quyền chức năng cho cán bộ
   - 3.3. Người dùng — sửa/khoá bất kỳ tài khoản nào
   - 3.4. Vai trò
   - 3.5. Lịch sử đăng nhập
4. Hồ sơ lý lịch (Hồ sơ · Thành viên gia đình · Lịch sử thẩm định · Yêu cầu bổ sung)
5. Xác minh
6. Thông báo
7. Báo cáo & Xuất
8. Danh mục
9. Thao tác chung: Thêm / Sửa / Xóa dữ liệu

**PHẦN IV. HƯỚNG DẪN SỬ DỤNG — BAN XÂY DỰNG ĐẢNG (CÁN BỘ)**
1. Danh sách chức năng
2. Đăng nhập hệ thống
3. Trang Dashboard
4. Đổi mật khẩu
5. Cấp tài khoản cho quần chúng
6. Danh sách hồ sơ (trang "Danh sách quần chúng") — tra cứu, xoá tài khoản
7. Thẩm định và phê duyệt hồ sơ
   - 7.1. Quy trình trạng thái hồ sơ
   - 7.2. Duyệt hồ sơ
   - 7.3. Góp ý và trả lại hồ sơ
   - 7.4. Xác nhận yêu cầu xác minh & Hoàn thiện hồ sơ
8. Xuất file Word (.docx)
9. Báo cáo & Thống kê
10. Thông báo

**PHẦN V. HƯỚNG DẪN SỬ DỤNG — QUẦN CHÚNG**
1. Đăng nhập lần đầu
2. Đổi mật khẩu
3. Kê khai hồ sơ lý lịch (Phần A–K)
4. Lưu nháp và Nộp hồ sơ
5. Xem góp ý và nộp lại khi hồ sơ bị trả

**PHẦN VI. PHỤ LỤC**
1. Bảng trạng thái hồ sơ đầy đủ
2. Câu hỏi thường gặp / xử lý lỗi

---

## PHẦN I. GIỚI THIỆU TỔNG QUAN

### 1. Giới thiệu

Tài liệu này hướng dẫn cách sử dụng **Hệ thống Quản lý Lý lịch Đảng viên** — phần mềm giúp quần chúng kê khai hồ sơ lý lịch điện tử, và giúp Ban Xây dựng Đảng tiếp nhận, thẩm định, phê duyệt hồ sơ và xuất file Word theo mẫu quy định.

### 2. Phạm vi tài liệu

Tài liệu áp dụng cho cả **3 vai trò** sử dụng hệ thống. Mỗi vai trò có 1 phần riêng (Phần III, IV, V) — **chỉ cần đọc đúng phần dành cho vai trò của mình**, không cần đọc hết toàn bộ tài liệu:

| Vai trò | Đọc phần |
|---|---|
| Quản trị cấp cao (Superadmin) | Phần I, II, **III** |
| Cán bộ / Quản trị viên Ban Xây dựng Đảng | Phần I, II, **IV** |
| Quần chúng (người kê khai hồ sơ) | Phần I, II, **V** |

> Muốn cài đặt phần mềm lên máy mới (chưa cài gì), xem file riêng `HUONG_DAN_CAI_WIN11.md`. Tài liệu này chỉ hướng dẫn **cách sử dụng** sau khi phần mềm đã chạy được.

### 3. Cách đọc tài liệu

Các ký hiệu dùng xuyên suốt tài liệu:

| Ký hiệu | Ý nghĩa |
|---|---|
| **Chữ in đậm** | Tên chính xác của nút bấm, tên trường nhập liệu, tên trang/tab hiển thị trên giao diện |
| `Chữ trong dấu ngoặc kép` | Nội dung/thông báo hiển thị nguyên văn trên màn hình |
| 📷 **Ảnh minh họa** | Vị trí cần chèn ảnh chụp màn hình thực tế (xem ghi chú trong khung) |
| ⚠️ **Lưu ý** | Điều cần đặc biệt chú ý, dễ gây nhầm lẫn hoặc sai sót |
| 💡 **Mẹo** | Gợi ý giúp thao tác nhanh, thuận tiện hơn |

---

## PHẦN II. GIỚI THIỆU CHUNG VỀ CHƯƠNG TRÌNH

### 1. Mục đích của chương trình

Hệ thống Quản lý Lý lịch Đảng viên được xây dựng nhằm số hoá quy trình kê khai — thẩm định — phê duyệt hồ sơ lý lịch của quần chúng xin vào Đảng, thay thế việc kê khai và luân chuyển hồ sơ giấy, đồng thời tự động tạo ra file Word theo đúng mẫu quy định (Mẫu 2-KNĐ) khi hồ sơ được hoàn thiện.

### 2. Kết cấu chương trình — 3 vai trò sử dụng

Chương trình phục vụ đồng thời 3 nhóm người dùng, mỗi nhóm có giao diện và quyền thao tác riêng biệt trên cùng 1 phần mềm:

| Vai trò | Là ai | Chức năng chính |
|---|---|---|
| **Quản trị cấp cao** (Superadmin) | Người quản lý kỹ thuật cao nhất, thường chỉ 1 người | Tạo/xoá tài khoản cán bộ Ban Xây dựng Đảng, phân quyền chi tiết |
| **Ban Xây dựng Đảng** (Cán bộ / Quản trị viên) | Cán bộ phụ trách công tác Đảng | Cấp tài khoản quần chúng, thẩm định/phê duyệt hồ sơ, xuất file Word, gửi thông báo, xem báo cáo — tuỳ quyền được cấp |
| **Quần chúng** | Người xin vào Đảng | Kê khai hồ sơ lý lịch của bản thân, nộp hồ sơ, theo dõi kết quả xét duyệt |

### 3. Các thao tác chung khi sử dụng chương trình

#### 3.1. Đăng nhập vào hệ thống

Cả 3 vai trò dùng **chung 1 màn hình đăng nhập** — hệ thống tự nhận diện vai trò và hiển thị đúng giao diện tương ứng ngay sau khi đăng nhập thành công.

**Các bước thực hiện:**

1. Mở trình duyệt, truy cập địa chỉ ứng dụng
2. Nhập **Số điện thoại** đã được cấp
3. Nhập **Mật khẩu**
4. Bấm nút **Đăng nhập**

> 📷 **Ảnh minh họa:** _(chèn ảnh màn hình popup "Đăng nhập hệ thống" — có ô Số điện thoại, ô Mật khẩu, nút Đăng nhập, và link "Đổi mật khẩu")_

⚠️ **Lưu ý:** nếu nhập sai mật khẩu **5 lần liên tiếp**, tài khoản sẽ tạm khoá — cần liên hệ cán bộ Ban Xây dựng Đảng (hoặc Quản trị cấp cao) để được mở lại.

#### 3.2. Các trạng thái hồ sơ (nhãn màu)

Trong các bảng danh sách, trạng thái hồ sơ được hiển thị bằng nhãn (pill) có màu để dễ phân biệt nhanh bằng mắt:

| Nhãn | Ý nghĩa |
|---|---|
| 🟡 Đang kê khai | Quần chúng chưa nộp, vẫn đang chỉnh sửa |
| 🔵 Đã nộp / Đang xem xét / Đang thẩm định | Đang trong quy trình xét duyệt nội bộ của Ban Xây dựng Đảng |
| 🔴 Trả lại | Bị yêu cầu bổ sung, đang chờ quần chúng sửa và nộp lại |
| 🟣 Đang xác minh | Đã phê duyệt, đang chờ xác minh lý lịch |
| 🟢 Hoàn thiện | Hồ sơ đã xong toàn bộ quy trình, có thể xuất Word |

(Xem bảng đầy đủ toàn bộ trạng thái tại **Phần VI.1**)

#### 3.3. Các nút thao tác thường gặp

| Nút | Ý nghĩa |
|---|---|
| **Lưu nháp** | Lưu tạm dữ liệu đang nhập dở, có thể thoát ra và vào lại sau |
| **📤 Nộp hồ sơ** | Gửi chính thức hồ sơ cho Ban Xây dựng Đảng xét duyệt |
| **✓ Duyệt** | Đẩy hồ sơ sang bước xét duyệt kế tiếp (cán bộ dùng) |
| **↩ Trả lại hồ sơ** | Yêu cầu quần chúng bổ sung/sửa lại (cán bộ dùng) |
| **Xem** | Mở xem chi tiết một hồ sơ/tài khoản |
| **Xóa** | Xoá vĩnh viễn — luôn có hộp thoại xác nhận trước khi xoá thật |

#### 3.4. Thoát / Đăng xuất

Bấm nút **Đăng xuất** ở cuối thanh điều hướng bên trái (sidebar) để thoát khỏi tài khoản hiện tại và quay về màn hình đăng nhập.

---

## PHẦN III. HƯỚNG DẪN SỬ DỤNG — QUẢN TRỊ CẤP CAO (SUPERADMIN)

Quản trị cấp cao thao tác trên trang **quản trị kỹ thuật (Django Admin)** — giao diện khác hẳn giao diện chính, dùng cho việc quản lý dữ liệu nền và tài khoản cán bộ, không dùng để tác nghiệp hàng ngày (việc tác nghiệp hàng ngày là của Ban Xây dựng Đảng ở **Phần IV**).

### 1. Danh sách chức năng

Toàn bộ mục quản trị được chia thành các **nhóm** hiển thị ở thanh bên trái trang quản trị kỹ thuật:

| Nhóm | Mục | Thêm/Sửa được? | Mô tả |
|---|---|---|---|
| Tổng quan | Dashboard | — | Trang chủ quản trị, xem "Hoạt động gần đây" |
| Quản lý người dùng | Cán bộ Đảng | ✅ Thêm/Sửa/Xoá | Tạo tài khoản & phân quyền cán bộ Ban Xây dựng Đảng |
| | Người dùng | ✅ Sửa/Khoá | Xem/sửa **mọi** tài khoản trong hệ thống (cả quần chúng) |
| | Vai trò | ✅ Xem/Sửa | Danh sách vai trò hệ thống (admin / can_bo_bxd / quan_chung) |
| | Lịch sử đăng nhập | 🔒 Chỉ xem | Tra cứu lịch sử đăng nhập thành công/thất bại |
| Hồ sơ lý lịch | Hồ sơ | ✅ Sửa/Xoá | Toàn bộ hồ sơ lý lịch quần chúng đã kê khai |
| | Thành viên gia đình | ✅ Sửa/Xoá | Dữ liệu thân nhân trong Phần I của từng hồ sơ |
| | Lịch sử thẩm định | 🔒 Chỉ xem | Nhật ký duyệt/trả lại từng hồ sơ |
| | Yêu cầu bổ sung | ✅ Sửa/Xoá | Các lần trả hồ sơ yêu cầu bổ sung |
| Xác minh | Yêu cầu xác minh | ✅ Sửa/Xoá | Yêu cầu xác minh lý lịch gửi đi |
| Thông báo | Thông báo | ✅ Sửa/Xoá | Thông báo đã gửi cho quần chúng |
| | Mẫu thông báo | ✅ Thêm/Sửa/Xoá | Các mẫu nội dung thông báo dựng sẵn |
| Báo cáo & Xuất | Xuất Word | 🔒 Chỉ xem | Nhật ký các lần xuất file Word |
| | Xuất báo cáo | 🔒 Chỉ xem | Nhật ký các lần xuất báo cáo |
| Danh mục | Dân tộc / Tôn giáo / Đơn vị hành chính | ✅ Thêm/Sửa/Xoá | Danh mục dữ liệu dùng chung trong các form kê khai |

💡 **Mẹo:** ngoài các nhóm trên, bấm **"Tất cả ứng dụng"** (góc trên bên trái) sẽ thấy thêm vài mục kỹ thuật ít dùng tới (Trình độ chính trị, Trình độ học vấn, File đã tải lên, Nhật ký hoạt động, Celery Results…) — đây là các bảng dữ liệu hệ thống tự sinh ra, thường **không cần** thao tác trực tiếp trừ khi được hướng dẫn cụ thể.

### 2. Đăng nhập & vào trang quản trị kỹ thuật (Dashboard)

**Mục đích:** truy cập trang quản trị kỹ thuật để quản lý tài khoản cán bộ, dữ liệu hồ sơ và danh mục dùng chung.

**Các bước thực hiện:**

1. Đăng nhập như hướng dẫn ở **Phần II.3.1** bằng tài khoản Superadmin
2. Vì đây là tài khoản quản trị cấp cao, hệ thống **không** vào thẳng giao diện chính mà hiện lại màn đăng nhập, kèm 1 khung thông báo phía trên: **"Đang có phiên đăng nhập: {tên bạn}"**
3. Bấm nút **⚙ Vào Django Admin** trong khung đó

> 📷 **Ảnh minh họa:** _(chèn ảnh khung thông báo "Đang có phiên đăng nhập" với nút "⚙ Vào Django Admin")_

Hệ thống chuyển sang trang **Dashboard** của trang quản trị kỹ thuật, gồm:
- Thanh bên trái: các nhóm mục đã liệt kê ở mục 1
- Khối **"Hoạt động gần đây"**: 10 thao tác gần nhất mà chính tài khoản đang đăng nhập đã thực hiện trên trang quản trị (thêm/sửa/xoá bản ghi nào, lúc nào)
- Phần nội dung chính: danh sách các nhóm ứng dụng kỹ thuật khác (Báo cáo, Celery Results, Danh mục dùng chung, File tài liệu…) — xem 💡 Mẹo ở mục 1

> 📷 **Ảnh minh họa:** _(chèn ảnh trang Dashboard Django Admin đầy đủ, thấy rõ sidebar + khối "Hoạt động gần đây")_

### 3. Quản lý người dùng

#### 3.1. Cán bộ Đảng — Tạo tài khoản cán bộ mới

**Mục đích:** cấp tài khoản đăng nhập mới cho một cán bộ Ban Xây dựng Đảng.

**Các bước thực hiện:**

1. Ở thanh bên trái, nhóm **"Quản lý người dùng"** → bấm **"Cán bộ Đảng"** → bấm **"ADD"** (Thêm)
2. Điền các thông tin cơ bản:
   - **Họ và tên**
   - **Số điện thoại** (dùng để đăng nhập, không được trùng tài khoản đã có)
   - **Email**
   - **Vai trò**: chọn `admin` (Quản trị viên — toàn quyền mặc định) hoặc `can_bo_bxd` (Cán bộ Ban Xây dựng Đảng thường — cần phân quyền chi tiết ở mục 3.2)
   - **Mật khẩu** ban đầu

> 📷 **Ảnh minh họa:** _(chèn ảnh form "Thêm Cán bộ Đảng" với đầy đủ các trường trên)_

3. Bấm **"Save"** ở cuối trang để lưu

#### 3.2. Phân quyền chức năng cho cán bộ

**Mục đích:** giới hạn đúng phạm vi chức năng mà từng cán bộ được phép thao tác.

**Các bước thực hiện:**

1. Ở màn hình tạo/sửa cán bộ (mục 3.1 ở trên), kéo xuống phần **"Phân quyền chức năng"**
2. Tick chọn đúng những quyền muốn cấp:

| Ô tick | Cán bộ được phép |
|---|---|
| Cấp tài khoản quần chúng | Tạo tài khoản mới cho quần chúng |
| Xem & trả lại hồ sơ | Xem hồ sơ, góp ý và trả lại yêu cầu bổ sung |
| Phê duyệt hồ sơ | Duyệt hồ sơ qua các bước xét duyệt |
| Xuất file Word | Xuất hồ sơ đã hoàn thiện ra file .docx |
| Gửi thông báo | Gửi nhắc nhở/thông báo cho quần chúng |
| Xem báo cáo | Xem thống kê, xuất báo cáo Excel |

> 📷 **Ảnh minh họa:** _(chèn ảnh khối "Phân quyền chức năng" với 6 ô tick)_

3. Bấm **"Save"**

⚠️ **Lưu ý:** không tick quyền nào thì cán bộ đăng nhập vào vẫn thấy giao diện nhưng các chức năng tương ứng sẽ tự ẩn/khoá, không thao tác được.

💡 **Mẹo:** vai trò `admin` mặc định có đủ toàn bộ 6 quyền dù không tick — chỉ cần phân quyền chi tiết cho vai trò `can_bo_bxd`.

#### 3.3. Người dùng — sửa/khoá bất kỳ tài khoản nào

**Mục đích:** đây là danh sách **toàn bộ** tài khoản trong hệ thống (cả cán bộ lẫn quần chúng) — dùng khi cần tra cứu/sửa thông tin hoặc khoá 1 tài khoản bất kỳ mà không qua các bước nghiệp vụ thông thường.

**Các bước thực hiện:**

1. Nhóm **"Quản lý người dùng"** → bấm **"Người dùng"**
2. Bấm vào đúng tên trong danh sách để mở
3. Sửa thông tin cần thiết (ví dụ đổi **Trạng thái** sang "Bị khóa" để khoá tài khoản ngay lập tức) → bấm **"Save"**

⚠️ **Lưu ý:** đây là thao tác kỹ thuật cấp cao, tác động trực tiếp lên dữ liệu — với tài khoản quần chúng, ưu tiên dùng chức năng **Xóa** ở giao diện Ban Xây dựng Đảng (**Phần IV.6**) thay vì sửa tay ở đây, trừ khi cần xử lý trường hợp đặc biệt.

#### 3.4. Vai trò

Danh sách 3 vai trò cố định của hệ thống: `admin`, `can_bo_bxd`, `quan_chung`. Hiếm khi cần thêm/sửa — chỉ tham khảo khi cần kiểm tra tên/mã vai trò.

#### 3.5. Lịch sử đăng nhập

🔒 Chỉ xem, không sửa/xoá được. Dùng để tra cứu khi cần kiểm tra ai đã đăng nhập, đăng nhập thành công hay thất bại, vào lúc nào — hữu ích khi hỗ trợ người dùng báo không đăng nhập được.

### 4. Hồ sơ lý lịch

Nhóm này chứa dữ liệu hồ sơ ở dạng bảng kỹ thuật (khác với giao diện xem hồ sơ trực quan theo Phần A–K bên giao diện chính) — chủ yếu dùng để tra cứu/sửa chữa dữ liệu khi cần hỗ trợ kỹ thuật:

| Mục | Nội dung |
|---|---|
| **Hồ sơ** | Toàn bộ hồ sơ lý lịch đã kê khai — có thao tác hàng loạt **"Xuất Word Mẫu 2-KNĐ (hàng loạt)"** khi chọn nhiều hồ sơ cùng lúc |
| **Thành viên gia đình** | Dữ liệu từng thành viên gia đình (Phần I) của mọi hồ sơ |
| **Lịch sử thẩm định** 🔒 | Nhật ký duyệt/trả lại từng hồ sơ (chỉ xem) |
| **Yêu cầu bổ sung** | Chi tiết từng lần trả hồ sơ yêu cầu bổ sung, gồm các mục đã yêu cầu |

Cách xuất Word hàng loạt: vào **Hồ sơ** → tick chọn nhiều hồ sơ ở đầu mỗi dòng → chọn hành động **"Xuất Word Mẫu 2-KNĐ (hàng loạt)"** ở ô thả xuống phía trên bảng → bấm **"Go"**.

### 5. Xác minh

Mục **"Yêu cầu xác minh"** — danh sách các yêu cầu xác minh lý lịch đã gửi đi (tương ứng thao tác **"Xác nhận YC"** bên giao diện Ban Xây dựng Đảng, xem **Phần IV.7.4**), dùng để tra cứu/chỉnh sửa khi cần.

### 6. Thông báo

| Mục | Nội dung |
|---|---|
| **Thông báo** | Toàn bộ thông báo đã gửi tới quần chúng |
| **Mẫu thông báo** | Các mẫu nội dung dựng sẵn để cán bộ chọn nhanh khi gửi thông báo |

### 7. Báo cáo & Xuất

🔒 Cả 2 mục đều chỉ xem (nhật ký hệ thống tự ghi lại, không sửa/xoá):

| Mục | Nội dung |
|---|---|
| **Xuất Word** | Nhật ký mọi lần xuất file Word — ai xuất, xuất hồ sơ nào, lúc nào |
| **Xuất báo cáo** | Nhật ký mọi lần xuất báo cáo Excel |

### 8. Danh mục

Danh mục dữ liệu dùng chung, hiển thị dạng lựa chọn (dropdown) trong các form kê khai của quần chúng:

| Mục | Dùng ở đâu |
|---|---|
| **Dân tộc** | Ô "Dân tộc" trong Phần A và Phần I (thành viên gia đình) |
| **Tôn giáo** | Ô "Tôn giáo" trong Phần A và Phần I |
| **Đơn vị hành chính** | Dữ liệu Tỉnh/Thành → Xã/Phường dùng cho các ô địa chỉ |

💡 Ngoài ra còn **Trình độ chính trị** và **Trình độ học vấn** (dùng cho Mục 11 Phần A) — 2 mục này chưa được gắn vào menu chính, truy cập qua **"Tất cả ứng dụng"** (xem 💡 Mẹo ở mục 1).

### 9. Thao tác chung: Thêm / Sửa / Xóa dữ liệu

Toàn bộ các mục quản lý có đánh dấu ✅ ở bảng mục 1 đều thao tác theo đúng 1 khuôn mẫu chung sau (chuẩn Django Admin):

**Thêm mới:**
1. Mở đúng mục cần thêm (ví dụ: Dân tộc) → bấm nút **"ADD [tên mục]"** ở góc trên bên phải
2. Điền các trường trong form hiện ra
3. Bấm **"SAVE"** (lưu và thoát) hoặc **"Save and add another"** (lưu và thêm tiếp bản ghi mới) hoặc **"Save and continue editing"** (lưu nhưng ở lại màn sửa)

**Sửa:**
1. Ở danh sách, bấm trực tiếp vào tên/dòng bản ghi cần sửa
2. Sửa nội dung trong form → bấm **"SAVE"**

**Xóa:**
- Xóa 1 bản ghi: mở bản ghi đó → kéo xuống cuối trang, bấm **"Delete"** (màu đỏ) → xác nhận ở trang cảnh báo tiếp theo
- Xóa nhiều bản ghi cùng lúc: ở trang danh sách, tick chọn các dòng cần xóa → chọn hành động **"Delete selected [tên mục]"** ở ô thả xuống phía trên bảng → bấm **"Go"** → xác nhận

> 📷 **Ảnh minh họa:** _(chèn ảnh 1 trang danh sách Django Admin bất kỳ, khoanh vùng nút "ADD", ô tick chọn dòng, và ô thả xuống hành động)_

⚠️ **Lưu ý:** các mục đánh dấu 🔒 (chỉ xem) ở bảng mục 1 sẽ **không có** nút "ADD" hoặc "Delete" — đây là nhật ký hệ thống tự ghi lại, không chỉnh sửa tay được.

---

## PHẦN IV. HƯỚNG DẪN SỬ DỤNG — BAN XÂY DỰNG ĐẢNG (CÁN BỘ)

### 1. Danh sách chức năng

Toàn bộ chức năng của Ban Xây dựng Đảng nằm trên **1 giao diện duy nhất** (khác với Superadmin phải qua trang quản trị kỹ thuật riêng), truy cập qua thanh điều hướng bên trái:

| Mục sidebar | Tên trang khi mở ra | Cần quyền gì | Mô tả |
|---|---|---|---|
| Dashboard | "Tổng quan hồ sơ quần chúng" | Không cần quyền riêng | Trang chủ — xem nhanh số liệu tổng quan (mục 3) |
| Danh sách hồ sơ | "Danh sách quần chúng" | Không cần quyền riêng | Tra cứu tài khoản, xoá tài khoản quần chúng (mục 6) |
| Xác minh lý lịch | "Theo dõi xác minh lý lịch" | Xem & trả lại hồ sơ / Phê duyệt hồ sơ | Thẩm định, duyệt, trả lại, xuất Word (mục 7–8) |
| Thông báo | "Trung tâm thông báo" | Gửi thông báo | Gửi/quản lý thông báo cho quần chúng (mục 10) |
| Cấp tài khoản | "Cấp tài khoản cho quần chúng" | Cấp tài khoản quần chúng | Tạo tài khoản mới cho quần chúng (mục 5) |
| Báo cáo & Thống kê | "Báo cáo & Thống kê" | Xem báo cáo | Xuất báo cáo tổng hợp theo tháng/năm (mục 9) |

⚠️ **Lưu ý:** tên gọi ngoài sidebar và tiêu đề của trang khi mở ra **không phải lúc nào cũng giống hệt nhau** (ví dụ sidebar ghi "Danh sách hồ sơ" nhưng trang mở ra tiêu đề lại là "Danh sách quần chúng") — đây là 2 cách gọi cho cùng 1 trang, không phải 2 trang khác nhau. Tài liệu này dùng tên trang (cột thứ 2) khi mô tả chi tiết từng chức năng.

### 2. Đăng nhập hệ thống

Thực hiện như **Phần II.3.1**, dùng Số điện thoại + Mật khẩu do Quản trị cấp cao cấp (**Phần III.3.1**). Sau khi đăng nhập thành công, hệ thống hiển thị giao diện Ban Xây dựng Đảng với thanh điều hướng bên trái gồm các mục đã liệt kê ở mục 1 (chỉ hiện đúng những mục tương ứng với quyền đã được cấp).

> 📷 **Ảnh minh họa:** _(chèn ảnh giao diện chính sau khi đăng nhập, thấy rõ thanh sidebar điều hướng)_

### 3. Trang Dashboard

**Mục đích:** xem nhanh tình hình xử lý hồ sơ toàn hệ thống ngay khi vừa đăng nhập.

Trang **"Tổng quan hồ sơ quần chúng"** (mục **Dashboard** ở sidebar) gồm 4 khối:

**a) 5 thẻ số liệu (KPI):**

| Thẻ | Ý nghĩa |
|---|---|
| 📋 Chờ thẩm định | Số hồ sơ đang cần cán bộ thẩm định |
| ✏️ Đang kê khai | Số hồ sơ quần chúng đang điền dở, chưa nộp |
| ⚠️ Yêu cầu bổ sung | Số hồ sơ đang chờ quần chúng bổ sung sau khi bị trả lại |
| ✅ Hoàn thiện | Số hồ sơ đã xong toàn bộ quy trình |
| 👥 Tổng quần chúng | Tổng số tài khoản quần chúng đang được theo dõi |

> 📷 **Ảnh minh họa:** _(chèn ảnh 5 thẻ số liệu ở đầu trang Dashboard)_

**b) Hoạt động gần đây:** danh sách các thao tác xét duyệt mới nhất trên toàn hệ thống (Đã nộp, Trả lại, Đã phê duyệt, Hoàn thiện…), kèm tên cán bộ thực hiện và thời gian.

**c) Phân bổ trạng thái:** biểu đồ tròn thể hiện tỉ lệ hồ sơ theo 4 trạng thái chính (Đang kê khai / Chờ thẩm định / Yêu cầu bổ sung / Hoàn thiện) — giúp nhìn nhanh khối lượng công việc còn tồn.

> 📷 **Ảnh minh họa:** _(chèn ảnh khối "Hoạt động gần đây" và biểu đồ "Phân bổ trạng thái")_

**d) 2 nút thao tác nhanh** ở đầu trang:
- **"Xuất Excel"**: tải ngay danh sách quần chúng ra file `.xlsx`
- **"+ Cấp tài khoản"**: đi thẳng tới trang Cấp tài khoản (mục 5)

### 4. Đổi mật khẩu

**Mục đích:** thay đổi mật khẩu đăng nhập, nên làm ngay sau khi nhận tài khoản lần đầu.

**Các bước thực hiện:**

1. Ở màn hình đăng nhập, bấm link **"Đổi mật khẩu"**
2. Nhập **Số điện thoại**, **Mật khẩu hiện tại**, **Mật khẩu mới** (tối thiểu 8 ký tự), **Nhập lại mật khẩu mới**
3. Bấm **"Đổi mật khẩu"**

> 📷 **Ảnh minh họa:** _(chèn ảnh popup "Đổi mật khẩu")_

Hệ thống báo **"✅ Đã đổi mật khẩu thành công"** và tự đăng xuất — đăng nhập lại bằng mật khẩu mới.

### 5. Cấp tài khoản cho quần chúng

**Mục đích:** tạo tài khoản kê khai điện tử cho một quần chúng, hệ thống tự gửi thông tin đăng nhập qua Gmail.

⚠️ Chỉ cán bộ có quyền **"Cấp tài khoản quần chúng"** mới thấy được tab này.

**Các bước thực hiện:**

1. Bấm mục **"Cấp tài khoản"** ở sidebar → vào trang **"Cấp tài khoản cho quần chúng"**

> 📷 **Ảnh minh họa:** _(chèn ảnh trang "Cấp tài khoản cho quần chúng" — Bước 1)_

2. **Bước 1 – Thông tin tài khoản**: điền đầy đủ **Họ và tên**, **Số CCCD** (12 số), **Ngày sinh**, **Số điện thoại**, **Email Gmail** (bắt buộc), và 2 ô tự nhập **Chi bộ** / **Đảng bộ** (không bắt buộc, có thể bổ sung sau) → bấm **"Tiếp theo →"**
3. **Bước 2 – Xác nhận**: kiểm tra lại toàn bộ thông tin vừa nhập

> 📷 **Ảnh minh họa:** _(chèn ảnh trang "Cấp tài khoản cho quần chúng" — Bước 2 Xác nhận)_

4. Bấm **"✓ Xác nhận & Cấp tài khoản"**

Hệ thống tự sinh mật khẩu ngẫu nhiên và gửi 1 email tới Gmail vừa nhập, gồm **số điện thoại đăng nhập** + **mật khẩu khởi tạo**.

⚠️ **Lưu ý:**
- Số CCCD và Số điện thoại phải **duy nhất** trong toàn hệ thống, không được trùng tài khoản đã có.
- Nếu quần chúng cung cấp sai CCCD/SĐT lúc tạo lần đầu, muốn tạo lại thì **phải xoá tài khoản sai đó trước** (xem mục 6 bên dưới) rồi mới cấp tài khoản lại từ đầu.

### 6. Danh sách hồ sơ (trang "Danh sách quần chúng") — tra cứu, xoá tài khoản

**Mục đích:** tra cứu toàn bộ tài khoản quần chúng trong hệ thống, và xoá bỏ những tài khoản không còn cần thiết mà không phải nhờ Quản trị cấp cao.

**Các bước thực hiện:**

1. Bấm mục **"Danh sách hồ sơ"** ở sidebar → vào trang **"Danh sách quần chúng"**
2. Dùng ô tìm kiếm (theo họ tên/SĐT/CCCD) hoặc bộ lọc trạng thái tài khoản để tìm đúng người

> 📷 **Ảnh minh họa:** _(chèn ảnh trang "Danh sách quần chúng" với bảng danh sách và 2 nút Xem/Xóa)_

3. Bấm **"Xem"** để xem nhanh thông tin tài khoản, hoặc bấm **"Xóa"** để xoá vĩnh viễn

⚠️ **Lưu ý:** nút **"Xóa"** sẽ xoá **vĩnh viễn, không khôi phục được** — xoá luôn cả tài khoản đăng nhập, hồ sơ, file đính kèm, lịch sử xét duyệt của người đó. Hệ thống yêu cầu xác nhận 2 lần trước khi xoá thật.

> ⚠️ Trang **"Danh sách quần chúng"** chỉ dùng để tra cứu/xoá tài khoản, **không phải** nơi thẩm định hồ sơ — việc thẩm định thực hiện ở mục 7 bên dưới (trang **"Xác minh lý lịch"**).

### 7. Thẩm định và phê duyệt hồ sơ

#### 7.1. Quy trình trạng thái hồ sơ

```
Đang kê khai → Đã nộp → Đang xem xét → Đang thẩm định → Đã phê duyệt
                                                              ↓
                                                        Đang xác minh
                                                              ↓
                                                          Hoàn thiện
```

Ở bất kỳ bước nào (trước khi Hoàn thiện), cán bộ cũng có thể **Trả lại** hồ sơ để quần chúng bổ sung; sau khi quần chúng nộp lại, hồ sơ quay về trạng thái **Đã nộp** và đi tiếp bình thường.

**Vào đúng trang:** bấm mục **"Xác minh lý lịch"** ở sidebar → trang **"Theo dõi xác minh lý lịch"**.

> 📷 **Ảnh minh họa:** _(chèn ảnh trang "Theo dõi xác minh lý lịch" — bảng danh sách hồ sơ)_

Các nút thao tác trên từng hồ sơ:

| Nút | Khi nào xuất hiện | Tác dụng |
|---|---|---|
| **Xem** | Luôn có | Mở chi tiết hồ sơ để đọc/chỉnh sửa, thẩm định |
| **✓ Duyệt** | Đã nộp / Đang xem xét / Đang thẩm định | Đẩy hồ sơ sang bước kế tiếp |
| **↩** (Trả lại hồ sơ) | Hầu hết các trạng thái trước Hoàn thiện | Trả về cho quần chúng yêu cầu sửa/bổ sung |
| **Xác nhận YC** | Đã phê duyệt | Xác nhận yêu cầu xác minh lý lịch, chuyển sang Đang xác minh |
| **Hoàn thiện** | Đang xác minh | Đánh dấu hồ sơ Hoàn thiện — mở khoá xuất Word |
| **📄 Xuất** | Hoàn thiện, cán bộ có quyền Xuất file Word | Tải file Word (.docx) — xem mục 8 |

#### 7.2. Duyệt hồ sơ

**Các bước thực hiện:**

1. Ở trang "Theo dõi xác minh lý lịch", tìm đúng hồ sơ
2. Bấm **"✓ Duyệt"**

⚠️ **Lưu ý quan trọng:** phải bấm **"✓ Duyệt" 3 lần liên tiếp** để hồ sơ đi hết 3 bước nội bộ (Đã nộp → Đang xem xét → Đang thẩm định → Đã phê duyệt) — đây là thiết kế có chủ đích để xác nhận từng bước xét duyệt, **không phải lỗi phần mềm**. Nút vẫn chỉ hiện chữ "Duyệt" ở mỗi lần bấm, chỉ có trạng thái ở cột bên cạnh thay đổi sau mỗi lần.

#### 7.3. Góp ý và trả lại hồ sơ

**Các bước thực hiện:**

1. Bấm **"Xem"** để mở hồ sơ ở **Chế độ thẩm định** (dữ liệu hiển thị dạng chỉ đọc)

> 📷 **Ảnh minh họa:** _(chèn ảnh trang thẩm định hồ sơ, chế độ chỉ đọc)_

2. Ở mỗi phần A–K, có sẵn 1 ô **"💬 Góp ý chung cho phần này…"** — gõ nội dung nhận xét/yêu cầu sửa cho phần đó
3. Bấm **"💾 Lưu nhận xét"** để lưu các góp ý vừa gõ

> 📷 **Ảnh minh họa:** _(chèn ảnh ô "Góp ý chung" tại 1 phần cụ thể)_

4. Bấm **"↩ Trả lại hồ sơ"** → hộp thoại **"Trả lại hồ sơ — Yêu cầu bổ sung"** hiện ra:
   - Chọn (tick) các phần cần quần chúng bổ sung (A, B, C…)
   - Bắt buộc gõ **"Ghi chú gửi kèm cho Quần chúng"** (tóm tắt lý do trả lại)
   - Tuỳ chọn tick gửi kèm **Zalo OA** và/hoặc **SMS** báo ngay cho quần chúng
   - Bấm **"↩ Xác nhận trả lại hồ sơ"**

> 📷 **Ảnh minh họa:** _(chèn ảnh hộp thoại "Trả lại hồ sơ — Yêu cầu bổ sung")_

Quần chúng sẽ thấy đúng góp ý đó hiện ở đúng phần tương ứng khi đăng nhập lại (xem **Phần V.5**).

💡 **Mẹo:** ngoài "Góp ý chung" (quần chúng nhìn thấy được), mỗi hồ sơ còn có ô **"Ghi chú nội bộ (chỉ cán bộ Ban Xây dựng Đảng xem)"** để ghi chú riêng — quần chúng không nhìn thấy ô này.

#### 7.4. Xác nhận yêu cầu xác minh & Hoàn thiện hồ sơ

**Các bước thực hiện:**

1. Khi hồ sơ ở trạng thái **Đã phê duyệt**, bấm **"Xác nhận YC"** → nhập nội dung xác minh và thời hạn → xác nhận. Hồ sơ chuyển sang **Đang xác minh**.
2. Sau khi xác minh xong (ngoài hệ thống), quay lại tìm đúng hồ sơ, bấm **"Hoàn thiện"** → xác nhận hộp thoại *"Xác nhận hoàn thiện hồ sơ {tên}?"*. Hồ sơ chuyển sang **Hoàn thiện** — lúc này mới xuất được file Word (mục 8).

### 8. Xuất file Word (.docx)

**Mục đích:** xuất hồ sơ đã hoàn thiện ra file Word theo đúng mẫu quy định (Mẫu 2-KNĐ).

⚠️ Chỉ áp dụng cho hồ sơ đã ở trạng thái **Hoàn thiện**, và cán bộ phải có quyền **"Xuất file Word"**.

**Các bước thực hiện:**

1. Ở trang **"Theo dõi xác minh lý lịch"**, tìm đúng hồ sơ đang ở trạng thái **Hoàn thiện** — cột **"Xuất Word"** sẽ hiện nút **"📄 Xuất"** (hồ sơ chưa Hoàn thiện thì cột này chỉ ghi "Chưa đủ điều kiện", không bấm được)

> 📷 **Ảnh minh họa:** _(chèn ảnh cột "Xuất Word" với nút "📄 Xuất")_

2. Bấm **"📄 Xuất"** → hệ thống báo **"⏳ Đang tạo file Word…"** rồi tự tải file `.docx` về máy
3. Thấy thông báo **"✓ Đã xuất Word thành công"** là xong — mở file vừa tải trong thư mục **Downloads** của trình duyệt

### 9. Báo cáo & Thống kê

⚠️ Cần quyền **"Xem báo cáo"**.

**Các bước thực hiện:**

1. Trang **"Dashboard"** hoặc **"Danh sách quần chúng"** đều có nút **"↓ Xuất Excel"** để xuất nhanh danh sách đang xem
2. Bấm mục **"Báo cáo & Thống kê"** ở sidebar để vào trang báo cáo riêng, chọn tháng/năm cần xuất → xuất báo cáo tổng hợp tình hình xử lý hồ sơ theo kỳ

> 📷 **Ảnh minh họa:** _(chèn ảnh trang "Báo cáo & Thống kê")_

### 10. Thông báo

⚠️ Cần quyền **"Gửi thông báo"**.

**Mục đích:** nhắc quần chúng chưa nộp hồ sơ, hồ sơ bị trả lại chưa cập nhật, hoặc tài khoản mới chưa đăng nhập lần nào.

**Các bước thực hiện:**

1. Bấm mục **"Thông báo"** ở sidebar → vào trang **"Trung tâm thông báo"**
2. Gửi cho từng người, hoặc chọn nhóm (theo tình trạng hồ sơ) để gửi hàng loạt cùng lúc

> 📷 **Ảnh minh họa:** _(chèn ảnh trang "Trung tâm thông báo")_

---

## PHẦN V. HƯỚNG DẪN SỬ DỤNG — QUẦN CHÚNG

### 1. Đăng nhập lần đầu

Thực hiện như **Phần II.3.1**, dùng **Số điện thoại** + **mật khẩu khởi tạo** nhận được qua Gmail (do cán bộ Ban Xây dựng Đảng cấp — xem Phần IV.5).

> 📷 **Ảnh minh họa:** _(chèn ảnh email nhận được, có số điện thoại + mật khẩu khởi tạo)_

💡 **Mẹo:** không thấy email, kiểm tra thêm mục Spam/Quảng cáo của Gmail.

### 2. Đổi mật khẩu

Nên đổi mật khẩu ngay sau lần đăng nhập đầu tiên — thực hiện đúng như **Phần IV.4** (bấm **"Đổi mật khẩu"** ở màn đăng nhập).

### 3. Kê khai hồ sơ lý lịch (Phần A–K)

Sau khi đăng nhập, ở thanh bên trái (sidebar) sẽ thấy 11 phần cần kê khai, chia thành 4 nhóm:

| Nhóm | Các phần |
|---|---|
| Thông tin cá nhân | A. Sơ lược lý lịch · B. Lịch sử bản thân · C. Những công việc, chức vụ đã qua · D. Đặc điểm lịch sử chính trị |
| Học vấn & Thành tích | E. Những lớp đào tạo, bồi dưỡng đã qua · F. Đi nước ngoài · G. Khen thưởng · H. Kỷ luật |
| Gia đình | I. Hoàn cảnh gia đình |
| Hoàn thiện hồ sơ | J. Tự nhận xét · K. Cam đoan, Ký tên & Nộp hồ sơ |

> 📷 **Ảnh minh họa:** _(chèn ảnh sidebar với đầy đủ danh sách các phần A–K)_

**Các bước thực hiện:**

1. Bấm lần lượt từng phần ở sidebar để điền — không bắt buộc điền theo đúng thứ tự
2. Hệ thống **tự lưu và hiện lại** dữ liệu đã nhập khi quay lại phần đó

> 📷 **Ảnh minh họa:** _(chèn ảnh 1 phần đang điền, ví dụ Phần A. Sơ lược lý lịch)_

⚠️ **Lưu ý riêng cho Phần I (Hoàn cảnh gia đình):** khi thêm thành viên gia đình, ô **"Nghề nghiệp"** nếu người đó không có nghề nghiệp thì phải ghi rõ **"Không"**, không được để trống.

### 4. Lưu nháp và Nộp hồ sơ

**Lưu nháp** (có thể làm bất cứ lúc nào):

1. Bấm **"Lưu nháp"** để lưu tạm và thoát ra — lần sau đăng nhập lại điền tiếp bình thường, không mất dữ liệu

**Nộp hồ sơ** (khi đã điền xong hết 11 phần):

1. Vào Phần K (Cam đoan & Nộp), đọc mục **"Kết quả kiểm tra tự động (AI)"** để xem hệ thống có phát hiện thiếu sót gì không

> 📷 **Ảnh minh họa:** _(chèn ảnh Phần K với khối "Kết quả kiểm tra tự động (AI)")_

2. Tick vào ô **cam đoan**
3. Bấm **"📤 Nộp hồ sơ"**

Nếu còn thiếu thông tin bắt buộc (họ tên/ngày sinh/giới tính, phần chưa điền, quá trình lịch sử/công tác bị đứt quãng…), hệ thống sẽ báo rõ chỗ còn thiếu, chưa cho nộp cho tới khi bổ sung đủ.

Nộp thành công sẽ thấy thông báo: **"✅ Hồ sơ đã nộp thành công! Cán bộ sẽ liên hệ trong 3–5 ngày làm việc."** — hồ sơ chuyển sang trạng thái **"Đã nộp"**, chờ Ban Xây dựng Đảng xử lý.

### 5. Xem góp ý và nộp lại khi hồ sơ bị trả

Nếu hồ sơ bị cán bộ trả lại để yêu cầu bổ sung, đăng nhập lại sẽ thấy khung **"💬 Góp ý chung"** màu nổi bật ngay trên đúng phần bị yêu cầu bổ sung.

> 📷 **Ảnh minh họa:** _(chèn ảnh khung "Góp ý chung" hiển thị trên 1 phần của form)_

**Các bước thực hiện:**

1. Đọc kỹ nội dung góp ý
2. Sửa đúng theo góp ý ở phần được đánh dấu
3. Nộp lại hồ sơ như mục 4 ở trên (Tick cam đoan → **"📤 Nộp hồ sơ"**)

Khung góp ý sẽ **tự biến mất** sau khi nộp lại thành công.

---

## PHẦN VI. PHỤ LỤC

### 1. Bảng trạng thái hồ sơ đầy đủ

| Trạng thái | Ý nghĩa |
|---|---|
| Đang kê khai | Quần chúng đang điền, chưa nộp |
| Đã nộp | Vừa nộp, chờ cán bộ xử lý |
| Đang xem xét | Bước xét duyệt nội bộ thứ 1 |
| Đang thẩm định | Bước xét duyệt nội bộ thứ 2 |
| Trả lại | Bị yêu cầu bổ sung, chờ quần chúng sửa và nộp lại |
| Đã phê duyệt | Đã qua hết các bước duyệt nội bộ |
| Đang xác minh | Đang xác minh lý lịch thực tế |
| Hoàn thiện | Xong toàn bộ quy trình — xuất được file Word |
| Từ chối | Hồ sơ không được chấp nhận |
| Rút hồ sơ | Quần chúng/cán bộ chủ động rút hồ sơ |

### 2. Câu hỏi thường gặp / xử lý lỗi

| Câu hỏi / Lỗi | Giải đáp |
|---|---|
| Tạo tài khoản quần chúng báo thất bại dù thông tin đúng | CCCD hoặc SĐT đã được dùng bởi 1 tài khoản khác trong hệ thống (thường do lần tạo trước bị sai, chưa xoá) — xem Phần IV.6 để xoá tài khoản cũ trước |
| Không tìm thấy email cấp tài khoản | Kiểm tra mục Spam/Quảng cáo trong Gmail; nếu vẫn không có, nhờ cán bộ tra cứu lại đúng email đã nhập lúc cấp tài khoản |
| Bấm "Duyệt" nhưng trạng thái không nhảy thẳng sang "Đã phê duyệt" | Bình thường — phải bấm "Duyệt" 3 lần liên tiếp, xem Phần IV.7.2 |
| Không thấy nút "Xuất Word" | Hồ sơ chưa ở trạng thái "Hoàn thiện", hoặc tài khoản chưa được cấp quyền "Xuất file Word" |
| Quần chúng không thấy góp ý sau khi hồ sơ bị trả | Đăng xuất và đăng nhập lại; nếu vẫn không thấy, báo cán bộ kiểm tra lại đã bấm "Lưu nhận xét" trước khi "Trả lại hồ sơ" chưa |
| Tài khoản bị khoá không đăng nhập được | Do nhập sai mật khẩu quá 5 lần — liên hệ cán bộ Ban Xây dựng Đảng để mở khoá |
