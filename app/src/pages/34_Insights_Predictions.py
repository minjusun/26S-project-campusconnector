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

# fetch insights data
try:
    res = requests.get(f"{API}/analytics/insights", timeout=5)
    data = res.json() if res.ok else {}
except Exception:
    data = {}

st.title("Insights & Predictions")
st.caption("Use event data to identify patterns, make recommendations, and predict future engagement.")

top1, top2, top3 = st.columns(3)

best_cat = data.get("best_category", {})
best_day = data.get("best_day", {})

with top1:
    st.write("##### Predicted High Attendance Category")
    st.write(f"### {best_cat.get('category', '—')}")
    st.caption("Expected to have the strongest turnout")

with top2:
    st.write("##### Best Event Day")
    st.write(f"### {best_day.get('day', '—')}")
    st.caption("Highest average attendance")

with top3:
    st.write("##### Recommendation")
    st.write("### Focus Promotion")
    st.caption(f"Prioritize {best_cat.get('category', 'events')} events")

st.markdown("")

st.markdown("### Attendance Predictions")

predictions = data.get("predictions", [])

st.table({
    "Category": [p["category"] for p in predictions],
    "Expected Attendance": [p["predicted_attendance"] for p in predictions],
})


st.markdown("")


st.markdown("### Analyst Alerts")

if best_cat and best_day:
    st.info(
        f"{best_cat.get('category')} events consistently perform best overall."
    )

    st.warning(
        f"{best_day.get('day')} has the highest engagement — consider scheduling events then."
    )

    st.success(
        "Focus resources on high-performing categories to maximize attendance."
    )
else:
    st.info("Not enough data yet to generate insights.")
