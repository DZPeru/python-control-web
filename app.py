# import module
import streamlit as st
import subprocess  # import blockdiag
import requests

from utils.save_file import save_file_diag
from utils.save_file import remove_temporals
from utils.save_file import generate_png_from_blockdiag

# Variables and cons
sample_file_diag = "temp/sample.diag"
sample_file_png = "temp/sample.png"
subheaders=["1. Load or create a diagram file (skip if it's new)",
            "2. Generate code with 'python-control' library",
            "3. "]
options = ["1.1. Upload your file (.diag)",
           "1.2. Create your file (.diag)",
           "1.3. Give URL of your file (.diag)",]
base_diag_file = """diagram admin {
    block1 -> block2;
}"""

# Title
st.title("Python-control-web")
# Description
st.header("The Python Control Systems Library is a Python module that implements basic operations for analysis and design of feedback control systems.")
# Subheader
st.subheader(subheaders[0])

data = st.radio('Choose one of them', options)

show=0
if data:
    remove_temporals(sample_file_diag)
    remove_temporals(sample_file_png)

    if data == options[0]:
        show=1
        uploaded_file = st.file_uploader("Upload your (.diag)", type=['diag'])
        if uploaded_file is not None:
            file_details = {"FileName": uploaded_file.name,
                            "FileType": uploaded_file.type, "FileSize": uploaded_file.size}

            datax = uploaded_file.read().decode('ascii')
            st.code(datax)
            save_file_diag(sample_file_diag, datax)

    if data == options[1]:
        show=1
        st.markdown('Write your code below like the <a target="_blank" href="{url}">examples</a>'.format(url="http://blockdiag.com/en/blockdiag/attributes/node.attributes.html"))
        entry_data = st.text_area("", value=base_diag_file,height=300)
        save_file_diag(sample_file_diag, entry_data)


    if data==options[2]:
        show=1
        temp_url=st.text_input("example: https://github.com/DZPeru/python-control-web/releases/download/samples/sample.diag")

        if temp_url:
            print('Beginning file download with requests')
            
            r = requests.get(temp_url)

            with open(sample_file_diag, 'wb') as f:
                f.write(r.content)
    
    if show==1:
        show=0
        with st.spinner(text='In progress'):
            
            try:
                generate_png_from_blockdiag(sample_file_diag)
                st.image(sample_file_png, "Your diagram loaded")
                # st.success('Done')
            except Exception as e:
                pass
# Subheader
st.subheader(subheaders[1])

generate_my_code=st.button("Generate my code")

if generate_my_code:
    print("gaaa")