import subprocess
import streamlit as st
from src.pdf_to_table.config.configuration import Configuration

configuration = Configuration()
file_name = configuration.get_pdf_saver_config().file_name

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

if uploaded_file is not None:
    with open(file_name, "wb") as f:
        f.write(uploaded_file.getbuffer())

# with open('output.zip', 'rb') as f:
#         zip_data = f.read()
#         st.download_button(label="Download Zip File", data=zip_data, file_name='downloaded_files.zip', key='zip')

result = subprocess.run("dvc repro", shell=True, capture_output=True, text=True)
if result.returncode:
    print("DONE")
    # for