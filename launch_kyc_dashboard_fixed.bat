@echo off
REM === Galactic KYC Streamlit Launcher with Auto-Installer & Path Fix ===

:: Go to root folder of the project (where this script is located)
cd /d %~dp0

echo Checking if Streamlit is installed...

pip show streamlit >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Streamlit not found. Installing...
    pip install streamlit
)

echo Launching Galactic KYC Verification Dashboard...
python -m streamlit run src/kyc_verification_app.py

pause
