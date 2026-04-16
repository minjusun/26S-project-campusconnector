import logging

logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout="wide")

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title("Event Analytics")
st.caption("Understand trends in attendance, engagement, and student behavior across events.")

top1, top2, top3 = st.columns(3)

with top1:
    st.write("##### Total Attendance (This Month)")
    st.write("### 810")
    st.caption("Across all events")

with top2:
    st.write("##### Repeat Attendance Rate")
    st.write("### 43%")
    st.caption("Students attending multiple events")

with top3:
    st.write("##### Most Popular Category")
    st.write("### Career")
    st.caption("Highest average turnout")

st.markdown("")

st.markdown("### Attendance by Event Category")

category_data = [
    ("Career", 320),
    ("Academic", 210),
    ("Social", 150),
    ("Leadership", 130),
]

st.table(
    {
        "Category": [row[0] for row in category_data],
        "Total Attendance": [row[1] for row in category_data],
    }
)

st.markdown("")

st.markdown("### Attendance by Day of Week")

day_data = [
    ("Monday", 90),
    ("Tuesday", 140),
    ("Wednesday", 200),
    ("Thursday", 220),
    ("Friday", 100),
    ("Weekend", 60),
]

st.table(
    {
        "Day": [row[0] for row in day_data],
        "Average Attendance": [row[1] for row in day_data],
    }
)

st.markdown("")

st.markdown("### Monthly Attendance Trends")

monthly_data = [
    ("January", 400),
    ("February", 520),
    ("March", 610),
    ("April", 810),
]

st.table(
    {
        "Month": [row[0] for row in monthly_data],
        "Total Attendance": [row[1] for row in monthly_data],
    }
)

st.markdown("")

left, right = st.columns(2)

with left:
    st.markdown("### Trend Insights")
    st.write("- Attendance is increasing month over month.")
    st.write("- Career-focused events drive the most participation.")
    st.write("- Midweek events (Wed–Thurs) perform best.")

with right:
    st.markdown("### Recommendations")
    st.write("- Schedule high-priority events midweek.")
    st.write("- Increase investment in career-focused programming.")
    st.write("- Improve promotion for weekend events.")

st.markdown("")

st.download_button(
    label="Export Analytics Data",
    data="Sample analytics export",
    file_name="event_analytics.txt",
    mime="text/plain"
)
