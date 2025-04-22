import os
from src.email_processing import read_email, download_attachments
from src.ocr import extract_ocr_data
from src.data_validation import read_form_data, compare_fields
from src.logging_utils import save_log
from src.email_sender import send_result_email

def process_latest_email_batch():
    print("Processing latest email...")
    msg = read_email()
    if not msg:
        print("No email retrieved.")
        return

    sender = msg.get("From")
    id_img, excel = download_attachments(msg)
    if not id_img or not excel:
        print("Missing attachments.")
        return

    ocr_data = extract_ocr_data(id_img)
    form_data = read_form_data(excel)
    status, mismatches = compare_fields(ocr_data, form_data)
    save_log(ocr_data, form_data, status)
    send_result_email(sender, status, mismatches)

if __name__ == "__main__":
    process_latest_email_batch()
