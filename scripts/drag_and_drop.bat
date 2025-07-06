@echo off
setlocal enabledelayedexpansion

:: Configure Python Path
set PYTHON="python"
set SCRIPT="%~dp0src\core\organizer.py"

:: Parse Input
if "%~1"=="" (
    set /p SOURCE="📂 Drag folder with music or enter path: "
) else (
    set "SOURCE=%~1"
)

:: Run with default output
%PYTHON% %SCRIPT% "%SOURCE%" "D:\KKDJ_LIBRARY"

pause