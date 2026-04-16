import os
import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

API = os.environ.get("WEB_API_URL", "http://localhost:4000")

st.title("Manage Attendance")
st.write("Pick an event and handle RSVPs.")

try:
    events = requests.get(f"{API}/events", timeout=5).json() or []
except requests.exceptions.RequestException as e:
    st.error(f"Could not load events: {e}")
    st.stop()

if not events:
    st.info("No events to manage yet.")
    st.stop()

event_map = {f"{e['title']} - {e['date']} (#{e['event_id']})": e['event_id'] for e in events}
picked = st.selectbox("Select event", list(event_map.keys()))
event_id = event_map[picked]

meta = next((e for e in events if e['event_id'] == event_id), {})
st.caption(f"Capacity: **{meta.get('capacity', 'n/a')}** | Status: **{meta.get('status', 'n/a')}**")

try:
    regs = requests.get(f"{API}/events/{event_id}/registration", timeout=5).json() or []
except requests.exceptions.RequestException as e:
    st.error(f"Could not load registrations: {e}")
    st.stop()

approved = sum(1 for r in regs if (r.get('status') or '').lower() in ('approved', 'registered'))
waitlisted = sum(1 for r in regs if (r.get('status') or '').lower() == 'waitlisted')

m1, m2, m3 = st.columns(3)
m1.metric("Total RSVPs", len(regs))
m2.metric("Approved / Registered", approved)
m3.metric("Waitlisted", waitlisted)

if not regs:
    st.info("No one has RSVP'd to this event yet.")
    st.stop()

st.divider()


def update_status(rid, new_status):
    try:
        r = requests.put(f"{API}/registration/{rid}", json={"status": new_status}, timeout=5)
        if r.ok:
            st.success(f"Updated to {new_status}.")
            st.rerun()
        else:
            st.error(f"Update failed: {r.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")


def remove_rsvp(rid):
    try:
        r = requests.delete(f"{API}/registration/{rid}", timeout=5)
        if r.ok:
            st.success("Removed.")
            st.rerun()
        else:
            st.error("Remove failed.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")


for reg in regs:
    with st.container(border=True):
        name = f"{reg.get('first_name', '')} {reg.get('last_name', '')}".strip() or 'Unknown'
        rid = reg['registration_id']
        cols = st.columns([3, 1, 1, 1, 1])
        with cols[0]:
            st.write(f"**{name}**")
            st.caption(f"{reg.get('email', '')} | RSVP #{rid}")
            st.write(f"Status: `{reg.get('status', 'n/a')}`")
        with cols[1]:
            if st.button("Approve", key=f"ap_{rid}"):
                update_status(rid, 'approved')
        with cols[2]:
            if st.button("Waitlist", key=f"wl_{rid}"):
                update_status(rid, 'waitlisted')
        with cols[3]:
            if st.button("Cancel", key=f"cn_{rid}"):
                update_status(rid, 'cancelled')
        with cols[4]:
            if st.button("Remove", key=f"rm_{rid}"):
                remove_rsvp(rid)
