import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

name = st.session_state.get('first_name', 'Student')

st.title(f"Welcome, {name}!")
st.write("### What do you want to do?")
st.write("Browse what's coming up on campus and RSVP to stuff you wanna go to.")

if st.button("Browse Upcoming Events", type='primary', use_container_width=True):
    st.switch_page('pages/41_Browse_Events.py')

if st.button("See My Events", type='primary', use_container_width=True):
    st.switch_page('pages/43_My_Events.py')

if st.button("Check Notifications", type='primary', use_container_width=True):
    st.switch_page('pages/44_Notifications.py')
