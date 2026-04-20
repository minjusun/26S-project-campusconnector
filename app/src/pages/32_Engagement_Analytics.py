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

# fetch analytics data
try:
    perf_res = requests.get(f"{API}/analytics/event-performance-detailed", timeout=5)
    insight_res = requests.get(f"{API}/analytics/insights", timeout=5)

    perf = perf_res.json() if perf_res.ok else {}
    insights = insight_res.json() if insight_res.ok else {}

except Exception:
    perf, insights = {}, {}

st.title("Event Analytics")
st.caption("Understand trends in attendance, engagement, and student behavior across events.")

top1, top2, top3 = st.columns(3)

with top1:
    st.write("##### Total Attendance (Avg Rate)")
    st.write(f"### {perf.get('avg_attendance_rate', 0):.2f}")
    st.caption("Across all events")

with top2:
    best = perf.get("best_event", {})
    st.write("##### Best Event")
    st.write(f"### {best.get('title', '—')}")
    st.caption("Highest attendance rate")

with top3:
    best_cat = insights.get("best_category", {})
    st.write("##### Most Popular Category")
    st.write(f"### {best_cat.get('category', '—')}")
    st.caption("Highest average turnout")

st.markdown("")

st.markdown("### Attendance by Event Category")

category_data = insights.get("predictions", [])

st.table({
    "Category": [c["category"] for c in category_data],
    "Avg Attendance": [c["predicted_attendance"] for c in category_data],
})

st.markdown("")

# event breakdown table
st.markdown("### Event Performance Breakdown")

events = perf.get("events", [])

st.table({
    "Event": [e["title"] for e in events],
    "Registrations": [e["registrations"] for e in events],
    "Attendance": [e["attendance"] for e in events],
    "Attendance Rate": [f"{e['attendance_rate']*100:.0f}%" for e in events],
    "Comments": [e["comments"] for e in events],
})


st.markdown("")

# insights section
left, right = st.columns(2)

best_category = insights.get("best_category", {})
best_day = insights.get("best_day", {})

with left:
    st.markdown("### Trend Insights")

    if best_category and best_day:
        st.write(f"- Most popular category is {best_category.get('category', '—')} with an average attendance of {best_category.get('predicted_attendance', 0)}.")
        st.write(f"- Best performing day is {best_day.get('day', '—')} with an average attendance of {best_day.get('avg', 0):.2f}.")
    else:
        st.write("- Not enough data available to generate insights.")
        st.write("- Event trends will appear once more events and registrations are recorded.")

with right:
    st.markdown("### Recommendations")

    if best_category and best_day:
        st.write(f"- Focus more events on {best_category.get('category', 'high-performing categories')}.")
        st.write(f"- Schedule events on {best_day.get('day', 'midweek days')} for better turnout.")
        st.write("- Improve promotion for lower-performing categories.")
    else:
        st.write("- Collect more engagement data before generating recommendations.")
