import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Data Analyst, {st.session_state['first_name']}.")
st.write('### What would you like to do today?')

if st.button('Engagement Analytics Dashboard',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/32_Engagement_Analytics.py')

if st.button('Event Performance',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/33_Event_Performance.py')

if st.button('Insights & Predictions',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/34_Insights_Predictions.py')
