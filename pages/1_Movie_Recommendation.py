import streamlit as st
from matplotlib import image
import os
import time
import pickle
import pandas as pd


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "mr.jpeg")
# def_img = os.path.join(dir_of_interest, "images", "download.png")

st.set_page_config(page_title="PickYourMovie",
                   page_icon="🎬",
                   layout="wide"
)
st.title("Know Your Movie 🍿📽️🍿")

img = image.imread(IMAGE_PATH)
# noimg = image.imread(def_img)
st.image(img, width=700, caption="Movie Recommendation System")

data_path = os.path.join(dir_of_interest, "data", "data_fm.pkl")

movies_dict = pickle.load(open(data_path, 'rb'))

movies_list = pd.DataFrame(movies_dict)

movies = movies_list["Movies"].values

selected_movie_name = st.selectbox("👉 Gather Your Choices:- ", movies)
st.write("👉 do you wanna see :red[_THEMAGIC_] 🤩🤩")
butt = st.button("Yeah!!!")
# Web scraping section ---------------------------------------------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome(executable_path=r'C:\Users\RITWIK GANGULY\anaconda3\chromedriver.exe')
# driver.maximize_window()
#
# def img_url(a):
#     p = []
#     driver.get("https://www.google.com/?&bih=746&biw=1536&hl=en")
#     try:
#         driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').clear()
#         driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(a)
#
#     except:
#         driver.find_element(By.XPATH, '//*[@id="APjFqb"]').clear()
#         driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys(a)
#
#     driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
#     try:
#         image = driver.find_element(By.XPATH, '//*[@id="tsuid_32"]').get_attribute('src')
#         p.append(image)
#
#
#     except:
#
#         try:
#             # for 2nd position
#             driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
#             image = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').get_attribute('src')
#             p.append(image)
#
#
#         except:
#             # for 1st position
#             st.image(noimg)
#
#
#     # img = Image.open(urlopen(p[0]))
#     # print(img)
#     return p

# NLP section --------------------------------------------------------------------------------------------------

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=8500, stop_words="english")

vectors = cv.fit_transform(movies_list["tags"]).toarray()

from sklearn.metrics.pairwise import cosine_similarity
similar = cosine_similarity(vectors)

# ------------------------------------------------------------------------------------------------------------------

def recommand(movie):
    movie_index = movies_list[movies_list["Movies"] == movie].index[0]
    dist = similar[movie_index]
    ch = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]

    mr = []
    for i in ch:
        mr.append(movies_list.iloc[i[0]].Movies)

    return mr
movie_index = movies_list[movies_list["Movies"] == selected_movie_name].index[0]
if butt:
    with st.spinner('Take patience, wait for it.....'):
        time.sleep(5)
    st.success('Done!')
    st.write("Your entered movie details:-")
    st.write("Your Movie Name - ", selected_movie_name)
    # try:
    #     url = img_url(selected_movie_name)
    #     st.image(url[0], width=200)
    #
    # except:
    #     pass
    st.write("Lead Star - ", movies_list.iloc[movie_index].first_name)
    st.write("Director - ", movies_list.iloc[movie_index].Director)
    st.write("Rating - ", movies_list.iloc[movie_index].Rating)
    st.write("TV-Show Type - ", movies_list.iloc[movie_index].tv_shows)
    st.write("Tags - ", movies_list.iloc[movie_index].tags)

    st.markdown("Your movie link - {}".format(movies_list.iloc[movie_index].imb_link))
    st.subheader("The Top 5 listed Movies of High rating(Rating > 7.0)")
    recom = recommand(selected_movie_name)

    for i in range(len(recom)):
        st.write("{}) {}".format(i+1, recom[i]))

        # try:
        #     url = img_url(recom[i])
        #     st.image(url[0], width=200)
        #
        # except:
        #     pass
        idx = movies_list[movies_list["Movies"] == recom[i]].index[0]
        st.write("Lead Star - ", movies_list.iloc[idx].first_name)
        st.write("Director - ", movies_list.iloc[idx].Director)
        st.write("Rating - ", movies_list.iloc[idx].Rating)
        st.write("TV-Show Type - ", movies_list.iloc[idx].tv_shows)
        st.write("Tags - ", movies_list.iloc[idx].tags)
        link = movies_list.iloc[idx].imb_link
        st.markdown("Movie link - {}".format(link), unsafe_allow_html=True)

    st.subheader("Hope You Enjoyed 🙄🙄")

    # driver.close()



