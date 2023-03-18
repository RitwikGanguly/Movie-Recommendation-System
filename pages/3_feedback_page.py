import streamlit as st
from matplotlib import image
import pandas as pd
import os


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "feedback.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "feedback.csv")

st.set_page_config(page_title="FEEDBACK",
                   page_icon="☢",
                   layout="wide"
)
st.title("Feedback Page ❤🤍❤️")
img = image.imread(IMAGE_PATH)
st.image(img, width=700, caption="Your Feedback Matters")

df = pd.read_csv(DATA_PATH)

name = st.text_input("Your Name")
age = st.slider("Your Age", 10, 90, 18)
text = st.text_area("Your Feedback")

butt = st.button("submit")

if butt:
    pg = []
    pg.append(name)
    pg.append(age)
    pg.append(text)
    row = pd.Series(pg, index=df.columns)
    df = df.append(row, ignore_index=True)
    df.to_csv(DATA_PATH, index=False)
    st.write("Your feedback is recorded 😊😊")
else:
    st.write("Please submit your feedback....")


