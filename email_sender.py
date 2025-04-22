import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_result_email(to_address, status, mismatches=None):
    subject = "KYC Verification Result"
    if status == "Approved":
        body = "✅ Your identity verification has been approved. Thank you!"
    else:
        mismatch_str = ", ".join(mismatches) if mismatches else "fields"
        body = f"⚠️ Your verification requires manual review due to mismatched fields: {mismatch_str}."

    message = MIMEMultipart()
    message["From"] = EMAIL_USER
    message["To"] = to_address
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(message)
        print(f"Email sent to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")
