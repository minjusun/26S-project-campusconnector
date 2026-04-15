import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

API = "http://web-api:4000"

st.title("Manage Events")
st.write("All events. Edit or delete below.")

try:
    resp = requests.get(f"{API}/events", timeout=5)
except requests.exceptions.RequestException as e:
    st.error(f"Could not reach the API: {e}")
    st.stop()

if not resp.ok:
    st.error("Failed to load events.")
    st.stop()

events = resp.json()

if not events:
    st.info("No events published yet.")
    if st.button("Create an Event", type='primary'):
        st.switch_page('pages/51_Create_Event.py')
    st.stop()

st.write(f"**{len(events)}** event(s) total.")

for ev in events:
    with st.container(border=True):
        info, edit_col, del_col = st.columns([4, 1, 1])
        with info:
            st.subheader(ev.get('title', 'Untitled'))
            st.caption(
                f"{ev.get('date')} | {ev.get('start_time')} - {ev.get('end_time')}"
                f" | {ev.get('category_name', 'n/a')} | Status: {ev.get('status', 'n/a')}"
            )
        with edit_col:
            if st.button("Edit", key=f"edit_{ev['event_id']}"):
                st.session_state['edit_event_id'] = ev['event_id']
                st.switch_page('pages/53_Edit_Event.py')
        with del_col:
            if st.button("Delete", key=f"del_{ev['event_id']}"):
                try:
                    r = requests.delete(f"{API}/events/{ev['event_id']}", timeout=5)
                    if r.ok:
                        st.success("Event deleted.")
                        st.rerun()
                    else:
                        st.error(f"Delete failed: {r.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error: {e}")
