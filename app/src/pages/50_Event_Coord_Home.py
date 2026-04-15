import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

name = st.session_state.get('first_name', 'Coordinator')

st.title(f"Welcome, {name}!")
st.write("### Event Coordinator Workspace")
st.write("Plan new events, edit published ones, and manage RSVPs — all in one place.")

if st.button("Create a New Event", type='primary', use_container_width=True):
    st.switch_page('pages/51_Create_Event.py')

if st.button("Manage Existing Events", type='primary', use_container_width=True):
    st.switch_page('pages/52_Manage_Events.py')

if st.button("Manage Attendance / RSVPs", type='primary', use_container_width=True):
    st.switch_page('pages/54_Manage_Attendance.py')
