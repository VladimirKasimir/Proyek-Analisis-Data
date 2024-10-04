import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('all_data.csv')

# Preprocess the data
df['dteday'] = pd.to_datetime(df['dteday'])
df['season'] = df['season'].map({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'})
df['weekday'] = df['weekday'].map({0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'})
df['yr'] = df['yr'].map({0: '2011', 1: '2012'})
df['weathersit'] = df['weathersit'].map({1: 'Clear', 2: 'Mist', 3: 'Light Snow/Rain', 4: 'Heavy Snow/Rain'})

# Streamlit dashboard layout
st.title("Bike Sharing Dashboard")

# Dropdowns for filtering by year, season, and weather condition
year = st.selectbox('Select Year', df['yr'].unique())
season = st.selectbox('Select Season', df['season'].unique())
weather = st.selectbox('Select Weather Condition', df['weathersit'].unique())

# Filter data based on selection
filtered_df = df[(df['yr'] == year) & (df['season'] == season) & (df['weathersit'] == weather)]

# User count over time
st.subheader("Total Users Over Time")
fig = px.line(filtered_df, x='dteday', y='cnt', title='Total Users Over Time', labels={'dteday': 'Date', 'cnt': 'Total Users'})
st.plotly_chart(fig)

# Seasonal analysis
st.subheader("User Count by Season")
season_df = df[df['yr'] == year]
fig2 = px.bar(season_df, x='season', y='cnt', color='season', barmode='group', title='User Count by Season', labels={'cnt': 'Total Users'})
st.plotly_chart(fig2)

# Weather analysis
st.subheader("User Count by Weather Condition")
weather_df = df[df['yr'] == year]
fig3 = px.pie(weather_df, names='weathersit', values='cnt', title='User Count by Weather Condition')
st.plotly_chart(fig3)

# Hourly usage analysis
st.subheader("User Count by Hour")
hourly_df = df[df['yr'] == year]
fig4 = px.line(hourly_df, x='hr', y='cnt', title='User Count by Hour', labels={'hr': 'Hour of Day', 'cnt': 'Total Users'})
st.plotly_chart(fig4)

# Day of the week analysis
st.subheader("User Count by Day of the Week")
weekday_df = df[df['yr'] == year]
fig5 = px.bar(weekday_df, x='weekday', y='cnt', color='weekday', title='User Count by Day of the Week', labels={'cnt': 'Total Users'})
st.plotly_chart(fig5)
