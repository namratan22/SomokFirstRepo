@echo off
REM YouTube Transcript Knowledge Base - Startup Script for Windows

echo Starting YouTube Transcript Knowledge Base Tool...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed
    pause
    exit /b 1
)

REM Check if dependencies are installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
)

REM Create outputs directory if it doesn't exist
if not exist "outputs" mkdir outputs

REM Run the application
echo Opening web browser...
echo Access the app at: http://localhost:8501
echo.
streamlit run app.py

pause
