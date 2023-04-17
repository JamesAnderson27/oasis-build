import streamlit as st

import pandas as pd
import numpy as np
import random

import requests
import json

## LIVE SCRAPING - NPS

# Site Scrape
api_key='&api_key=Vsv3OfLMOGtoptQS7V5zvYIKawJZ29UbTErkVLgl'
url = 'https://developer.nps.gov/api/v1/campgrounds?stateCode=co'
limits='&start=0&limit=400'
r = requests.get(url+limits+api_key)
content = r.content
data = json.loads(content.decode('utf-8'))

name=[]
lat=[]
long=[]
p_code=[]
rez_type=[]
rez_link=[]
road = []
fee = []
trash = []
toilets = []
water = []
wood = []

for park in data["data"]:
    name.append(park["name"])
    lat.append(float(park["latitude"]))
    long.append(float(park["longitude"]))
    p_code.append(str(park["parkCode"]))
    road.append(park['accessibility']['accessRoads'])
    trash.append(park['amenities']['trashRecyclingCollection'])
    toilets.append(park['amenities']['toilets'][0])
    water.append(park['amenities']['potableWater'][0])
    wood.append(park['amenities']['firewoodForSale'])
    

    if len(park['fees'])>=1:
        fee.append(float(park['fees'][0]['cost']))
    else:
        fee.append('No Fee Recorded')
    
    
    n_res = int(park['numberOfSitesReservable'])
    n_fc = int(park['numberOfSitesFirstComeFirstServe'])
    
    if n_fc>0:
        rez_type.append('First-come-first-serve')
        rez_link.append(park['reservationUrl'])
    
        
    else:
        rez_type.append('Reservations Available')
        rez_link.append(park['reservationUrl'])

n = len(data['data'])
ids = np.arange(10,10+n)

site_dict={
    "id":ids,
    "park_name":name,
    "latitude":lat,
    "longitude":long,
    "park_code":p_code,
    "reserve":rez_type,
    "reserve_link":rez_link,
    "fee":fee,
    "road_conditions":road,
    "firewood":wood,
    "water":water,
    "trash":trash,
    "toilets":toilets
}

site_df = pd.DataFrame(site_dict)

# Alert Scrape
api_key='&api_key=Vsv3OfLMOGtoptQS7V5zvYIKawJZ29UbTErkVLgl'
url = 'https://developer.nps.gov/api/v1/alerts?stateCode=co'
limits='&start=0&limit=50'
r = requests.get(url+limits+api_key)
content = r.content
data = json.loads(content.decode('utf-8'))

title=[]
park_code=[]
message=[]

for i,item in enumerate(data['data']):
    title.append(item['title'])
    park_code.append(item['parkCode'])
    message.append(item['description'])
    
assert len(park_code)==len(message)==len(title)

alert_dict = {
    'title':title,
    'park_code':park_code,
    'message':message
}
alert_df = pd.DataFrame(alert_dict)

# HEADER
st.title('      :evergreen_tree:  :green[Welcome to Oasis!] :evergreen_tree:')
st.write('We provide a centralized pool of public information to inform your next trip into the *Great* Outdoors.\n\n\n')
st.write('**Directions: Select a campsite from the map and type the site ID into the box below.**\n')

# READ IN DB
#alert_df = pd.read_csv('DB_alerts.csv')
#site_df = pd.read_csv('DB_campsites.csv')


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


