import os
import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

API = os.environ.get("WEB_API_URL", "http://localhost:4000")

event_id = st.session_state.get('selected_event_id')
if not event_id:
    st.warning("No event selected. Please pick one from Browse Events.")
    if st.button("Back to Browse"):
        st.switch_page('pages/41_Browse_Events.py')
    st.stop()

try:
    resp = requests.get(f"{API}/events/{event_id}", timeout=5)
except requests.exceptions.RequestException as e:
    st.error(f"Could not reach the API: {e}")
    st.stop()

ev = resp.json() if resp.ok else None
if not ev:
    st.error("Event not found.")
    st.stop()

st.title(ev.get('title', 'Event Details'))

if ev.get('image_url'):
    st.image(ev['image_url'], width=400)

a, b = st.columns(2)
with a:
    st.write(f"**Date:** {ev.get('date')}")
    st.write(f"**Time:** {ev.get('start_time')} to {ev.get('end_time')}")
    st.write(f"**Category:** {ev.get('category_name', 'n/a')}")
with b:
    st.write(f"**Location:** {ev.get('location_name', 'n/a')}")
    st.write(f"**Capacity:** {ev.get('capacity')}")
    st.write(f"**Status:** {ev.get('status')}")

st.write("### Description")
st.write(ev.get('description') or "_no description._")

st.divider()
st.write("### RSVP")

user_id = st.session_state.get('user_id')
role = st.session_state.get('role')

left, right = st.columns(2)
with left:
    if role == 'student':
        if st.button("RSVP to this event", type='primary', use_container_width=True):
            payload = {"event_id": event_id, "user_id": user_id, "status": "registered"}
            try:
                r = requests.post(f"{API}/registration", json=payload, timeout=5)
                if r.status_code == 201:
                    st.success("you're in! check My Events to see it.")
                else:
                    st.error(f"RSVP failed: {r.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")
    else:
        st.info("Log in as a student to RSVP.")
with right:
    if st.button("Back to Browse", use_container_width=True):
        st.switch_page('pages/41_Browse_Events.py')
