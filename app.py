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
resume_file = current_dir/"assets"/"A_Sudhara_Dhananjaya - QA_Engineer.pdf"
profile_pic = current_dir/"assets"/"profile-pic-3.png"


# --- General Settings - Part 2 ---
NAME = "Sudhara Dhananjaya"
DESCRIPTION = """
Aspiring Data Scientist seeking internship opportunities to gain hands-on experience in the field of data science.
"""

EMAIL = "sudharad7@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sudharad/",
    "GitHub": "https://github.com/sudharaD",
    "Portfolio": "http://localhost:8501/",
}

PROJECTS = {
    "✅ Project 1": "https://github.com/sudharaD",
    "✅ Project 2": "https://github.com/sudharaD",
    "✅ Project 3": "https://github.com/sudharaD",
    "✅ Project 4": "https://github.com/sudharaD",
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


# --- Social Links ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Experience and Qualifications ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✅ Arimac Lanka (Pvt) Ltd | 06 Months | Quality Assuarance Engineer Intern
- ✅ Virtusa (Pvt) Ltd | 08 Months - Quality Assuarance Engineer Intern
    """
)

# --- Skills ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- ✅ Programming: Python (Scikit-learn, Pandas), SQL, VBA
- ✅ Data Visulization: PowerBi, MS Excel, Plotly
- ✅ Modeling: Logistic regression, linear regression, decition trees
- ✅ Databases: Postgres, MongoDB, MySQL
    """
)

# --- Academic Background ---
st.write("#")
st.subheader("Academic Background")
st.write("---")

st.write("🎓", "**BSc (Hons) Computing | Wrexham Glyndwr University - UK**")
st.write("2021 - 2022")

st.write("#")
st.write("🏫", "**NDT in Information Technology | Institute of Technology, University of Moratuwa**")
st.write("2019 - 2022")
st.write("Current GPA - 3.32 (Up to 4th Semester)")

st.write("#")
st.write("📚", "**GCE Advanced Level**")
st.write("2017")
st.write(
    """
- ➔ Combined Mathematics - B
- ➔ Chemistry - C
- ➔ Physics - C
    """
)

# --- Projects & Accomplishments ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")











