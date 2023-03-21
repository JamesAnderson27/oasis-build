import streamlit as st
import pandas as pd


# HEADER
st.title('      :evergreen_tree:  :green[Welcome to Oasis!] :evergreen_tree:')
st.write('We provide a centralized pool of public information to inform your next trip into the *Great* Outdoors.')


# DISPLAY FOLIUM MAP
with open('PRODUCT_foliummap.html','r') as f:
    html_read = f.read()
st.header("Prototype Map")
st.components.v1.html(html_read,height=400)


# CAMPSITE SELECT AND DISPLAY
site_code = st.number_input('Enter a campsite code',
    min_value=int(0),
    max_value=int(10),
    step=1)
st.write('The selected campsite is ', site_code)
message_list = ['You picked campsite #1!','You picked campsite #2!']
if st.button('Click for details'):
    st.write('You selected: ',message_list[int(site_code)])

    # PLACE HOLDER FOR DB READING
    site_name = 'Cimarron Campground'
    site_alerts = ['Black Bears in the area.']
    site_weather = {'prec_type':':sun:'}
    site_coord = (23.3253,75.3452)

    st.subheader(site_name)
    st.code('Coordinates 'site_coord)
    st.write('Daily Forecast: ', site_weather['prec_type'])
    st.write('Daily Alerts: ', site_alerts)



