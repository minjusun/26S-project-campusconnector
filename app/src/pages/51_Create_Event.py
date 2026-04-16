import os
from datetime import date, time
import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

API = os.environ.get("WEB_API_URL", "http://localhost:4000")

st.title("Create Event")
st.write("Fill out the form and hit publish.")

try:
    categories = requests.get(f"{API}/event_categories", timeout=5).json() or []
    locations = requests.get(f"{API}/event_location", timeout=5).json() or []
except requests.exceptions.RequestException as e:
    st.error(f"Could not load form options: {e}")
    st.stop()

if not categories or not locations:
    st.warning("No categories or locations yet. Seed the database first.")
    st.stop()

cat_options = {c['category_name']: c['category_id'] for c in categories}
loc_options = {
    f"{l['location_name']} (cap {l['capacity']})": l['location_id']
    for l in locations
}

with st.form("create_event_form"):
    title = st.text_input("Event Title *", placeholder="e.g. Career Fair 2026")

    col1, col2 = st.columns(2)
    with col1:
        event_date = st.date_input("Date *", value=date.today())
        start_t = st.time_input("Start Time *", value=time(10, 0))
    with col2:
        end_t = st.time_input("End Time *", value=time(12, 0))
        status = st.selectbox("Status *", ["upcoming", "active", "cancelled"])

    cat_label = st.selectbox("Category *", list(cat_options.keys()))
    loc_label = st.selectbox("Location *", list(loc_options.keys()))

    image_url = st.text_input("Image URL", placeholder="https://...")
    description = st.text_area(
        "Description",
        placeholder="what's the event about?",
        height=150,
    )

    submitted = st.form_submit_button("Publish Event", type='primary')

if submitted:
    if not title.strip():
        st.error("Event title is required.")
    elif end_t <= start_t:
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
            r = requests.post(f"{API}/events", json=payload, timeout=5)
            if r.status_code == 201:
                st.success(f"Event published! ID: {r.json().get('event_id', 'n/a')}")
                st.balloons()
            else:
                st.error(f"Create failed: {r.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error: {e}")
