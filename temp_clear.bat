@echo off
echo Clearing...
del /s /q C:\Windows\Temp\*
del /s /q C:\Users\%USERNAME%\AppData\Local\Temp\*
rd /s /q C:\Windows\Temp
md C:\Windows\Temp
rd /s /q C:\Users\%USERNAME%\AppData\Local\Temp
md C:\Users\%USERNAME%\AppData\Local\Temp
echo Clear success! 
pause
