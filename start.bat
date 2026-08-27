@echo off
setlocal
chcp 65001 >nul
echo ============================================
echo   KHOI DONG UNG DUNG LY LICH DANG
echo ============================================
echo.

set "ROOT=%~dp0"
set "BACKEND=%ROOT%backend"
set "VENV=%ROOT%.venv"

if not exist "%VENV%\Scripts\python.exe" (
    echo [LOI] Chua thay virtual environment.
    echo       Hay chay install.bat truoc ^(chi can chay 1 lan duy nhat^).
    pause
    exit /b 1
)

"%VENV%\Scripts\python.exe" --version >nul 2>&1
if errorlevel 1 (
    echo [LOI] Virtual environment bi hong ^(co the do project duoc chep tu may khac^).
    echo       Hay xoa thu muc .venv roi chay lai install.bat de tao lai tren may nay.
    pause
    exit /b 1
)

echo [0/3] Don cache Python cu ^(tranh chay nham code cu^)...
for /f "delims=" %%D in ('dir /s /b /ad "%ROOT%__pycache__" 2^>nul') do rd /s /q "%%D"

echo [1/3] Khoi dong MySQL ^(XAMPP^)...
if exist "C:\xampp\mysql_start.bat" (
    start "" /min "C:\xampp\mysql_start.bat"
    timeout /t 4 >nul
) else (
    echo [CANH BAO] Khong thay XAMPP o C:\xampp.
    echo            Hay tu bat MySQL qua XAMPP Control Panel roi bam phim bat ky.
    pause
)

echo [2/3] Khoi dong Django server...
call "%VENV%\Scripts\activate.bat"
pushd "%BACKEND%"
start "Django Server - DUNG TAT CUA SO NAY" cmd /k "python manage.py runserver 0.0.0.0:8010"
popd

echo [3/4] Khoi dong web server cho giao dien LAN, mo trinh duyet...
REM Khong duoc mo index.html bang cach double-click / file:// vi trinh duyet
REM se chan CORS (Origin: null). Phai phuc vu qua http://
REM Dung dung cong 5500 vi index.html chi tu nhan API server (127.0.0.1:8010)
REM khi chay o cong 5500/5501 (gia dinh la Live Server) - cong khac se bi 404.
pushd "%ROOT%"
start "Frontend Server - DUNG TAT CUA SO NAY" cmd /k "python -m http.server 5500"
popd

echo [4/4] Khoi dong Caddy ^(HTTPS cho domain lylich.nhabe.vn^)...
if exist "C:\caddy\caddy.exe" (
    pushd "C:\caddy"
    start "Caddy HTTPS Server - DUNG TAT CUA SO NAY" cmd /k "caddy.exe run"
    popd
) else (
    echo [CANH BAO] Khong tim thay C:\caddy\caddy.exe - bo qua HTTPS.
    echo            Truy cap qua domain se khong hoat dong.
)

timeout /t 4 >nul
start "" "http://127.0.0.1:5500/index.html"

echo.
echo ============================================
echo   DA KHOI DONG XONG.
echo   Ung dung dang chay o 3 cua so: "Django Server", "Frontend Server"
echo   va "Caddy HTTPS Server".
echo   DUNG DONG cac cua so do khi con dang dung ung dung.
echo ============================================
pause
