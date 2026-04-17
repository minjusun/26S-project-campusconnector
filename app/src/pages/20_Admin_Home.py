import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()



st.title('System Administrator Home Page')
st.write('### What would you like to do today?')

if st.button('Administrator Dashboard',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/21_Administrator_Dashboard.py')

if st.button('System Status',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/22_System_Status.py')

if st.button('Backups',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/23_Backups.py')
    
if st.button('Logs',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/24_Logs.py')

if st.button('User Management',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/25_Admin_User_Management.py')