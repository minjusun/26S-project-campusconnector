import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title('System Status Dashboard')

btn1, btn2 = st.columns(2)

with btn1:
    st.button("Run System Check", use_container_width=True, type="primary")

with btn2:
    st.button("View Detailed Report", use_container_width=True)

top1, top2, top3 = st.columns(3)

with top1:
    st.write("##### Overall Status")
    st.write("### Healthy")
    st.success("All critical services operational")

with top2:
    st.write("##### Last Full Check")
    st.write("### Today, 2:00 PM")
    st.caption("Next scan in 50 minutes")

with top3:
    st.write("##### Active Alerts")
    st.write("### 1 Warning")   
    st.caption("No critical incidents")

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

