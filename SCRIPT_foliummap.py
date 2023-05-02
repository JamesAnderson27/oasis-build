## Sample code for Folium map build

- Using GeoPandas and Folium to render an interactive map
- Reading from a file with a list of campgrounds and their latitudes
    
Resources
- https://python-visualization.github.io/folium/quickstart.html#Markers
- https://medium.com/geekculture/how-to-create-interactive-maps-using-folium-b2a6f6d731b8
_________________________________________________________________________________________

import pandas as pd
import geopandas as gpd
import json
import folium as f

def save_map(map_name,html_name):
    from IPython.display import IFrame
    m.save(file_name)
    return IFrame(file_name, width='100%', height='500px')

df = pd.read_csv('DB_campsites.csv')
gdf = gpd.GeoDataFrame(
    
        df, geometry = gpd.points_from_xy(
            df.longitude,
            df.latitude
        ),
    
        columns=[
             'id',
             'park_name',
             'latitude',
             'longitude',
             'geometry',
            'reserve']
)

map_ = f.Map(location=[39.1993,-105.5930],
             zoom_start=6.5,
             tiles='openstreetmap'
            )

marker_icon='fire'

for i in range(len(gdf)):
    site = gdf.loc[i,['park_name','latitude','longitude','id','reserve']]
    site_name = site[0]
    long = site[1]
    lat = site[2]
    id_ = site[3]
    rez = site[4]
    
    if rez == 'First-come-first-serve':
        marker_color='darkgreen'
    if rez == 'Reservations Available':
        marker_color='darkblue'
    
    f.Marker(
        [long,lat],
        popup="<h6>{}: {}</h6>\n<body>{}".format(id_,site_name,rez),
        icon = f.Icon(
                     color=marker_color,
                     prefix='fa',
                     icon=marker_icon
                          )
    ).add_to(map_)

map_.save('PRODUCT_foliummap.html')