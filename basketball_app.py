import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json

st.title('NBA 2K League Player Stats Explorer')

st.markdown("""
This app performs simple webscraping of NBA 2K League player stats data!
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [NBA 2K League Website](https://2kleague.nba.com/stats/).
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(2018,2022))))

# Web scraping of NBA 2K League player stats
@st.cache
def load_data(year):
    url = "https://data.nba.com/data/10s/v2015/json/mobile_teams/2KL/2021/league/stats/12_league_leaders_points_02.json"
    html = pd.read_html(url, header = 0)
    df = html[0]
   

# Sidebar - Team selection
sorted_unique_team = sorted(())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# Sidebar - Position selection
unique_pos = ['C','PF','SF','PG','SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filtering data
#df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
st.dataframe(df_selected_team)

# Download NBA player stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

