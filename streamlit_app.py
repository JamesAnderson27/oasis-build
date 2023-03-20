import streamlit as st

"""
# :evergreen_tree: Welcome to Oasis' Dashboard! :evergreen_tree:
"""

with open('PRODUCT_foliummap.html','r') as f:
    html_read = f.read()

st.header("Prototype Map")
st.components.v1.html(html_read,height=400)

