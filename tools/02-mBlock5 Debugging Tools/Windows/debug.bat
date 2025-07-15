@echo off
cd /d C:\Users\Public\Programs\mblock
start "" mBlock.exe --remote-debugging-port=9222
timeout /t 3 >nul
start chrome http://localhost:9222
