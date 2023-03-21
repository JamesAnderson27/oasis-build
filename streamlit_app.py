import streamlit as st

import pandas as pd
import numpy as np

import requests
import json



# HEADER
st.title('      :evergreen_tree:  :green[Welcome to Oasis!] :evergreen_tree:')
st.write('We provide a centralized pool of public information to inform your next trip into the *Great* Outdoors.')


# READ IN DB
alert_df = pd.read_csv('DB_alerts.csv')
site_df = pd.read_csv('DB_campsites.csv')
#forecast_df = pd.read('DB_forecast')


# DISPLAY FOLIUM MAP
with open('PRODUCT_foliummap.html','r') as f:
    html_read = f.read()
st.header("Map")
st.components.v1.html(html_read,height=400)


# CAMPSITE SELECT AND DISPLAY
site_code = st.number_input('Enter campsite number',
    min_value=int(10),
    max_value=int(39),
    step=1)
st.write('Selected campsite:', site_code)

st.table(site_df)

if st.button('Click for details'):

    # PLACE HOLDER FOR DB READING
    site_name = 'Cimarron Campground'
    site_alerts = ['Black Bears in the area.']
    site_forecast = {}
    site_coord = (23.3253,75.3452)

    p_code='grsa'

    st.subheader(site_name)
    st.code(site_coord)
    #st.write('Daily Forecast: ', site_weather['prec_type'])
    st.write(':orange[Daily Alerts] ')

    alert_list = list(alert_df.loc[alert_df['park_code']==p_code,['message']]['message'].values)
    for i,a in enumerate(alert_list):
        st.write(i,'. ',a)



