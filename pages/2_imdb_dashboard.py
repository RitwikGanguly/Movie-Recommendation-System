import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "imdb.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "yag.csv")

REC_FILE = os.path.join(dir_of_interest, "data", "record.csv")
st.set_page_config(page_title="Movie Dashboard",
                   page_icon="🎥",
                   layout="wide"
)

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
rg = pd.read_csv(REC_FILE)

l = df["Stars"].str.split(",")
df["first_name"] = l.str[:1]
df["first_name"] = df["first_name"].str[:].str[0]
df = df[df["start_year"] > 1700]

st.write("Do you wanna see the Dataframe:-")
yes = st.button("Yeah")
if yes:
    st.dataframe(df)
else:
    st.text("Not interested!!!!!!!!")

st.subheader("Now be ready for the Visualisation Part")

# draft templete

draft_template = go.layout.Template()
draft_template.layout.annotations = [
    dict(
        name="draft watermark",
        text="YAG",
        textangle=-30,
        opacity=0.1,
        font=dict(color="red", size=100),
        xref="paper",
        yref="paper",
        x=0.5,
        y=0.5,
        showarrow=False,
    )
]

l = {1:"histogram", 2: "bar", 3: "line", 4: "scatter", 5: "pie"}

s = ['all']
for i in range(2027, 1880, -1):
    s.append(i)
genre = ['all', 'comedy',
       'Sci-fi', 'horror', 'romance', 'action', 'thriller', 'drama', 'mystery',
       'crime', 'animation', 'adventure', 'fantasy', 'family', 'biography',
       'docum', 'film-noir', 'history', 'music', 'musical', 'short', 'sport',
       'superhero', 'war', 'western']
st.sidebar.header("The Input Section,Take Patience 😊")

options = st.sidebar.selectbox("Select the Option:", l.values())

g = st.sidebar.selectbox("Select the genre: ", genre)

y = st.sidebar.selectbox('Enter the year', s)

age = st.sidebar.slider("Your Age", 10, 90, 18)

butt = st.sidebar.button("submit")

if butt:
    pg = []
    pg.append(options)
    pg.append(g)
    pg.append(y)
    pg.append(age)
    row = pd.Series(pg, index=rg.columns)
    rg = rg.append(row, ignore_index=True)
    rg.to_csv(REC_FILE, index=False)







# histogram plot of certificate
col1, col2, col3, col4, col5 = st.columns(5)
if butt:
    if options == list(l.values())[0]:
        if g == "all" and y == "all":
            data = df[df["Certificate"] != "Not Certified"]
            data = data[data["Certificate"] != "Not Rated"]
            fig = px.histogram(data, x = "Certificate", title="<b> Year wise Certificates (HistPlot with Boxplot)\t <total count : {}> </b>".format(len(data)), marginal="box", template="ggplot2", color_discrete_sequence=["#AB63FA"])
            fig.update_layout(template = draft_template, paper_bgcolor = "black")
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="white"
            )

            col1.plotly_chart(fig, use_container_width=True)

        elif g == "all" and y != "all":
            data = df[df["start_year"] == int(y)]
            data = data[data["Certificate"] != "Not Certified"]
            data = data[data["Certificate"] != "Not Rated"]
            fig = px.histogram(data, x="Certificate",
                               title="<b> Year wise Certificates (HistPlot with Boxplot)\t <total count : {}> </b>".format(
                                   len(data)), color="start_year", marginal="box", template="ggplot2",
                               color_discrete_sequence=["#AB63FA"])
            fig.update_layout(template=draft_template, paper_bgcolor="black")
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="white"
            )
            col1.plotly_chart(fig, use_container_width=True)
        elif g != "all" and y == "all":
            data = df[df[g] == 1]
            data = data[data["Certificate"] != "Not Certified"]
            data = data[data["Certificate"] != "Not Rated"]
            fig = px.histogram(data, x="Certificate",
                               title="<b> Year wise Certificates (HistPlot with Boxplot)\t <{} count : {}> </b>".format(g,
                                                                                                                        len(data)),
                               color="start_year", marginal="box", template="ggplot2", color_discrete_sequence=["#AB63FA"])
            fig.update_layout(template=draft_template, paper_bgcolor="black")
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="white"
            )
            col1.plotly_chart(fig, use_container_width=True)
        else:
            data = df[df["start_year"] == int(y)]
            data = data[data[g] == 1]
            data = data[data["Certificate"] != "Not Certified"]
            data = data[data["Certificate"] != "Not Rated"]
            fig = px.histogram(data, x="Certificate",
                               title="<b> Year wise Certificates (HistPlot with Boxplot)\t <{} count : {}> </b>".format(g,
                                                                                                                        len(data)),
                               color="start_year", marginal="box", template="ggplot2", color_discrete_sequence=["#AB63FA"])
            fig.update_layout(template=draft_template, paper_bgcolor="black")
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="white"
            )
            col1.plotly_chart(fig, use_container_width=True)


    elif options == list(l.values())[1]:
        if y == "all" and g == "all":
            bar = df["first_name"].value_counts()[1:16]
            fig = px.bar(bar,
                         x=bar.index,
                         y=bar.values,
                         title="<b> Top 15 Stars Acted in movie in All genre, All Year </b>",
                         color_discrete_sequence=["#e31b9a"],
                         color="first_name",
                         height=800,
                         width=800
                         )
            fig.update_layout(template=draft_template, paper_bgcolor="black")
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                xaxis_title="Name of Stars",
                yaxis_title="Total no of Movies"
            )
            col2.plotly_chart(fig, use_container_width=True)

        elif g == "all" and y != "all":
            data = df[df["start_year"] == int(y)]
            bar = data["first_name"].value_counts()[1:16]
            fig = px.bar(bar,
                         x=bar.index,
                         y=bar.values,
                         title="<b> Top 15 Stars Acted in movie in All genre, Year - {} </b>".format(y),
                         color_discrete_sequence=["#AB63FA"],
                         color="first_name"
                         )
            fig.update_layout(template=draft_template, paper_bgcolor="black")
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                xaxis_title="Name of Stars",
                yaxis_title="Total no of Movies"
            )
            col2.plotly_chart(fig, use_container_width=True)

        elif g != "all" and y == "all":
            data = df[df[g] == 1]
            bar = data["first_name"].value_counts()[1:16]
            fig = px.bar(bar,
                         x=bar.index,
                         y=bar.values,
                         title="<b> Top 15 Stars Acted in movie in {} genre, All Year </b>".format(g),
                         color_discrete_sequence=["#AB63FA"],
                         color="first_name"
                         )
            fig.update_layout(template=draft_template, paper_bgcolor="black")
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                xaxis_title="Name of Stars",
                yaxis_title="Total no of Movies"
            )
            col2.plotly_chart(fig, use_container_width=True)

        else:
            data = df[df["start_year"] == int(y)]
            data = data[data[g] == 1]
            bar = data["first_name"].value_counts()[1:16]
            fig = px.bar(bar,
                         x=bar.index,
                         y=bar.values,
                         title="<b> Top 15 Stars Acted in movie in {} genre, {} Year </b>".format(g, y),
                         color_discrete_sequence=["#AB63FA"],
                         color="first_name",

                         )
            fig.update_layout(template=draft_template, paper_bgcolor="black")
            fig.update_layout(

                font_color="white",
                title_font_color="white",
                xaxis_title="Name of Stars",
                yaxis_title="Total no of Movies"
            )
            col2.plotly_chart(fig, use_container_width=True)

    elif options == list(l.values())[2]:
        if y == "all" and g == "all":
            line = df.groupby("start_year")["Time"].agg("sum").reset_index()
            fig = px.line(line, x="start_year", y="Time")
            fig.update_layout(template=draft_template, paper_bgcolor="black",
                              title="<b> Total Time of Movies in All year, All Genre </b>")
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="white"
            )
            fig.update_traces(mode='lines')
            col3.plotly_chart(fig, use_container_width=True)

        elif g == "all" and y != "all":
            data = df[df["start_year"] == y]
            line = data.groupby("start_year")["Time"].agg("sum").reset_index()
            fig = px.scatter(line, x="start_year", y="Time")
            fig.update_layout(template=draft_template, paper_bgcolor="black",
                              title="<b> Total Time of Movies in {} year, {} Genre </b>".format(y, g.upper()))
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="white"
            )
            col3.plotly_chart(fig, use_container_width=True)

        elif g != "all" and y == "all":
            data = df[df[g] == 1]
            line = data.groupby("start_year")["Time"].agg("sum").reset_index()
            fig = px.line(line, x="start_year", y="Time")
            fig.update_layout(template=draft_template, paper_bgcolor="black",
                              title="<b> Total Time of Movies in All year, {} Genre </b>".format(g.upper()))
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="white"
            )
            fig.update_traces(mode='lines')
            col3.plotly_chart(fig, use_container_width=True)
        else:
            data = df[df["start_year"] == y]
            data = data[data[g] == 1]
            line = data.groupby("start_year")["Time"].agg("sum").reset_index()
            fig = px.scatter(line, x="start_year", y="Time")
            fig.update_layout(template=draft_template, paper_bgcolor="black",
                              title="<b> Total Time of Movies in {} year, {} Genre </b>".format(y, g.upper()))
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="white"
            )
            col3.plotly_chart(fig, use_container_width=True)

    elif options == list(l.values())[3]:
        if g == "all" and y == "all":
            rg = df.groupby("start_year")["Rating"].mean().reset_index()
            fig = px.scatter(rg, x="start_year", y="Rating", color="start_year", size='Rating')
            fig.update_layout(template=draft_template, paper_bgcolor="black",
                              title="<b> Avarage Rating of Movies in All year, All Genre </b>")
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="white"
            )
            col3.plotly_chart(fig, use_container_width=True)

        elif g == "all" and y != "all":
            data = df[df["start_year"] == y]
            rg = data.groupby("start_year")["Rating"].mean().reset_index()
            fig = px.scatter(rg, x="start_year", y="Rating", color="start_year", size='Rating')
            fig.update_layout(template=draft_template, paper_bgcolor="black",
                              title="<b> Avarage Rating of Movies in {} year, All Genre </b>".format(y))
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="white"
            )
            col3.plotly_chart(fig, use_container_width=True)
        elif g != "all" and y == "all":
            data = df[df[g] == 1]
            rg = data.groupby("start_year")["Rating"].mean().reset_index()
            fig = px.scatter(rg, x="start_year", y="Rating", color="start_year", size='Rating')
            fig.update_layout(template=draft_template, paper_bgcolor="black",
                              title="<b> Avarage Rating of Movies in All year, {} Genre </b>".format(g))
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="white"
            )
            col3.plotly_chart(fig, use_container_width=True)
        else:
            data = df[df["start_year"] == y]
            data = data[data[g] == 1]
            rg = data.groupby("start_year")["Rating"].mean().reset_index()
            fig = px.scatter(rg, x="start_year", y="Rating", color="start_year", size='Rating')
            fig.update_layout(template=draft_template, paper_bgcolor="black",
                              title="<b> Avarage Rating of Movies in {} year, {} Genre </b>".format(y, g))
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="white"
            )
            col3.plotly_chart(fig, use_container_width=True)


    elif options == list(l.values())[4]:
        if g == "all" and y == "all":
            pie = df["tv_shows"].value_counts()
            fig = go.Figure(
                data=[go.Pie(labels=pie.index, values=pie.values, pull=[0, 0.2], hole=0.3, title="<b> YAG </b>")])
            fig.update_traces(textposition="inside", textinfo="percent+label")
            fig.update_layout(title="<b> Tv-Shows in All year </b>")
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="red"
            )
            col4.plotly_chart(fig, use_container_width=True)

        elif g == "all" and y != "all":
            data = df[df["start_year"] == y]
            pie = data["tv_shows"].value_counts()
            fig = go.Figure(
                data=[go.Pie(labels=pie.index, values=pie.values, pull=[0, 0.2], hole=0.3, title="<b> YAG </b>")])
            fig.update_traces(textposition="inside", textinfo="percent+label")
            fig.update_layout(title="<b> Tv-Shows in {} year </b>".format(y))
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="red"
            )
            col4.plotly_chart(fig, use_container_width=True)

        elif g != "all" and y == "all":
            data = df[df[g] == 1]
            pie = data["tv_shows"].value_counts()
            fig = go.Figure(
                data=[go.Pie(labels=pie.index, values=pie.values, pull=[0, 0.2], hole=0.3, title="<b> YAG </b>")])
            fig.update_traces(textposition="inside", textinfo="percent+label")
            fig.update_layout(title="<b> Tv-Shows in {} genre </b>".format(g))
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="red"
            )
            col4.plotly_chart(fig, use_container_width=True)

        else:
            data = df[df["start_year"] == y]
            data = data[data[g] == 1]
            pie = data["tv_shows"].value_counts()
            fig = go.Figure(
                data=[go.Pie(labels=pie.index, values=pie.values, pull=[0, 0.2], hole=0.3, title="<b> YAG </b>")])
            fig.update_traces(textposition="inside", textinfo="percent+label")
            fig.update_layout(title="<b> Tv-Shows in {} year and {} genre</b>".format(y, g))
            fig.update_layout(
                font_color="white",
                title_font_color="white",
                legend_title_font_color="red"
            )
            col4.plotly_chart(fig, use_container_width=True)

    st.write("Thanks 😊😊")
    st.write("Have a good day")

else:
    st.sidebar.write("Hey!! Submit Your Choices")




st.subheader("🙏 Please submit your feedback at the Next page 🙏")










