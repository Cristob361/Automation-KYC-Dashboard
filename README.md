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

## 📜 License

This project is part of an academic submission under the MSc in AI for Business – National College of Ireland (2025). Not intended for commercial deployment.

## 👤 Author

**Cristóbal Cáceres**
MSc in Artificial Intelligence for Business
