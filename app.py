import streamlit as st
from datetime import datetime,date,time
import requests
import pandas as pd
import numpy as np
#from geopy.geocoders import Nominatim
#from geopandas import gpd

# from streamlit_folium import folium_static
# import folium
# import os

st.markdown('''# How much will next taxi fare be?
## Input your destination. Let AI answer the question!
''')

# m = folium.Map(location=[47, 1], zoom_start=6)

# geojson_path = os.path.join("data", "departements.json")
# cities_path = os.path.join("data", "lewagon_cities.csv")

# for _, city in pd.read_csv(cities_path).iterrows():

#     folium.Marker(
#         location=[city.lat, city.lon],
#         popup=city.city,
#         icon=folium.Icon(color="red", icon="info-sign"),
#     ).add_to(m)

# def color_function(feat):
#     return "red" if int(feat["properties"]["code"][:1]) < 5 else "blue"

# folium.GeoJson(
#     geojson_path,
#     name="geojson",
#     style_function=lambda feat: {
#         "weight": 1,
#         "color": "black",
#         "opacity": 0.25,
#         "fillColor": color_function(feat),
#         "fillOpacity": 0.25,
#     },
#     highlight_function=lambda feat: {
#         "fillColor": color_function(feat),
#         "fillOpacity": .5,
#     },
#     tooltip=folium.GeoJsonTooltip(
#         fields=['code', 'nom'],
#         aliases=['Code', 'Name'],
#         localize=True
#     ),
# ).add_to(m)

# folium_static(m)

def geocode(address):
    params = { "q": address, 'format': 'json' }
    place = requests.get("https://nominatim.openstreetmap.org/search", params=params).json()
    return place[0]

date_ = st.date_input("Put your date",date(2022,4,29))
time_ = st.time_input("Put your time",time(11,30))
# pickup_logitude = st.text_input("Put your pickup longitude")
# pickup_latitude = st.text_input("Put your pickup latitude")
# dropoff_logitude = st.text_input("Put your dropoff longitude")
# dropoff_latitude = st.text_input("Put your dropoff latitude")
pickup_address = st.text_input('Put your pickup address')
dropoff_address = st.text_input('Put your dropoff address')
passenger_count = st.slider("Passenger count",1,9,2)


url = 'https://taxifare.lewagon.ai/predict'

params_filled = date_ and time_ and pickup_address and dropoff_address and passenger_count


if params_filled:
    params_ = {
            'pickup_datetime':datetime.combine(date_,time_),
            'pickup_longitude':geocode(pickup_address)['lon'],
            'pickup_latitude':geocode(pickup_address)['lat'],
            'dropoff_longitude':geocode(dropoff_address)['lon'],
            'dropoff_latitude':geocode(dropoff_address)['lat'],
            'passenger_count':passenger_count
    }


    response = requests.get(url,params=params_).json()

    st.json(response)


    # @st.cache
    # def get_map_data():

    #     return pd.DataFrame(
    #             np.array([[int(float(pickup_latitude)),int(float(pickup_logitude))],[int(float(dropoff_latitude)),int(float(dropoff_logitude))]]),
    #             columns=['lat', 'lon']
    #         )

    # df = get_map_data()

    # st.map(df)
