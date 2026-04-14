import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title('App Administration Page')

st.write('## Model 1 Maintenance')

if st.button('System Status',
             type='primary',
             use_container_width=True):
    results = requests.get('http://web-api:4000/prediction/10/25').json()
    st.dataframe(results)
