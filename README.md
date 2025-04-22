# Automation KYC Verification Dashboard 🌌

An intelligent, modular identity verification system for the banking sector, built with Python, Streamlit, and OCR (Tesseract). Designed to streamline KYC (Know Your Customer) processes, the tool enables manual verification via ID image upload and structured field comparison — with a fully prepared email automation module for future integration.

## 🚀 Features

- 🌠 OCR-based ID field extraction (Tesseract + PIL preprocessing)
- 🛰️ Manual data input form with real-time comparison
- 🛡️ Logging and audit trail saved as CSV
- ✉️ Email scanner module (coded but disabled for security)
- 🎨 Galactic UI via Streamlit tabs (Auto Email Scan & Manual Upload)
- 📁 Modular codebase with separation of concerns

## 🔧 Project Structure

```
/autocris
│
├── kyc_verification_app.py         # Main Streamlit dashboard
├── .env                            # (Not included) Email credentials
├── requirements.txt                # Python dependencies
├── launch_kyc_dashboard.bat        # Auto-launcher with streamlit installer
├── logs/
│   └── kyc_verification_log.csv    # Verification results
├── src/
│   ├── email_processing.py         # IMAP integration (deactivated)
│   ├── ocr.py                      # Preprocessing + OCR logic
│   ├── data_validation.py          # Field comparison and validation
│   ├── dashboard.py                # Streamlit visual layout
│   ├── logging_utils.py            # Save/load CSV log
```

## 🧪 How to Run

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/galactic-kyc-dashboard.git
   cd galactic-kyc-dashboard
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the app**  
   ```bash
   streamlit run kyc_verification_app.py
   ```

4. **(Optional)** Use `launch_kyc_dashboard.bat` to auto-launch with pip check

## 🛑 Notes on Email Automation

> ✉️ The `email_processing.py` module is fully implemented and can extract attachments from the latest IMAP inbox email. For safety reasons and privacy during development, it is disabled by default. You can activate it by setting up a secure `.env` file with your credentials.

## 💡 Demo Use Case

Use the provided fictional ID image (e.g., “McLovin.jpg”) and manually enter name, date of birth, and address. The system will validate OCR-extracted values vs input and log the result.
# Requirements for Automation KYC Verification Dashboard

streamlit==1.32.0         # For building the interactive dashboard
pytesseract==0.3.10        # OCR engine wrapper for Python (uses Tesseract)
Pillow==10.2.0             # Image processing library (used in OCR)
pandas==2.2.0              # Data manipulation and CSV logging
python-dotenv==1.0.1       # Loads email credentials from .env file
openpyxl==3.1.2            # Required for Excel form reading
You can install all dependencies using:

pip install -r requirements.txt
re is a simple and secure .env.example file you can include in your GitHub repository. This helps others understand what environment variables are needed without exposing sensitive data:

# .env.example – Sample environment variables for KYC email integration

EMAIL_USER=your_email@example.com
EMAIL_PASS=your_app_specific_password
IMAP_SERVER=imap.yourmailprovider.com
SMTP_SERVER=smtp.yourmailprovider.com
SMTP_PORT=587
🔒 Important:

Do not commit your actual .env file.

Use this .env.example to document required variables.
## 👤 Author

**Cristóbal Cáceres**
