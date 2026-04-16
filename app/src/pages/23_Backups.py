import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title('Backups Dashboard')

top1, top2, top3 = st.columns(3)

with top1:
    st.write("##### Last Backup")
    st.write("### March 29, 2026")
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
    
st.markdown("")

st.markdown("### Backup History")
backup_data = [
    ("March 29, 2026", "02:00 AM", "Success", "3 GB"),
    ("March 28, 2026", "02:00 AM", "Success", "7.5 GB"),
    ("March 27, 2026", "02:00 AM", "Success", "2.5 GB"),
    ("March 26, 2026", "02:00 AM", "Failed", "N/A"),
    ("March 25, 2026", "02:00 AM", "Success", "1.4 GB"),
]

with st.container(border=True):

    # Header row
    col1, col2, col3 = st.columns([3, 2, 1])
    col1.markdown("**DATE & TIME**")
    col2.markdown("**STATUS**")
    col3.markdown("**SIZE**")

    st.divider()

for date, time, status, size in backup_data:
        col1, col2, col3 = st.columns([3, 2, 1])

        with col1:
            st.markdown(f"**{date}**")
            st.caption(time)

        with col2:
            if status == "Success":
                st.success("Success")
            else:
                st.error("Failed")

        with col3:
            st.write(size)

        st.divider()