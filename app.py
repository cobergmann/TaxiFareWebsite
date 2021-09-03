import streamlit as st
from streamlit_folium import folium_static

import requests
import numpy as np
import pandas as pd
import folium

'''
# TaxiFareModel front
'''

# date = st.date_input("Pick-up date")
# time = st.time_input("Pick-up time")
# pickup_datetime = str(date) + ' ' + str(time)
# pickup_longitude = st.text_input('pickup longitude')
# pickup_latitude = st.text_input('pickup latitude')
# dropoff_longitude = st.text_input('dropoff longitude')
# dropoff_latitude = st.text_input('dropoff latitude')
# passenger_count = st.slider('Passenger count', 1, 8)

date = st.sidebar.date_input("Pick-up date")
time = st.sidebar.time_input("Pick-up time")
pickup_datetime = str(date) + ' ' + str(time)
pickup_longitude = st.sidebar.text_input('pickup longitude')
pickup_latitude = st.sidebar.text_input('pickup latitude')
dropoff_longitude = st.sidebar.text_input('dropoff longitude')
dropoff_latitude = st.sidebar.text_input('dropoff latitude')
passenger_count = st.sidebar.slider('Passenger count', 1, 8)


url = 'https://taxifare.lewagon.ai/predict'

params = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

pickup = [pickup_longitude, pickup_latitude]
dropoff = [dropoff_longitude, dropoff_latitude]

if st.button('Predict'):

    m = folium.Map(location=[40.7850, -73.9682], zoom_start=11)

    folium.Marker(location=pickup,
                  popup='Pickup',
                  icon=folium.Icon(color='red', icon='angry')
                  ).add_to(m)

    folium.Marker(location=dropoff,
                  popup='Dropoff',
                  icon=folium.Icon(color='green', icon='angry')
                  ).add_to(m)

    #folium.PolyLine([tuple(pickup), tuple(dropoff)]).add_to(m)

    folium_static(m)

    response = requests.get(url, params=params)
    if response.status_code == requests.codes.ok:
        response = response.json()
        prediction = response['prediction']
        st.write('Predicted fare:', np.round(prediction,3), '$')
    else:
        st.error('''Sorry, there was an error in your request. Please try again or
              contact customer support.''')



# pickup_datetime=2012-10-06%2012:10:20
# pickup_longitude=40.7614327
# pickup_latitude=-73.9798156
# dropoff_longitude=40.6513111
# dropoff_latitude=-73.8803331
# passenger_count=2
