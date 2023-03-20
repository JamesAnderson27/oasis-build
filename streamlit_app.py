import streamlit as st
import pandas as pd

st.title('<div style="text-align: center;">#evergreen_tree:  :green[Welcome to Oasis!] :evergreen_tree:</div>', unsafe_allow_html=True)

st.write('We provide a centralized pool of public information to inform your next trip into the *Great* Outdoors.')

with open('PRODUCT_foliummap.html','r') as f:
    html_read = f.read()

st.header("Prototype Map")
st.components.v1.html(html_read,height=400)

st.write("Here's our first attempt at using data to create a table:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.table(df)
st.write(df)