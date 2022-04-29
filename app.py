import streamlit as st
from datetime import datetime,date,time
import requests
import pandas as pd
import numpy as np

st.markdown('''# How much will next taxi fare be?
## Input your destination. Let AI answer the question!
''')

df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)


date_ = st.date_input("Put your date",date(2022,4,29))
time_ = st.time_input("Put your time",time(11,30))
pickup_logitude = st.text_input("Put your pickup longitude")
pickup_latitude = st.text_input("Put your pickup latitude")
dropoff_longitude = st.text_input("Put your dropoff longitude")
dropoff_latitude = st.text_input("Put your dropoff latitude")
passenger_count = st.slider("Passenger count",1,9,2)


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('API from lewagon')


params = {
    'pickup_datetime':datetime.combine(date_,time_),
    'pickup_longitude':pickup_logitude,
    'pickup_latitude':pickup_latitude,
    'dropoff_longitude':dropoff_longitude,
    'dropoff_latitude':dropoff_latitude,
    'passenger_count':passenger_count
}

response = requests.get(url,params=params).json()

st.json(response)
