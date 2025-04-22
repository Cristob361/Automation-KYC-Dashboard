import streamlit as st
import pandas as pd
from datetime import datetime
from src.logging_utils import save_log

def manual_entry_form():
    st.markdown("### 🧾 Manual Data Entry")
    name_id = st.text_input("Full Name (from ID)")
    dob_id = st.date_input("Date of Birth (from ID)")
    address_id = st.text_input("Address (from ID)")

    name_form = st.text_input("Full Name (from Excel Form)")
    dob_form = st.date_input("Date of Birth (from Form)")
    address_form = st.text_input("Address (from Form)")

    if st.button("Submit Manual Entry"):
        status = "Approved" if name_id == name_form and dob_id == dob_form and address_id == address_form else "Manual Review"
        data_id = {"Name": name_id, "DOB": str(dob_id), "Address": address_id}
        data_form = {"Form_Name": name_form, "Form_DOB": str(dob_form), "Form_Address": address_form}
        mismatches = []
        for k in data_id:
            if data_id[k] != data_form.get("Form_" + k, ""):
                mismatches.append(k)
        save_log(data_id, data_form, status)
        if status == "Approved":
            st.success("✅ Data Approved")
        else:
            st.warning("⚠️ Manual Review Needed: " + ", ".join(mismatches))
        st.json(data_id)
        st.json(data_form)
