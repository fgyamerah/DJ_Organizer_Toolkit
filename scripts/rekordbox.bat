@echo off
set XML_PATH="D:\KKDJ_LIBRARY\_REKORDBOX_XML_EXPORTS\rekordbox.xml"

if not exist %XML_PATH% (
    echo ❌ XML not found at %XML_PATH%
    pause
    exit /b 1
)

start "" "C:\Program Files\Pioneer\rekordbox\rekordbox.exe"
timeout /t 3 >nul
explorer "D:\KKDJ_LIBRARY\_REKORDBOX_XML_EXPORTS"