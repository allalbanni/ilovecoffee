@echo off
REM Automated PDF Marking System - Startup Script

echo ========================================
echo  Automated PDF Marking System
echo ========================================
echo..\run.bat.\run.bat

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created.
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if dependencies are installed
echo Checking dependencies...
pip list | findstr /i "streamlit" >nul
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    echo Dependencies installed.
    echo.
)

REM Launch the application
echo Launching Automated PDF Marking System...
echo.
echo The application will open in your browser at: http://localhost:8501
echo Press Ctrl+C to stop the server.
echo.

streamlit run app.py

pause
