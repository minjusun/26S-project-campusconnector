import logging

logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout="wide")

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title("Insights & Predictions")
st.caption("Use event data to identify patterns, make recommendations, and predict future engagement.")

top1, top2, top3 = st.columns(3)

with top1:
    st.write("##### Predicted High Attendance")
    st.write("### Career Fair")
    st.caption("Expected to have the strongest turnout")

with top2:
    st.write("##### Best Event Day")
    st.write("### Thursday")
    st.caption("Highest average attendance")

with top3:
    st.write("##### Recommendation")
    st.write("### Promote Earlier")
    st.caption("Low-turnout events may benefit from earlier advertising")

st.markdown("")

st.markdown("### Attendance Predictions")

prediction_data = [
    ("Spring Career Fair", "Career", "240"),
    ("AI Workshop", "Academic", "170"),
    ("Club Networking Night", "Social", "110"),
    ("Resume Review Session", "Career", "95"),
    ("Leadership Panel", "Leadership", "125"),
]

st.table(
    {
        "Upcoming Event": [row[0] for row in prediction_data],
        "Category": [row[1] for row in prediction_data],
        "Predicted Attendance": [row[2] for row in prediction_data],
    }
)

st.markdown("")


st.markdown("### Analyst Alerts")

st.info("Leadership Panel is projected to perform well if scheduled during the middle of the week.")
st.warning("Club Networking Night may need additional promotion to increase attendance.")
st.success("Career-focused events continue to show the highest predicted engagement.")

st.markdown("")

st.download_button(
    label="Export Predictions",
    data="Sample predictions export",
    file_name="insights_predictions.txt",
    mime="text/plain"
)