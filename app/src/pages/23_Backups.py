import os
import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title('Backups Dashboard')

API = os.environ.get("WEB_API_URL", "http://localhost:4000")

st.markdown("### Run Backup")

if st.button("Start Backup", type="primary", use_container_width=True):
    try:
        res = requests.post(
            f"{API}/backups",
            json={"user_id": st.session_state.get("user_id", 1)},
            timeout=5
        )

        if res.status_code == 201:
            st.success("Backup started successfully")
            st.rerun()
        else:
            st.error("Failed to start backup")

    except:
        st.error("API request failed")

# pull backup data
try:
    backups = requests.get(f"{API}/backups", timeout=5).json()
except:
    backups = []

# compute stats from data
total_backups = len(backups)
failed_backups = len([b for b in backups if b.get("status") == "failed"])
completed_backups = len([b for b in backups if b.get("status") == "completed"])
in_progress = len([b for b in backups if b.get("status") == "in_progress"])


top1, top2, top3 = st.columns(3)

with top1:
    st.write("##### Total Backups")
    st.write(f"### {total_backups}")

with top2:
    st.write("##### Completed")
    st.write(f"### {completed_backups}")
    st.success("successful runs")

with top3:
    st.write("##### Failed / Issues")
    st.write(f"### {failed_backups}")
    if failed_backups > 0:
        st.error("attention needed")
    else:
        st.success("all good")
    
st.markdown("")

st.markdown("### Backup History")

with st.container(border=True):

    c1, c2 = st.columns([2, 1])
    c1.markdown("**USER ID**")
    c2.markdown("**STATUS**")

    st.divider()

    for b in backups:
        c1, c2 = st.columns([2, 1])

        with c1:
            st.write(f"User {b.get('user_id')}")

        with c2:
            status = b.get("status")

            if status == "completed":
                st.success("completed")
            elif status == "failed":
                st.error("failed")
            else:
                st.warning(status)

        st.divider()
