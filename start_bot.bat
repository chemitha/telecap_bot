@echo off
title start_bot

:: Step 0: Check if Python is installed on the system
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [41;37m[!] Python is not installed on this system.[0m
    echo +------------------------------------------------------------------+
    echo ^|                                                                  ^|
    echo ^| Please download the latest version and run this .bat file again: ^|
    echo ^| https://www.python.org/downloads/                                ^|
    echo ^|                                                                  ^|
    echo ^|------------------------------------------------------------------^|
    echo ^|                                                                  ^|
    echo ^| Recommended quick installation guide:                            ^|
    echo ^| https://www.youtube.com/shorts/3aG9ssaTsw0                       ^|
    echo ^|                                                                  ^|
    echo +------------------------------------------------------------------+
    timeout /t 3 >nul
    start https://www.python.org/downloads/
    pause
    exit
)

echo [1/2] Checking system dependencies...
python -m pip show python-telegram-bot >nul 2>&1
if %errorlevel% equ 0 (
    cls
    echo [2/2] Launching application...
    goto start_loop
)

:install_deps
echo [!] Dependencies missing. Initializing setup wizard...
python -m pip install -r requirements.txt
cls
echo [2/2] Launching application...

:start_loop
taskkill /im python.exe /f 2>nul
python _seeker_main.py
timeout /t 1200
goto start_loop
