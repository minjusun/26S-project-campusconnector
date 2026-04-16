import os
import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

API = os.environ.get("WEB_API_URL", "http://localhost:4000")

st.title("Notifications")
st.write("Reminders about your events.")

user_id = st.session_state.get('user_id')
if not user_id:
    st.warning("Not logged in.")
    st.stop()

try:
    resp = requests.get(f"{API}/notifications", params={"user_id": user_id}, timeout=5)
except requests.exceptions.RequestException as e:
    st.error(f"Could not reach the API: {e}")
    st.stop()

if not resp.ok:
    st.error("Failed to load notifications.")
    st.stop()

notes = resp.json()
if not notes:
    st.info("No notifications yet.")
    st.stop()

for n in notes:
    with st.container(border=True):
        st.write(f"**{n.get('message', '')}**")
        st.caption(f"Event #{n.get('event_id')} | Sent {n.get('sent_at', '')}")
