@echo off
title start_bot
:loop
::Attention! This code must be debug because this code kills all the python.exe

taskkill /im python.exe /f
start /b python C:\Users\DELL\Documents\TelegramBot\neko_seeker_bot\neko_seeker_main.py
timeout /t 1200
goto loop
