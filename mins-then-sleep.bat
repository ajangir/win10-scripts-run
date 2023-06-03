@echo off
for /l %%i in (1,1,3) do (
  timeout /t 60 >nul
  echo %%i)
C:\Windows\System32\rundll32.exe powrprof.dll,SetSuspendState 0,1,0
