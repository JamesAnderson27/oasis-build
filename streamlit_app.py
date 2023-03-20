import streamlit as st
import pandas as pd



st.title('      :evergreen_tree:  :green[Welcome to Oasis!] :evergreen_tree:')
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
st.write(df)



site_code = ' '
site_code = st.number_input('Enter a campsite code',
    min_value=int(0),
    max_value=int(10),
    step=1)

st.write('The current campsite is ', site_code)

message_list = ['You picked campsite #1!','You picked campsite #2!']
if st.button('Click for details.'):
    st.write('You selected: ',message_list[int(site_code)])