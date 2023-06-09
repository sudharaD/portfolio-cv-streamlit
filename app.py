from pathlib import Path
import streamlit as st
from PIL import Image


# --- General Settings - Part 1 ---
PAGE_TITLE = "Digital CV | Sudhara Dhananjaya"
PAGE_ICON = ":rocket:" # can use "random" for random emoji


# st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
# Call set_page_config only once at the beginning of the script
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- Path Settings ---
#sets the variable current_dir to the parent directory of the current file if the variable __file__ is present
#in the local namespace. Otherwise, it sets current_dir to the current working directory.
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()


css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"CV.pdf"
profile_pic = current_dir/"assets"/"profile-pic.png"


# --- General Settings - Part 2 ---
NAME = "Sudhara Dhananjaya"
DESCRIPTION = """
Aspiring Data Scientist seeking internship opportunities to gain hands-on experience in the field of data science.
"""

EMAIL = "sudharad7@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sudharad/",
    "GitHub": "https://github.com/sudharaD",
    "Portfolio": "Still developing",
}

PROJECTS = {
    "✅ Project 1",
    "✅ Project 2",
    "✅ Project 3",
    "✅ Project 4",
}


# --- LOAD CSS, PDF & PROFILE PICTURE ---
with open(css_file) as f:
    st.markdown("<style>{}<style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- Hero Section ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name = resume_file.name,
        mime="application/octet-stream",
    )
    st.write(":mailbox:", EMAIL)
