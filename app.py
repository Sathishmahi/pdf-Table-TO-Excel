import os
import subprocess
import pandas as pd
import streamlit as st
from src.pdf_to_table.config.configuration import Configuration

configuration = Configuration()
file_name = configuration.get_pdf_saver_config().file_name
csv_dir_name = configuration.get_text_extractor_config().csv_dir_name

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

if uploaded_file is not None:
    with open(file_name, "wb") as f:
        f.write(uploaded_file.getbuffer())

# with open('output.zip', 'rb') as f:
#         zip_data = f.read()
#         st.download_button(label="Download Zip File", data=zip_data, file_name='downloaded_files.zip', key='zip')

# result = subprocess.run("dvc repro", shell=True, capture_output=True, text=True)
# if result.returncode:
if True:
    if not len(os.listdir(csv_dir_name)):
        st.write(f"no table contain this pdf or something went wrong")
    csv_files = [file for file in os.listdir(csv_dir_name) if file.endswith(".csv")]

    # Allow the user to select a CSV file
    selected_file = st.selectbox("Select a CSV file to display:", csv_files)

    # Read and display the selected CSV file
    if selected_file:
        st.subheader(f"Displaying {selected_file}")
        df = pd.read_csv(os.path.join(csv_dir_name, selected_file))
        st.write(df)
    else:
        st.write("Please select a CSV file to display.")