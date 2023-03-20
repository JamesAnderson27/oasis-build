import streamlit as st

"""
# :evergreen_tree: Welcome to Oasis' Functional Dashboard! :evergreen_tree:
"""

with open('folium_map_copy.html','r') as f:
    html_read = f.read()

st.header("Prototype Map")
st.components.v1.html(html_read,height=400)

