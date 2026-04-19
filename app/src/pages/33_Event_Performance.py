import os
import logging

logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout="wide")

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

API = os.environ.get("WEB_API_URL", "http://localhost:4000")

# fetch event analytics
try:
    perf_res = requests.get(f"{API}/analytics/event-performance-detailed", timeout=5)
    perf = perf_res.json() if perf_res.ok else {}
except Exception:
    perf = {}

st.title("Event Performance")
st.caption("Compare how events are performing using attendance, engagement, and feedback metrics.")

top1, top2, top3 = st.columns(3)

best_event = perf.get("best_event", {})
avg_rate = perf.get("avg_attendance_rate", 0) * 100

with top1:
    st.write("##### Best Performing Event")
    st.write(f"### {best_event.get('title', '—')}")
    st.caption("Highest attendance rate")

with top2:
    st.write("##### Average Attendance Rate")
    st.write(f"### {avg_rate:.0f}%")
    st.caption("Across all events")

with top3:
    st.write("##### Total Events")
    st.write(f"### {len(perf.get('events', []))}")
    st.caption("Tracked in system")

st.markdown("")

st.markdown("### Event Comparison")

events = perf.get("events", [])

st.table({
    "Event": [e["title"] for e in events],
    "Registrations": [e["registrations"] for e in events],
    "Attendance": [e["attendance"] for e in events],
    "Attendance Rate": [f"{e['attendance_rate']*100:.0f}%" for e in events],
    "Comments": [e["comments"] for e in events],
})

st.markdown("")

st.markdown("### Feedback Summary")

if events:
    most_discussed = max(events, key=lambda x: x["comments"])

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.write("##### Most Discussed Event")
            st.write(f"### {most_discussed['title']}")
            st.caption(f"{most_discussed['comments']} comments")

        with col2:
            best_commented = max(events, key=lambda x: x["comments"])
            st.write("##### Highest Engagement Event")
            st.write(f"### {best_commented['title']}")
            st.caption(f"{best_commented['comments']} comments")

st.markdown("")

# export
st.download_button(
    label="Export Event Performance",
    data=str(perf),
    file_name="event_performance.json",
    mime="application/json"
)
