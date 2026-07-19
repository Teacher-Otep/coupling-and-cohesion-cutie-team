@echo off
REM Batch file to generate PowerPoint presentation
REM This script will install python-pptx if needed and generate the presentation

echo.
echo ============================================================
echo Coupling and Cohesion Refactoring - Presentation Generator
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python 3.6 or later from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [✓] Python found
python --version
echo.

REM Check if python-pptx is installed
python -c "import pptx" >nul 2>&1
if errorlevel 1 (
    echo [*] Installing python-pptx library...
    echo.
    python -m pip install --quiet python-pptx
    if errorlevel 1 (
        echo ERROR: Failed to install python-pptx
        echo.
        echo Try installing manually:
        echo   pip install python-pptx
        pause
        exit /b 1
    )
    echo [✓] python-pptx installed successfully
) else (
    echo [✓] python-pptx is already installed
)

echo.
echo [*] Generating presentation...
echo.

REM Run the presentation generator
python generate_presentation.py
if errorlevel 1 (
    echo.
    echo ERROR: Failed to generate presentation
    pause
    exit /b 1
)

echo.
echo ============================================================
echo [✓] Presentation generated successfully!
echo ============================================================
echo.
echo File: Coupling_and_Cohesion_Refactoring.pptx
echo.
pause
