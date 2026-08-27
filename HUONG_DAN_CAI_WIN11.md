# Hướng dẫn cài đặt & vận hành hệ thống Lý lịch Đảng trên Windows 11

Áp dụng khi cài trên một máy Windows 11 **chưa có gì cài sẵn**, và triển khai để quần chúng truy cập thật qua domain `lylich.nhabe.vn` (HTTPS) 24/24. Đọc và làm theo đúng thứ tự — tài liệu này đã được cập nhật dựa trên toàn bộ các lỗi thực tế gặp phải khi triển khai.

Trong thư mục gốc dự án có sẵn 2 file hỗ trợ:
- **`install.bat`** — chạy **1 lần duy nhất** khi cài lần đầu (tạo môi trường, cài thư viện, tạo database)
- **`start.bat`** — chạy **mỗi lần** muốn mở ứng dụng (tự khởi động MySQL + Django + web server LAN + Caddy HTTPS)

---

## PHẦN 1 — Cài phần mềm nền

### 1.1. Cài Python — **bản 3.13** (không dùng 3.14, không dùng 3.12)

> ⚠️ Thư viện `Pillow==10.4.0` mà dự án dùng **không hỗ trợ Python 3.14** (lỗi khi cài thư viện). Python 3.12 bản mới nhất thì **không còn file cài đặt** (chỉ còn bản mã nguồn). Nên bắt buộc dùng **Python 3.13**.

1. Vào **python.org/downloads** → kéo xuống bảng **"Active Python releases"** → tìm dòng **"3.13"** → bấm **"Download"** ở đúng dòng đó (không bấm nút vàng to ở đầu trang, nút đó ra bản mới nhất 3.14)
2. Ở trang mới, kéo xuống tìm dòng **"Windows installer (64-bit)"** → bấm tải file `.exe`
3. Nếu Edge cảnh báo "isn't commonly downloaded" → bấm **"..."** cạnh file → **"Keep"**
4. Mở file `.exe` vừa tải. **Quan trọng:** ở màn hình đầu tiên, tick vào ô **"Add python.exe to PATH"** (dễ bị bỏ sót)
5. Bấm **"Install Now"** → đợi xong → **"Close"**
6. Kiểm tra: mở **cửa sổ PowerShell MỚI** (không dùng cửa sổ đã mở từ trước khi cài Python — PATH chưa được cập nhật ở cửa sổ cũ), gõ:
   ```
   python --version
   ```
   Phải ra `Python 3.13.x`.
   - Nếu báo **"Python was not found; run without arguments to install from the Microsoft Store..."** → vào Settings → Apps → Advanced app settings → App execution aliases → tắt (Off) cả 2 công tắc `python.exe` và `python3.exe`, mở PowerShell mới thử lại.

### 1.2. Cài XAMPP

1. Vào **apachefriends.org** → bấm nút **"Download"** cho Windows
2. Mở file `.exe` vừa tải → nếu hỏi UAC → **"Yes"** → nếu XAMPP cảnh báo Antivirus → **"OK"**
3. Màn hình **"Select Components"** → để mặc định → **"Next"**
4. Nơi cài đặt → để mặc định **`C:\xampp`** (không đổi) → **"Next"** → **"Next"** vài lần → **"Finish"**
5. **XAMPP Control Panel** tự mở → dòng **MySQL** → bấm **"Start"** → phải lên xanh, `Port(s): 3306`

### 1.3. Nâng cấp MariaDB lên bản 10.11 (BẮT BUỘC)

> ⚠️ XAMPP mặc định kèm **MariaDB 10.4.32**, nhưng Django 5.1 yêu cầu tối thiểu **MariaDB 10.5+**. Nếu bỏ qua bước này, chạy server sẽ báo lỗi `NotSupportedError: MariaDB 10.5 or later is required`.

1. XAMPP Control Panel → **Stop** MySQL
2. Vào `C:\xampp\` → đổi tên thư mục **`mysql`** thành **`mysql_old`** (giữ lại, không xoá)
3. Vào **mariadb.org/download** → chọn **MariaDB Server**, phiên bản **10.11**, hệ điều hành **Windows**, loại gói **"Zip file"** → Download
4. Giải nén file zip vừa tải, bên trong có 1 thư mục con dạng `mariadb-10.11.xx-winx64` → đổi tên thành **`mysql`** → di chuyển vào `C:\xampp\` (đường dẫn cuối: `C:\xampp\mysql`)
5. Copy file **`my.ini`** từ `C:\xampp\mysql_old\bin\` sang `C:\xampp\mysql\bin\` (đè lên nếu hỏi)
6. Mở PowerShell (cửa sổ mới, không cần venv), gõ:
   ```powershell
   & "C:\xampp\mysql\bin\mysql_install_db.exe" --datadir="C:\xampp\mysql\data"
   ```
   (Lưu ý: PowerShell cần dấu `&` ở đầu khi chạy file có đường dẫn đặt trong dấu ngoặc kép)
7. XAMPP Control Panel → **Start** MySQL lại → phải lên xanh
8. Kiểm tra version:
   ```powershell
   & "C:\xampp\mysql\bin\mysql.exe" -u root -e "SELECT VERSION();"
   ```
   Phải ra bản **10.11.x**

---

## PHẦN 2 — Chép source code dự án vào máy

1. Chép cả thư mục dự án (USB/Zalo/Drive/UltraViewer...) vào máy đích, ví dụ `C:\Users\Admin\Downloads\lylich\lylich`
2. **Không chép** các thư mục sau nếu có ở máy nguồn (để tự tạo lại trên máy đích):
   - **`.venv`** — **tuyệt đối không chép**, vì virtual environment Python ghi chết đường dẫn của máy tạo ra nó, chép qua máy khác sẽ báo lỗi `did not find executable at ...` (venv không portable giữa các máy)
   - `__pycache__`, `logs`, `node_modules`
3. Nếu muốn có sẵn dữ liệu đúng, hãy **xuất dữ liệu mới nhất** từ máy đang chạy tốt trước khi chép, ghi đè lên `lylich_dang.sql`:
   ```powershell
   & "C:\xampp\mysql\bin\mysqldump.exe" -u root lylich_dang > "đường-dẫn\lylich_dang.sql"
   ```

---

## PHẦN 3 — Cài đặt lần đầu (`install.bat`)

1. Double-click **`install.bat`** (nếu SmartScreen cảnh báo → "More info" → "Run anyway")
2. Script tự: dọn `__pycache__` cũ → tạo/kiểm tra `.venv` (tự phát hiện và tạo lại nếu venv bị hỏng do copy từ máy khác) → cài thư viện → bật MySQL → tạo database `lylich_dang` + user `django` (mật khẩu để trống) → tạo file `.env` từ `.env.example`
3. Khi hỏi **"Import du lieu mau nay vao khong? (Y/N)"**:
   - **Y** — import file `lylich_dang.sql` có sẵn (có dữ liệu ngay, bỏ qua migrate)
   - **N** — tạo database trắng, script tự chạy `migrate`, rồi hỏi tạo superuser (nhập số điện thoại + họ tên + mật khẩu)
4. Xong, thấy dòng **"CAI DAT XONG!"**

**Chỉ chạy `install.bat` một lần duy nhất trên máy đó.**

---

## PHẦN 4 — Mở ứng dụng hằng ngày (`start.bat`)

Double-click **`start.bat`** — script tự động:
1. Dọn `__pycache__` cũ
2. Khởi động MySQL (XAMPP)
3. Chạy Django server ở cổng **8010** (cửa sổ **"Django Server"**)
4. Chạy web server tĩnh ở cổng **5500** cho truy cập LAN nội bộ (cửa sổ **"Frontend Server"**), tự mở `http://127.0.0.1:5500/index.html`
5. Chạy **Caddy** để phục vụ HTTPS qua domain `lylich.nhabe.vn` (cửa sổ **"Caddy HTTPS Server"**)

> ⚠️ Windows Firewall có thể hỏi "Allow access" nhiều lần (cho từng cửa sổ/cổng khác nhau) — luôn bấm **"Allow access"**.

**Không đóng 3 cửa sổ đen đó** khi còn đang dùng ứng dụng. Đợi vài giây sau khi chạy `start.bat` rồi mới thử đăng nhập (Django cần thời gian khởi động xong).

### 4.1. Vì sao dùng cổng 8010 (không phải 8000) và 5500 (không phải 8080)?
- **8010**: cổng 8000 mặc định hay bị **Docker Desktop/WSL2** chiếm mất trên các máy có cài Docker cho project khác.
- **5500**: `index.html` chỉ tự nhận diện gọi về Django (`127.0.0.1:8010`) khi trang được mở đúng ở cổng **5500 hoặc 5501** (quy ước cổng của extension "Live Server"). Mở bằng cổng khác hoặc double-click trực tiếp file (`file://`) sẽ bị lỗi CORS hoặc 404.

### 4.2. Truy cập từ máy khác trong LAN
```
http://<IP-LAN-của-máy-server>:5500/index.html
```
Xem IP bằng lệnh `ipconfig` (dòng "IPv4 Address"). Nên đặt **IP tĩnh** cho máy server (Settings → Network & Internet → chọn mạng đang dùng → IP assignment → Edit → Manual → bật IPv4, điền đúng IP/Subnet/Gateway hiện tại) để IP không đổi sau khi khởi động lại router.

---

## PHẦN 5 — Cho quần chúng truy cập qua Internet (domain + HTTPS)

### 5.1. Trỏ DNS
1. Đăng nhập `https://domain.tenten.vn/` (tài khoản quản trị domain `nhabe.vn`)
2. Vào **Quản lý DNS** → thêm bản ghi:
   - Loại: **A**
   - Tên: **`lylich`**
   - Giá trị: **IP công cộng (WAN)** của mạng — kiểm tra bằng cách vào Google gõ "ip của tôi", hoặc xem trực tiếp trong trang quản trị router
3. Lưu lại, đợi 5–30 phút để DNS lan truyền

### 5.2. Port-forward trên router (Draytek)
Vào trang quản trị router (thường `http://192.168.1.1`) → **NAT >> Port Redirection** → tạo 2 rule:

| Service Name | Protocol | Public Port | Private IP | Private Port |
|---|---|---|---|---|
| LyLich-HTTP | TCP | **80** | IP LAN máy server | **80** |
| LyLich-HTTPS | TCP | **443** | IP LAN máy server | **443** |

Nhớ tick **Enable** cho cả 2 rule.

> Nếu router báo **"port configurations collided with Management webpages"**: vào **System Maintenance >> Management** → đổi **HTTP Port** và **HTTPS Port** (quản trị router) sang số khác (VD: `8081`, `8443`) → Save → quay lại tạo NAT rule như trên (từ nay vào quản trị router phải gõ kèm cổng mới, VD `http://192.168.1.1:8081`).

### 5.3. Cài đặt Caddy (tự động HTTPS miễn phí)

1. Vào **caddyserver.com/download** → chọn Platform **Windows**, Architecture **amd64** → Download
2. Tạo thư mục `C:\caddy\`, copy file `.exe` vừa tải vào đó
3. Đổi tên file cho đúng `caddy.exe` bằng **PowerShell** (không dùng Explorer, dễ bị dư đuôi `.exe.exe` do Explorer ẩn phần mở rộng file):
   ```powershell
   Rename-Item "C:\caddy\<tên-file-gốc>" "caddy.exe"
   ```
4. Mở **Notepad**, dán nội dung sau:
   ```
   lylich.nhabe.vn {
   	handle /api/* {
   		reverse_proxy 127.0.0.1:8010
   	}
   	handle /admin/* {
   		reverse_proxy 127.0.0.1:8010
   	}
   	handle /static/* {
   		reverse_proxy 127.0.0.1:8010
   	}
   	handle /media/* {
   		reverse_proxy 127.0.0.1:8010
   	}
   	handle {
   		root * C:\Users\Admin\Downloads\lylich\lylich
   		file_server
   	}
   }
   ```
   (sửa đúng đường dẫn project ở dòng `root *` nếu khác)
5. **File → Save As** → đổi "Save as type" thành **"All Files"** → tên file gõ đúng **`Caddyfile`** (không đuôi) → lưu vào `C:\caddy\`
6. Mở **PowerShell với quyền Administrator** (chuột phải → Run as administrator), gõ:
   ```powershell
   cd C:\caddy
   .\caddy.exe run
   ```
7. Theo dõi log — phải thấy dòng **"certificate obtained successfully"** cho `lylich.nhabe.vn`. Nếu báo lỗi `404` khi xin chứng chỉ (challenge http-01) hoặc `Timeout` (challenge tls-alpn-01) → kiểm tra lại NAT port-forward ở mục 5.2 đã đúng và đã lưu chưa.

Từ lần sau, Caddy sẽ **tự chạy cùng `start.bat`** (đã tích hợp sẵn, xem Phần 4), không cần mở tay bước 6 nữa.

### 5.4. Vì sao dùng đường dẫn tương đối `/api/v1` thay vì `http://...`?
Vì Caddy đã đóng vai trò "cổng vào" duy nhất — vừa phục vụ giao diện (`index.html`), vừa chuyển tiếp `/api/*` sang Django — nên khi truy cập qua `https://lylich.nhabe.vn`, giao diện và API coi như **cùng một nguồn gốc (same-origin)**. Gọi API bằng đường dẫn tuyệt đối `http://...` sẽ bị trình duyệt chặn lỗi **Mixed Content** (trang HTTPS không được gọi tài nguyên HTTP thường).

---

## PHẦN 6 — Cấu hình chạy 24/24 (không cần ai bật tay)

### 6.1. BIOS: tự bật lại máy khi có điện trở lại
Khởi động lại máy, bấm liên tục **Del** hoặc **F2** lúc mới bật nguồn để vào BIOS → tìm mục **"Power Management"** / **"AC Power Recovery"** / **"Restore on AC Power Loss"** → chọn **"Power On"** (không chọn "Power Off"/"Last State").

### 6.2. Windows tự đăng nhập (bỏ qua màn hình nhập mật khẩu)
1. **Windows + R** → gõ `regedit` → Enter (xác nhận UAC nếu hỏi)
2. Vào đúng khoá:
   ```
   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
   ```
3. Sửa/tạo các String Value:
   - `AutoAdminLogon` = `1`
   - `DefaultUserName` = tên tài khoản Windows (VD: `Admin`)
   - `DefaultPassword` = mật khẩu Windows thật của tài khoản đó (nếu chưa có dòng này, chuột phải vùng trống → New → String Value, đặt tên chính xác `DefaultPassword`)

   > Lưu ý: mật khẩu lưu dạng không mã hoá trong Registry — chấp nhận được với máy nội bộ ít người truy cập.
4. Restart máy để kiểm tra: phải **tự vào thẳng Desktop**, không hiện màn hình nhập mật khẩu.

### 6.3. Tự chạy `start.bat` sau khi đăng nhập xong (Task Scheduler)
1. Start → gõ **"Task Scheduler"** → mở
2. Bấm **"Create Task..."** (không phải "Create Basic Task")
3. Tab **General**: Name = `AutoStart LyLich` → tick **"Run with highest privileges"** (bắt buộc, để Caddy có quyền mở cổng 80/443)
4. Tab **Triggers** → **New** → Begin the task: **"At log on"** → chọn user hiện tại → OK
5. Tab **Actions** → **New**:
   - Program/script: **Browse** → chọn file `start.bat`
   - **Start in (optional)**: dán đúng đường dẫn **thư mục gốc project** (bắt buộc điền, không để trống) — VD `C:\Users\Admin\Downloads\lylich\lylich`
6. Tab **Conditions**: bỏ tick "Start the task only if the computer is on AC power" (nếu có)
7. **OK** để lưu (có thể hỏi lại mật khẩu Windows)
8. Restart máy 1 lần để kiểm tra toàn bộ chuỗi: tự bật máy (nếu mất điện) → tự đăng nhập → tự chạy `start.bat` → 3 cửa sổ server tự mở.

### 6.4. Chuyển MySQL thành Windows Service (giảm rủi ro hỏng dữ liệu khi mất điện)
Mặc định MySQL của XAMPP chạy như 1 chương trình thường — khi mất điện/tắt đột ngột dễ hỏng file log nội bộ (xem lỗi Aria ở Phần 7). Nên chuyển thành Windows Service:
1. Mở **XAMPP Control Panel với quyền Administrator** (chuột phải icon → Run as administrator)
2. Tick vào **checkbox nhỏ** ở đầu dòng **MySQL** (cột trước tên module)
3. Xác nhận UAC nếu được hỏi

---

## PHẦN 7 — Các bước thủ công (khi `install.bat`/`start.bat` báo lỗi)

### 7.1. Tạo virtual environment & cài thư viện bằng tay
```powershell
cd đường-dẫn\đến\lylich\backend
python -m venv ..\.venv
..\.venv\Scripts\Activate.ps1
```
- Lỗi "running scripts is disabled": gõ `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` trước, rồi Activate lại.
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

### 7.2. Tạo database qua phpMyAdmin
`localhost/phpmyadmin` → tab **SQL** → dán:
```sql
CREATE DATABASE lylich_dang CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'django'@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON lylich_dang.* TO 'django'@'localhost';
FLUSH PRIVILEGES;
```
→ **Go**

### 7.3. Khôi phục tài khoản bị xoá mềm / đặt lại mật khẩu
Nếu đăng nhập báo "Tài khoản không tồn tại" nhưng tạo lại báo "Số điện thoại đã dùng" — tài khoản đó đang bị xoá mềm (`deleted_at` có giá trị). Trong `backend`, đã activate venv:
```powershell
python manage.py shell -c "from apps.accounts.models import User; u = User.objects.get(phone='SỐ_ĐIỆN_THOẠI'); u.deleted_at = None; u.status = 'active'; u.save(); print('OK:', u.full_name, u.status)"
python manage.py changepassword SỐ_ĐIỆN_THOẠI
```

### 7.4. Chạy server & mở giao diện bằng tay
```powershell
python manage.py runserver 0.0.0.0:8010
```
Mở thêm 1 PowerShell khác (không cần venv), tại thư mục gốc project:
```powershell
python -m http.server 5500
```
Mở trình duyệt vào `http://127.0.0.1:5500/index.html`. **Không** double-click mở thẳng file `index.html`, **không** dùng cổng khác 5500/5501.

---

## PHẦN 8 — Xử lý lỗi thường gặp

| Lỗi | Nguyên nhân / Cách xử lý |
|---|---|
| `'python' is not recognized` | Chưa tick "Add python.exe to PATH" lúc cài, hoặc đang dùng cửa sổ PowerShell mở từ trước khi cài Python → mở cửa sổ mới |
| `Python was not found; run without arguments to install from the Microsoft Store` | Tắt "App execution aliases" cho python.exe/python3.exe trong Settings → Apps |
| Cài `Pillow` thất bại, báo "does not support Python 3.14" | Đang dùng Python 3.14 — gỡ ra, cài lại **Python 3.13** (Phần 1.1) |
| `NotSupportedError: MariaDB 10.5 or later is required` | XAMPP dùng bản MariaDB 10.4 mặc định quá cũ — làm theo Phần 1.3 để nâng cấp lên 10.11 |
| `did not find executable at 'C:\Users\...\python.exe'` khi chạy venv | Thư mục `.venv` bị chép nguyên từ máy khác (không portable) — xoá `.venv`, chạy lại `install.bat` (đã tự phát hiện & tạo lại) |
| PowerShell: "running scripts is disabled" | `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` trước khi Activate venv |
| `Access denied for user 'django'@'localhost'` | User MySQL `django` chưa tồn tại/sai mật khẩu — làm lại Phần 7.2, đảm bảo `DB_PASSWORD=` trong `.env` để trống |
| CORS: `blocked by CORS policy`, `Origin 'null'` | Đang mở `index.html` bằng double-click (`file:///...`) — phải mở qua `http://127.0.0.1:5500/index.html` |
| Đăng nhập báo `404 Not Found` dù mở đúng `http://127.0.0.1:.../index.html` | Đang phục vụ frontend ở cổng khác 5500/5501 — `index.html` chỉ tự nhận API ở đúng 2 cổng này |
| Đăng nhập báo `502 Bad Gateway` khi vào qua domain HTTPS | Caddy không kết nối được Django (cổng 8010) — kiểm tra cửa sổ "Django Server" còn chạy không, có báo lỗi đỏ không |
| `Mixed Content: ... requested an insecure resource 'http://...'` | `index.html` đang hardcode gọi API bằng `http://` trong khi trang tải qua `https://` — đảm bảo code dùng đường dẫn tương đối `/api/v1` khi chạy qua domain Caddy |
| Log Caddy báo lỗi xin chứng chỉ SSL (`404` hoặc `Timeout`) | NAT port-forward (Phần 5.2) chưa đúng, hoặc port 80/443 bị Draytek tự chiếm cho trang quản trị router — đổi cổng quản trị router (System Maintenance >> Management) |
| Router báo "port configurations collided with Management webpages" | Đổi HTTP/HTTPS Port của chính router (System Maintenance >> Management) sang số khác, VD 8081/8443 |
| `netstat` báo PID đang chiếm cổng nhưng `tasklist` báo không tìm thấy | Dấu hiệu Docker Desktop/WSL2 đang publish cổng đó — đổi dự án sang cổng khác (VD 8010 thay vì 8000) |
| Tài khoản: "không tồn tại" khi login nhưng "đã dùng" khi tạo mới | Tài khoản bị xoá mềm — làm theo Phần 7.3 |
| MySQL báo "shutdown unexpectedly", log có `Aria recovery failed... delete all aria_log` | File log Aria bị hỏng do tắt máy đột ngột — xoá `aria_log_control` và các file `aria_log.########` trong `C:\xampp\mysql\data\`, khởi động lại MySQL. Nên làm Phần 6.4 để tránh lặp lại |
| Windows Defender Firewall hỏi khi chạy server | Bấm **"Allow access"** — bắt buộc để trình duyệt/máy khác/Caddy gọi được vào server |
| SmartScreen chặn khi chạy `.bat`/Caddy | Bấm **"More info"** → **"Run anyway"** |
| XAMPP báo Apache không bật được do cổng 443 đang dùng | Bình thường — Caddy đang dùng cổng 443, dự án này không cần Apache, bỏ qua |
