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
resume_file = current_dir/"assets"/"Sudhara Dhananjaya - CV.pdf"
profile_pic = current_dir/"assets"/"profile-pic-4.png"


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
    "✅ Skin Infection Detection Assistant": "https://github.com/sudharaD",
    "✅ Movie Recommendation System": "https://github.com/sudharaD",
    "✅ Handwritten Digit Recognition-MNIST": "https://github.com/sudharaD",
    "✅ House Price Prediction": "https://github.com/sudharaD",
    "✅ Travel Mobile Application and Admin Dashboard": "https://github.com/sudharaD",
    "✅ Fitness Mobile Application": "https://github.com/sudharaD",
}

PROJECT_DES = [
    "Deep learning and Image processing-based system to detect skin diseases by analyzing images (CNN / Image Processing / Python / Open CV)",
    "A machine learning-based system that suggests similar movies based on user input (Python / NumPy / Pandas / sklearn)",
    "System that can accurately recognize and classify handwritten digits (Python / NumPy / Pandas / sklearn)",
    "A machine learning-based system that predicts house prices based on various features and attributes (Python / NumPy / Pandas / sklearn / Matplotlib)",
    "A comprehensive travel solution that includes a mobile application for users and an admin dashboard for managing travel-related functionalities. (Flutter / React / Firebase)",
    "A comprehensive mobile application designed to help users track and manage their fitness activities. (Java)"
]


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

# --- Skills ---
st.write("#")
st.subheader("Skills")
st.write("---")
st.write(
    """
- ✅ Programming Languages | Python
- ✅ Data Analysis and Visualization | Pandas, NumPy, Matplotlib, Seaborn
- ✅ Machine Learning | Scikit-learn, TensorFlow, Keras, PyTorch
- ✅ Big Data Tools | PySpark
- ✅ Database Technologies | Relational Databases (MySQL), NoSQL Databases (MongoDB)
- ✅ Deep Learning | Neural Networks, CNN
- ✅ Data Science Methods/Algorithms/Process | Supervised Learning, Unsupervised Learning, Time Series Analysis, Linear Regression, Decision Trees, Random Forest, Clustering, Neural Networks, Problem Formulation, Data Collection, Feature Selection, Model Training, Model Evaluation"
- ✅ Web Application Development: Streamlit
- ✅ Other | Version Control(Git, GitHub), Cloud Platforms(Microsoft Azure)
- ✅ Soft Skills | Self-Directed Learning, Team Player
- ✅ Languages | English, Sinhala 
    """
)

# --- Projects & Accomplishments ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
project_des_count = 0
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    st.write(PROJECT_DES[project_des_count])
    project_des_count += 1


# --- Experience and Qualifications ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write("---")
st.markdown("###### ✅ Virtusa (Pvt) Ltd| Quality Assurance Engineer Internship (08/2021 – 04/2022)")
st.write("Test Design, Manual Testing – British Telecommunications Project")
st.markdown("###### ✅ Arimac Lanka (Pvt) Ltd| Quality Assurance Engineer Internship (08/2022 – 02/2023)")
st.write("Performance Testing, Mobile Testing – People’s Bank Project, Sampath Bank Project, Rocell Bathware.lk, Sri Lankan Airline Project, SLT Mobitel Project")

# --- Coursework ---
st.write("#")
st.subheader("Coursework")
st.write("---")
st.write(
    """
- ✅ Data Science with Python | University of Colombo School of Computing
- ✅ Programming in Python - Python Programming | University of Moratuwa
- ✅ 100 Days of Code: The Complete Python Pro Bootcamp | Udemy
- ✅ Introduction to Data Science | SkillUP / simplilearn
- ✅ Introduction to Artificial Intelligence | SkillUP / simplilearn
- ✅ CI/CD for Beginners | SkillUP / simplilearn
- ✅ Python Libraries for Data Science | SkillUP / simplilearn
- ✅ Git and GitHub Crash Course | Udemy
- ✅ ISTQB - Foundation Level Certified Tester Examination (FL-CT) | ISTQB®
- ✅ HTML5 and CSS Fundamentals | edX
- ✅ Learn MySQL - For Beginners | Udemy
- ✅ Learn JavaScript - For Beginners |Udemy
- ✅ Teamwork & Collaboration | Rochester Institute of Technology | edX
- ✅ Critical Thinking & Problem Solving | Rochester Institute of Technology | edX
- ✅ Business Communication | Rochester Institute of Technology | edX
    """
)

# --- Other ---
st.write("#")
st.subheader("Other")
st.write("---")
st.write(
    """
- ✅ Microsoft Build: Azure AI Challenge 2023
- ✅ Hacktoberfest challenge - 2022

    """
)








