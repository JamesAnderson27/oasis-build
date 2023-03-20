from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# :evergreen_tree: Welcome to Oasis! :evergreen_tree:

This mockup was creating using Streamlit. This service allows us to create functional webpages without front-end expertise.  

:campfire:     File Path -->  '/streamlit_app.py'     :campfire:


In the meantime, below is an example of what you can do with just a few lines of code:
"""

with open('map_copy.html','r') as f:
    html_read = f.read()

st.componenets.html(html_read)