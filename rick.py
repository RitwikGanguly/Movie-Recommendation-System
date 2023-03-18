import streamlit as st
from PIL import Image
import os

from pathlib import Path


# cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# prof_pic = cur_dir / "assets" / "ricky.jpg"

cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
prof_pic = cur_dir / "assets" / "mypic.jpg"


# Description
PAGE_TITLE = "MOVIE RECOMMENDATION SYSTEM"
PAGE_ICON = "✨"
NAME = "Ritwik Ganguly"
DESCRIPTION = """
I am a CSE student, currently in 3rd year and enthusiastic in data science, data analysis & Machine Learning, aspire to learn new thing at every second. 
"""
EMAIL = "gangulyritwik2003@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/ritwikganguly003",
    "GitHub": "https://github.com/RitwikGanguly",
}
PROJECTS_REQUIRMENTS_DONE= {
    "🍿🍿 The Things are done so far for this project......",
    "🏆 Scraping the raw data from https://www.imdb.com/ through selenium and with python programming language",
    "🏆 Cleaning and do all the preprocessing task through pandas library of python to get a clean dataframe",
    "🏆 Done all the visualization task for the imdb_dashboard through plotly library of python"
    "🏆 Making the model through NLP(natural language processing), to get the desired insight 😊"
    "🏆 Last but not the list make the website through streamlit framework through python and deploy in "
    "streamlit app."
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hi!! :red[Everyone]")
st.subheader("welcome all, let's enjoy together😎😎😎😎")

# Load css, pdf and profile pic

# with open(css_file) as f:
#     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

prof = Image.open(prof_pic)


# Header section

col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(prof, width=220)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📩", EMAIL)

st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write('\n')
st.subheader("Knowledge & Self-declaration ")
st.write(
    """
- ✔️ Currently a student, studied in 3rd year
- ✔️ Intermediate knowledge in python, still exploring and trying to grasp a good hand in python
- ✔️ Has understanding in data science and trying to find the hardness behind the easy word ML 
- ✔️ Has team management and problem solving capability
- ✔️ Always try to learn new things through challenges and tasks 
- ✔️ Some time get confused to himself and has somewhat little patience
"""
)
st.subheader("Project Name - Movie Recommendation System")
st.subheader("Project Requirements ...............")
st.write(
    """
- 🍿🍿 The Things are done so far for this project-----------------------------------------------------------
- 🏆 Scraping the raw data from https://www.imdb.com/ by selenium and with python programming language
- 🏆 Cleaning and do all the preprocessing task through pandas library of python to get a clean dataframe
- 🏆 Done all the visualization task for the imdb_dashboard through plotly library of python
- 🏆 Making the model through NLP(natural language processing), to get the desired insight 😊
- 🏆 Last but not the list make the website through streamlit framework through python 

"""
)




st.subheader("Some Points I must say...")

st.write(
    """
- 👉 The website is somewhat slow so please take patience and enjoy the beauty of this project.
- 👉 There are total 4 pages including this page, please do submit the feedback at the end.
- 👉 I will add more stuffs in this webpage later point of time, do patience. 
- 👉 some time the images of some movies will not load due to server issue but after refresh you may see those images 😒
- 👉 Lastly at the recommendation it may take some time so please take patience
- 👉 This is not build commercial purposes, it's totally build to get knowledge 😊😊 

"""
)

st.subheader("👉 THE GITHUB LINK OF THIS PROJECT: {}".format("https://github.com/RitwikGanguly/Movie-Recommendation-System"))






