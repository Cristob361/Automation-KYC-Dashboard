# Importar en la parte superior del archivo principal
from src.manual_entry import manual_entry_form
from src.email_reader import fetch_latest_email_with_attachments

# Dentro del layout del dashboard
tab1, tab2, tab3 = st.tabs(["🚀 Auto Email Scan", "🛰️ Manual Upload", "📝 Manual Entry"])

with tab1:
    if st.button("Scan Latest Email"):
        sender, attachments = fetch_latest_email_with_attachments()
        if not attachments:
            st.warning("No valid attachments found.")
        else:
            st.success(f"Files downloaded from {sender}")
            for file in attachments:
                st.write("Downloaded:", file)

with tab2:
    st.write("Upload ID image and Excel form manually for demo/testing.")
    id_img = st.file_uploader("ID Image", type=["jpg", "jpeg", "png"])
    excel = st.file_uploader("Excel Form", type=["xlsx", "xls"])
    if st.button("Verify Uploaded Files"):
        if not id_img or not excel:
            st.error("Please upload both files.")
        else:
            with open("temp_id_img.png", "wb") as f:
                f.write(id_img.read())
            with open("temp_form.xlsx", "wb") as f:
                f.write(excel.read())
            ocr_data = extract_ocr_data("temp_id_img.png")
            form_data = read_form_data("temp_form.xlsx")
            status, mismatches = compare_fields(ocr_data, form_data)
            save_log(ocr_data, form_data, status)
            show_result(ocr_data, form_data, status, mismatches)

with tab3:
    manual_entry_form()
