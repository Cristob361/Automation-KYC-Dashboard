@echo off
REM === Galactic KYC Launcher with VENV Activation and Streamlit Auto-Installer ===

:: Go to root folder of the project (where this script is located)
cd /d %~dp0

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Checking if Streamlit is installed...
pip show streamlit >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Streamlit not found. Installing...
    pip install streamlit
)

echo Launching Galactic KYC Verification Dashboard...
python -m streamlit run kyc_verification_app.py

pause
