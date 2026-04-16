import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title("System Logs")
st.caption("Monitor system events, user activity, warnings, and errors.")

top1, top2, top3 = st.columns(3)

with top1:
    st.write("##### Total Logs")
    st.write("### 128")
    st.caption("Last 7 days")

with top2:
    st.write("##### Errors")
    st.write("### 12")
    st.error("3 new today")

with top3:
    st.write("##### Warnings")
    st.write("### 27")
    st.warning("5 require review")

st.markdown("")

st.markdown("### Recent Logs")

log_data = [
    ("Apr 16, 2026", "10:15 AM", "INFO", "Backup Service", "Backup completed"),
    ("Apr 16, 2026", "9:42 AM", "WARNING", "Auth Service", "Multiple failed logins"),
    ("Apr 16, 2026", "8:03 AM", "ERROR", "Database", "Connection timeout"),
    ("Apr 15, 2026", "10:14 PM", "INFO", "Event Manager", "Event updated"),
    ("Apr 15, 2026", "6:27 PM", "ERROR", "Storage", "Low disk space"),
]

st.table(
    {
        "Date": [row[0] for row in log_data],
        "Time": [row[1] for row in log_data],
        "Level": [row[2] for row in log_data],
        "Service": [row[3] for row in log_data],
        "Action": [row[4] for row in log_data],
    }
)

st.markdown("")

st.download_button(
    label="Export Logs",
    data="Sample log export",
    file_name="system_logs.txt",
    mime="text/plain"
)