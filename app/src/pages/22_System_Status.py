import os
import logging
logger = logging.getLogger(__name__)

import streamlit as st
from datetime import date
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

API = os.environ.get("WEB_API_URL", "http://localhost:4000")

# fetch backend data
try:
    users = requests.get(f"{API}/users", timeout=5).json()
    events = requests.get(f"{API}/events", timeout=5).json()
    logs = requests.get(f"{API}/logs", timeout=5).json()
except:
    users, events, logs = [], [], []


# system metrics
total_users = len(users)
total_events = len(events)
total_logs = len(logs)

latest_logs = logs[:10]


# system status
if logs:
    system_status = "Healthy"
else:
    system_status = "Unknown"


# page header
st.title("System Status Dashboard")
st.write("### Live system monitoring")


# top metrics
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.write("##### Users")
    st.write(f"### {total_users}")

with c2:
    st.write("##### Events")
    st.write(f"### {total_events}")

with c3:
    st.write("##### Logs")
    st.write(f"### {total_logs}")

with c4:
    st.write("##### Status")
    st.write(f"### {system_status}")

    if system_status == "Healthy":
        st.success("operational")
    else:
        st.error("no activity detected")

st.markdown("")
    
# overview section
left, right = st.columns([2, 1])

with left:
    with st.container(border=True):
        st.markdown("### System Overview")

        st.write(f"Users: {total_users}")
        st.write(f"Events: {total_events}")
        st.write(f"Logs: {total_logs}")


with right:
    with st.container(border=True):
        st.markdown("### System Activity")

        for log in logs[:5]:
            st.write(log.get("description", ""))
st.markdown("")

# activity feed
st.markdown("### Recent Activity")

with st.container(border=True):
    for log in latest_logs:
        c1, c2, c3 = st.columns([3, 1, 2])
        c1.write(log.get("description", ""))
        c2.write(f"user {log.get('user_id', '')}")
        c3.write(log.get("created_at", ""))
        st.divider()

