import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

st.write("# About this App")

st.markdown(
    """
    This is a demo application for the CampusConnector platform, a data-driven system designed to improve how events are created, managed, and experienced across campus.

    The goal of this demo is to showcase the different user roles within the system, including students, event coordinators, data analysts, and system administrators. Each role highlights a unique perspective, from discovering and managing events to analyzing engagement data and maintaining system performance.

    The app also demonstrates the underlying tech stack and how the frontend and backend work together to support real-time data, user interactions, and administrative control.

    Stay tuned for additional features, including personalized event recommendations, advanced analytics, and expanded system capabilities.
    """
)

# Add a button to return to home page
if st.button("Return to Home", type="primary"):
    st.switch_page("Home.py")
