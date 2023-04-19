import streamlit as st
import pandas as pd
import subprocess
import sys

subprocess.run([f"{sys.executable}", "SCRIPT_alertscrape.py"])
subprocess.run([f"{sys.executable}", "SCRIPT_campsitescrape.py"])
subprocess.run([f"{sys.executable}", "SCRIPT_foliummap.py"])

## PLACEHOLDER

# HEADER
st.title('      :evergreen_tree:  :green[Welcome to Oasis!] :evergreen_tree:')
st.write('We provide a centralized pool of public information to inform your next trip into the *Great* Outdoors.\n\n\n')
st.write('**Directions: Select a campsite from the map and type the site ID into the box below.**\n')

# READ IN DB
alert_df = pd.read_csv('DB_alerts.csv')
site_df = pd.read_csv('DB_campsites.csv')


# DISPLAY FOLIUM MAP
with open('PRODUCT_foliummap.html','r') as f:
    html_read = f.read()
st.components.v1.html(html_read,height=400)

# CAMPSITE SELECT AND DISPLAY
st.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Campsites in :green[Green] are First-come-first-serve.*')
st.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Campsites in :blue[Blue] have reservations available.*')

site_code = st.number_input('Enter campsite number',
    min_value=int(10),
    max_value=int(39),
    step=1)
st.write('Selected campsite:', site_code)

if st.button('Click for details'):

    site = site_df[site_df['id']==site_code].values[0]
    site_name = site[2]

    site_coord = (site[3],site[4])
    p_code=site[5]
    rez_type=site[6]
    rez_link=site[7]
    fee=site[8]
    road_c = site[9].strip("'[]")

    am_dict = {}
    firewood = site[10]
    water = site[11]
    trash = site[12]
    toilets = site[13]

    st.subheader('\n')
    st.header(str(site_name))

    ## Amenity Display 
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

    am_string = 'Amenities:  | '
    if am_dict['wood']:
        am_string = am_string+'&nbsp;&nbsp;&nbsp;&nbsp;:wood:&nbsp;&nbsp;&nbsp;&nbsp;|'
    if am_dict['water']:
        am_string = am_string+'&nbsp;&nbsp;&nbsp;&nbsp;:potable_water:&nbsp;&nbsp;&nbsp;&nbsp;|'
    if am_dict['toilets']:
        am_string = am_string+'&nbsp;&nbsp;&nbsp;&nbsp;:toilet:&nbsp;&nbsp;&nbsp;&nbsp;|'
    if am_dict['trash']:
        am_string = am_string+'&nbsp;&nbsp;&nbsp;&nbsp;:wastebasket:&nbsp;&nbsp;&nbsp;&nbsp;|'

    st.subheader(am_string)
    st.write('***'+(rez_type)+'  |  '+str(road_c)+'  |  '+str(fee)+' Fee***')
    st.subheader('\n')
    
    st.write('To visit the public website & make reservations, click the link below.')
    st.write(rez_link)
    st.subheader('\n')

    st.write(':red[Daily Alerts] ')
    alert_list = list(alert_df.loc[alert_df['park_code']==p_code,['message']]['message'].values)
    for i,a in enumerate(alert_list):
        st.write(':red['+str(i+1)+']','. '+str(a))
        st.subheader('\n')

    st.code('coord -> '+str(site_coord))


