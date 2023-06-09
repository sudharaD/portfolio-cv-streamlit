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
resume_file = current_dir/"assests"/"CV.pdf"
profile_pic = current_dir/"assests"/"profile-pic.png"


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


st.title("Hello there")
