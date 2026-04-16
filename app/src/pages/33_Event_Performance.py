import logging

logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout="wide")

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title("Event Performance")
st.caption("Compare how events are performing using attendance, engagement, and feedback metrics.")

top1, top2, top3 = st.columns(3)

with top1:
    st.write("##### Best Performing Event")
    st.write("### Spring Career Fair")
    st.caption("Highest attendance rate")

with top2:
    st.write("##### Average Attendance Rate")
    st.write("### 78%")
    st.caption("Across all events")

with top3:
    st.write("##### Average Rating")
    st.write("### 4.3 / 5")
    st.caption("Based on student feedback")

st.markdown("")

st.markdown("### Event Comparison")

event_data = [
    ("Spring Career Fair", "250", "220", "88%", "42", "4.6"),
    ("AI Workshop", "180", "150", "83%", "30", "4.4"),
    ("Club Networking Night", "120", "85", "71%", "18", "4.1"),
    ("Resume Review Session", "100", "60", "60%", "10", "3.9"),
    ("Student Leadership Panel", "140", "95", "68%", "15", "4.2"),
]

st.table(
    {
        "Event": [row[0] for row in event_data],
        "Registrations": [row[1] for row in event_data],
        "Attendance": [row[2] for row in event_data],
        "Attendance Rate": [row[3] for row in event_data],
        "Comments": [row[4] for row in event_data],
        "Rating": [row[5] for row in event_data],
    }
)

st.markdown("")

st.markdown("### Feedback Summary")

feedback1, feedback2 = st.columns(2)

with feedback1:
    st.write("##### Most Discussed Event")
    st.write("### Spring Career Fair")
    st.caption("42 comments")

with feedback2:
    st.write("##### Highest Rated Event")
    st.write("### Spring Career Fair")
    st.caption("4.6 / 5 average rating")

st.markdown("")

st.download_button(
    label="Export Event Performance",
    data="Sample event performance export",
    file_name="event_performance.txt",
    mime="text/plain"
)