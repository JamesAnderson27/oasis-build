import streamlit as st

import pandas as pd
import numpy as np
import random

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
st.components.v1.html(html_read,height=400)


st.write('Hello world!')

# CAMPSITE SELECT AND DISPLAY
st.write('**Directions: Select a campsite from the map and type the site ID into the box below.**\n')
st.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Campsites in :green[Green] are First-come-first-serve.*')
st.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Campsites in :blue[Blue] have reservations available.*')

site_code = st.number_input('Enter campsite number',
    min_value=int(10),
    max_value=int(39),
    step=1)
st.write('Selected campsite:', site_code)

if st.button('Click for details'):

    # PLACE HOLDER FOR DB READING
    site = site_df[site_df['id']==site_code].values[0]
    site_name = site[2]
    #site_alerts = alert_lister()
    site_forecast = {}
    site_coord = (site[3],site[4])
    p_code=site[5]
    rez_type=site[6]
    rez_link=site[7]
    fee=site[8]
    road_c = site[9].strip("'[]")

    st.subheader('\n')
    st.header(site_name)
    st.write('***'+(rez_type)+'  |  '+str(road_c)+'  |  '+str(fee)+' Fee***')
    st.code('coord --> '+str(site_coord))
    st.subheader('\n')


    ## Amenity Display 
        # :potable_water:
        # :wood:
        # :wastebasket:
        # :toilet:

    am_dict = {}
    firewood = site[9]
    water = site[10]
    trash = site[11]
    toilets = site[12]

    if 'Yes' in firewood:
        am_dict['wood']=True
    else:
        am_dict['wood']=False
    if 'No' in water:
        am_dict['water']=False
    else:
        am_dict['water']=True
    if 'No' in toilets:
        am_dict['toilets']=False
    else:
        am_dict['toilets']=True
    if 'No' in trash:
        am_dict['trash']=False
    else:
        am_dict['trash']=True

    st.metric(':toilet:')
    
    st.write('To visit the public website & make reservations, click the link below.')
    st.write(rez_link)
    st.subheader('\n')

    st.write(':red[Daily Alerts] ')
    alert_list = list(alert_df.loc[alert_df['park_code']==p_code,['message']]['message'].values)
    for i,a in enumerate(alert_list):
        st.write(':red['+str(i+1)+']','. '+str(a))
        st.subheader('\n')



