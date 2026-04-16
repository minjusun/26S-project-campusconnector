import os
import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

API = os.environ.get("WEB_API_URL", "http://localhost:4000")

st.title("My Events")
st.write("Stuff you signed up for.")

user_id = st.session_state.get('user_id')
if not user_id:
    st.warning("Not logged in.")
    st.stop()

try:
    resp = requests.get(f"{API}/users/{user_id}/registration", timeout=5)
except requests.exceptions.RequestException as e:
    st.error(f"Could not reach the API: {e}")
    st.stop()

if not resp.ok:
    st.error("Failed to load your events.")
    st.stop()

regs = resp.json()

if not regs:
    st.info("You haven't signed up for any events yet.")
    if st.button("Browse Events", type='primary'):
        st.switch_page('pages/41_Browse_Events.py')
    st.stop()

st.write(f"You have **{len(regs)}** registration(s).")

for reg in regs:
    with st.container(border=True):
        left, right = st.columns([4, 1])
        with left:
            st.subheader(reg.get('title', 'Untitled'))
            st.caption(
                f"{reg.get('date')} | {reg.get('start_time')} - {reg.get('end_time')}"
                f" | {reg.get('category_name', 'n/a')}"
            )
            st.write(f"**RSVP status:** {reg.get('status', 'n/a')}")
        with right:
            if st.button("Cancel RSVP", key=f"cancel_{reg['registration_id']}"):
                try:
                    r = requests.delete(
                        f"{API}/registration/{reg['registration_id']}", timeout=5
                    )
                    if r.ok:
                        st.success("Registration cancelled.")
                        st.rerun()
                    else:
                        st.error("Cancellation failed.")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error: {e}")
