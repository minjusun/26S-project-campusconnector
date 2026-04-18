import os
import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title("System Logs")
st.caption("Monitor system events, user activity, warnings, and errors.")

API = os.environ.get("WEB_API_URL", "http://localhost:4000")

# filters
col1, col2, col3 = st.columns(3)

with col1:
    user_filter = st.text_input("User ID (optional)")

with col2:
    action_filter = st.selectbox(
        "Action Type",
        ["", "create_event", "update_event", "send_notification", "view_dashboard", "backup_check", "role_review"]
    )

with col3:
    limit = st.slider("Limit logs", 10, 100, 20)

params = {}

if user_filter:
    params["user_id"] = user_filter

if action_filter:
    params["action_type"] = action_filter

params["limit"] = limit

try:
    logs = requests.get(f"{API}/logs", params=params, timeout=5).json()
except:
    logs = []

st.markdown("### Activity Feed")

with st.container(border=True):

    c1, c2, c3 = st.columns([2, 2, 6])

    c1.markdown("**USER**")
    c2.markdown("**TYPE**")
    c3.markdown("**DESCRIPTION**")

    st.divider()

    for log in logs:

        c1, c2, c3 = st.columns([2, 2, 6])

        with c1:
            st.write(f"user {log.get('user_id', 'system')}")

        with c2:
            t = log.get("action_type", "info")

            if "error" in t:
                st.error(t)
            elif "warning" in t:
                st.warning(t)
            else:
                st.info(t)

        with c3:
            st.write(log.get("description", ""))

        st.divider()

st.download_button(
    label="Export Logs",
    data="\n".join(
        [
            f"{l.get('user_id')} | {l.get('action_type')} | {l.get('description')}"
            for l in logs
        ]
    ),
    file_name="system_logs.txt",
    mime="text/plain"
)
