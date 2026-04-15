import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

name = st.session_state.get('first_name', 'Student')

st.title(f"Welcome, {name}!")
st.write("### What would you like to do today?")
st.write("Find events that match your interests, RSVP in one click, and keep track of your schedule.")

if st.button("Browse Upcoming Events", type='primary', use_container_width=True):
    st.switch_page('pages/41_Browse_Events.py')

if st.button("See My Events", type='primary', use_container_width=True):
    st.switch_page('pages/43_My_Events.py')

if st.button("Check Notifications", type='primary', use_container_width=True):
    st.switch_page('pages/44_Notifications.py')
