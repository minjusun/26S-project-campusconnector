import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

API = "http://web-api:4000"

st.title("Browse Upcoming Events")
st.write("Filter by category or search by name.")

# pull categories for the dropdown
categories = []
try:
    r = requests.get(f"{API}/event_categories", timeout=5)
    if r.ok:
        categories = [c['category_name'] for c in r.json()]
except requests.exceptions.RequestException:
    pass

c1, c2 = st.columns([2, 1])
with c1:
    search = st.text_input("Search by title", placeholder="e.g. Career Fair")
with c2:
    pick = st.selectbox("Category", ["All"] + categories)

params = {"upcoming": "true"}
if pick != "All":
    params["category"] = pick
if search:
    params["q"] = search

try:
    resp = requests.get(f"{API}/events", params=params, timeout=5)
except requests.exceptions.RequestException as e:
    st.error(f"Could not reach the API: {e}")
    st.stop()

if not resp.ok:
    st.error("Failed to load events.")
    st.stop()

events = resp.json()
st.write(f"Found **{len(events)}** event(s).")

if not events:
    st.info("No events match your filters.")
else:
    for ev in events:
        with st.container(border=True):
            left, right = st.columns([4, 1])
            with left:
                st.subheader(ev.get('title', 'Untitled'))
                st.caption(
                    f"{ev.get('date')} | {ev.get('start_time')} - {ev.get('end_time')}"
                    f" | {ev.get('category_name', 'n/a')}"
                )
                st.write(f"Capacity: {ev.get('capacity', 'n/a')} | Status: {ev.get('status', 'n/a')}")
            with right:
                if st.button("View details", key=f"view_{ev['event_id']}"):
                    st.session_state['selected_event_id'] = ev['event_id']
                    st.switch_page('pages/42_Event_Details.py')
