import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title('System Status Dashboard')

top1, top2, top3 = st.columns(3)

with top1:
    st.write("##### Last Backup")
    st.write("### March 29, 2026 -")
    st.write("### 02:00 AM")
    st.success("Successful")

with top2:
    st.write("##### Backup Schedule")
    st.write("### Daily (2:00 AM)")
    st.caption("Next backup in 6 hours")

with top3:
    st.write("##### Storage Usage")
    st.write("### 65% used")
    st.progress(0.65)
    st.caption("120 GB / 200 GB")