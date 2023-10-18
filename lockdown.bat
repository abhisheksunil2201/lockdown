@echo off
echo Welcome to Lockdown Encryption Program!
echo This program will ensure the security of your files.
set /p answer=Do you want to proceed? (Y/N): 
if /i "%answer%"=="Y" (
    start src/main.py
) else (
    echo Autorun declined. Your files will remain encrypted.
)