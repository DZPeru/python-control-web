import subprocess
import streamlit as st

font_dir="fonts/Roboto-Medium.ttf"

def save_file_diag(filename, data):

    text_file = open(filename, "w")
    n = text_file.write(str(data))
    text_file.close()

    return True


def remove_temporals(filename):
    try:
        # Command as string
        command = 'rm {filename}'.format(filename=filename)
        # Use shell to execute the command
        sp = subprocess.Popen(command, shell=True)
        # Store the return in rc variable
        rc = sp.wait()
    except Exception as e:
        st.text(str(e))
        
    return True

def generate_png_from_blockdiag(filename):
    # https://www.golinuxcloud.com/python-subprocess/
    # Command as string
    command = ' blockdiag -f {font_dir} {filename}'.format(
       font_dir=font_dir, filename=filename)
    # Use shell to execute the command
    sp = subprocess.Popen(command, shell=True)
    # Store the return in rc variable
    rc = sp.wait()

    return True