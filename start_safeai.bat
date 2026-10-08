@echo off

cd /d "C:\Users\vaidy\OneDrive\Desktop\Python code\Project\safeAI"

start "" "C:\Users\vaidy\OneDrive\Desktop\Python code\.venv\Scripts\python.exe" app.py

timeout /t 3 /nobreak >nul

start "" http://127.0.0.1:5000

pause