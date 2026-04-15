from datetime import datetime, date, time
import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

API = "http://web-api:4000"

event_id = st.session_state.get('edit_event_id')
if not event_id:
    st.warning("No event selected. Open Manage Events and choose one.")
    if st.button("Go to Manage Events"):
        st.switch_page('pages/52_Manage_Events.py')
    st.stop()

try:
    ev = requests.get(f"{API}/events/{event_id}", timeout=5).json()
    categories = requests.get(f"{API}/event_categories", timeout=5).json() or []
    locations = requests.get(f"{API}/event_location", timeout=5).json() or []
except requests.exceptions.RequestException as e:
    st.error(f"Could not load event: {e}")
    st.stop()

if not ev:
    st.error("Event not found.")
    st.stop()

st.title(f"Edit Event: {ev.get('title', '')}")


def parse_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return date.today()


def parse_time(s):
    try:
        return datetime.strptime(s, "%H:%M:%S").time()
    except (TypeError, ValueError):
        return time(10, 0)


cat_options = {c['category_name']: c['category_id'] for c in categories}
loc_options = {
    f"Location #{l['location_id']} (cap {l['capacity']})": l['location_id']
    for l in locations
}

# figure out which dropdown option matches the current event
cat_index = next(
    (i for i, n in enumerate(cat_options) if cat_options[n] == ev.get('category_id')),
    0,
)
loc_index = next(
    (i for i, n in enumerate(loc_options) if loc_options[n] == ev.get('location_id')),
    0,
)

statuses = ["upcoming", "active", "cancelled"]
cur_status = ev.get('status', 'upcoming')
status_index = statuses.index(cur_status) if cur_status in statuses else 0

with st.form("edit_event_form"):
    title = st.text_input("Event Title *", value=ev.get('title', ''))
    col1, col2 = st.columns(2)
    with col1:
        event_date = st.date_input("Date *", value=parse_date(ev.get('date')))
        start_t = st.time_input("Start Time *", value=parse_time(ev.get('start_time')))
    with col2:
        end_t = st.time_input("End Time *", value=parse_time(ev.get('end_time')))
        status = st.selectbox("Status *", statuses, index=status_index)

    cat_label = st.selectbox("Category *", list(cat_options.keys()), index=cat_index)
    loc_label = st.selectbox("Location *", list(loc_options.keys()), index=loc_index)

    image_url = st.text_input("Flyer / Image URL", value=ev.get('image_url') or "")
    description = st.text_area("Description", value=ev.get('description') or "", height=150)

    s_col, c_col = st.columns(2)
    with s_col:
        save = st.form_submit_button("Save Changes", type='primary')
    with c_col:
        cancel = st.form_submit_button("Back to List")

if save:
    if end_t <= start_t:
        st.error("End time must be after start time.")
    else:
        payload = {
            "title": title.strip(),
            "date": event_date.isoformat(),
            "start_time": start_t.strftime("%H:%M:%S"),
            "end_time": end_t.strftime("%H:%M:%S"),
            "status": status,
            "category_id": cat_options[cat_label],
            "location_id": loc_options[loc_label],
            "image_url": image_url or None,
            "description": description or None,
        }
        try:
            r = requests.put(f"{API}/events/{event_id}", json=payload, timeout=5)
            if r.ok:
                st.success("Event updated.")
            else:
                st.error(f"Update failed: {r.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error: {e}")

if cancel:
    st.switch_page('pages/52_Manage_Events.py')
