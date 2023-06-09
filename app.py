from pathlib import Path
import streamlit as st
from PIL import Image

# --- Path Settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assests"/"CV.pdf"
profile_pic = current_dir/"assests"/"profile-pic.png"
