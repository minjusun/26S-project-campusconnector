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

left_col, right_col = st.columns([2.2, 1])

with left_col:
    with st.container(border=True):
        st.markdown("### System Health")

        health_items = [
            ("Database integrity", "Last run: 2 hours ago", "ok"),
            ("File system consistency", "Last run: 2 hours ago", "ok"),
            ("Backup encryption", "Last run: 2 hours ago", "ok"),
            ("Storage capacity", "Last run: 2 hours ago", "warning"),
            ("Network connectivity", "Last run: 5 minutes ago", "ok"),
        ]

        for title, subtitle, status in health_items:
            icon = "🟢" if status == "ok" else "🟠"

            col1, col2 = st.columns([0.1, 0.8])

            with col1:
             st.write(icon)

             with col2:
                st.write(f"**{title}**")
                st.caption(subtitle)

            st.divider()