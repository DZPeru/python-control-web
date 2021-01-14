# import module
import streamlit as st
import subprocess  # import blockdiag

from utils.save_file import save_file_diag
from utils.save_file import remove_temporals
from utils.save_file import generate_png_from_blockdiag

# Variables and cons
options = ["1.1. Upload your file (.diag)",
           "1.2. Create your file (.diag)"]
base_diag_file = """diagram admin {
    block1 -> block2;
}"""
sample_file_diag = "sample.diag"
sample_file_png = "sample.png"
subheaders=["1. Load or create a diagram file (skip if it's new)",
            "2. Setup as control system",
            "3. "]


# Title
st.title("Python-control-web")
# Description
st.header("The Python Control Systems Library is a Python module that implements basic operations for analysis and design of feedback control systems.")
# Subheader
st.subheader(subheaders[0])

data = st.radio('Choose one of them', options)

if data:
    remove_temporals(sample_file_diag)
    remove_temporals(sample_file_png)

    if data == options[0]:
        uploaded_file = st.file_uploader("Upload your (.diag)", type=['diag'])
        if uploaded_file is not None:
            file_details = {"FileName": uploaded_file.name,
                            "FileType": uploaded_file.type, "FileSize": uploaded_file.size}

            datax = uploaded_file.read().decode('ascii')
            st.code(datax)
            save_file_diag(sample_file_diag, datax)

    if data == options[1]:
        # st.text("Or type the diag in the following text box input")

        entry_data = st.text_area("", value=base_diag_file)
        save_file_diag(sample_file_diag, entry_data)

    load_file = st.button("Load and plot diagram")
    if load_file:
        generate_png_from_blockdiag(sample_file_diag)
        st.image(sample_file_png, "Your diagram loaded")

# Subheader
st.subheader(subheaders[1])
