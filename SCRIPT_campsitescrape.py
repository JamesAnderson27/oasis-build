

## 
import requests
import numpy as np
import pandas as pd
import json
import random

api_key='&api_key=Vsv3OfLMOGtoptQS7V5zvYIKawJZ29UbTErkVLgl'
url = 'https://developer.nps.gov/api/v1/campgrounds?stateCode=co'
limits='&start=0&limit=400'
r = requests.get(url+limits+api_key)
content = r.content
data = json.loads(content.decode('utf-8'))

name,lat,long,p_code,rez_type,rez_link,road,fee,trash,toilets,water,wood=[],[],[],[],[],[],[],[],[],[],[],[]

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

df = pd.DataFrame(site_dict)
df['reserve_link'] = df['reserve_link'].fillna('*No Link Available.*')
df['road_conditions'] = df['road_conditions'].apply(lambda x:x[0].strip("[]''"))
df.to_csv('DB_campsites.csv')