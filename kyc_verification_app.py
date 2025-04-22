import streamlit as st
from src.email_processing import read_email, download_attachments
from src.ocr import extract_ocr_data
from src.data_validation import load_excel_data, compare_data
from src.logging_utils import generate_log, load_log
from src.dashboard import render_dashboard
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

st.set_page_config(
    page_title="Galactic KYC Verification",
    layout="wide",
    page_icon=":milky_way:"
)

render_dashboard()