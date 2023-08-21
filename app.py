import streamlit as st
from src.pdf_to_table.config.configuration import Configuration

configuration = Configuration()
file_name = configuration.get_pdf_saver_config().file_name

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

if uploaded_file is not None:
    with open(file_name, "wb") as f:
        f.write(uploaded_file.getbuffer())
st.stop()
st.write("This line will be executed if the server is not stopped.")