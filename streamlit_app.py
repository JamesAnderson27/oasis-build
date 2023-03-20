import streamlit as st

"""
# :evergreen_tree: Welcome to Oasis! :evergreen_tree:

We provide a centralized pool of public information to inform your next trip into the *great* outdoors.
"""

with open('PRODUCT_foliummap.html','r') as f:
    html_read = f.read()

st.header("Prototype Map")
st.components.v1.html(html_read,height=400)

