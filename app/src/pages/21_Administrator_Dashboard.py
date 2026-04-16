import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title('Administrator Dashboard')

top1, top2, top3, top4 = st.columns(4)

with top1:
    st.write("##### Registered Users")
    st.write("### 1,284")
    st.caption("42 new this week")

with top2:
    st.write("##### Upcoming Events")
    st.write("### 42")
    st.caption("8 this week")

with top3:
    st.write("##### Pending Approvals")
    st.write("### 6")
    st.caption("0 urgent")

with top4:
    st.write("##### System Status")
    st.write("### Healthy")
    st.success("All services operational")

st.markdown("")
left_col, right_col = st.columns([2.2, 1])

with left_col:
    with st.container(border=True):
        st.markdown("### System Overview")

        items = [
            ("Database integrity", "Last run: 2 hours ago", "ok"),
            ("Backup status", "Last completed: today 2:00 PM", "ok"),
            ("Storage capacity", "65 GB used", "warning"),
            ("Network connectivity", "Last checked: 5 min ago", "ok"),
        ]

        for title, subtitle, status in items:
            icon = "🟢" if status == "ok" else "🟠"
            c1, c2 = st.columns([0.08, 0.92], vertical_alignment="center")
            with c1:
                st.markdown(icon)
            with c2:
                st.markdown(f"**{title}**")
                st.caption(subtitle)
            st.divider()

with right_col:
    with st.container(border=True):
        st.markdown("### Admin Controls")
        st.selectbox("Refresh Interval", ["5 min", "15 min", "30 min", "1 hour"])
        st.toggle("Maintenance Mode", value=False)
        st.toggle("Auto Backups", value=True)

        st.markdown("")
        st.button("Run System Check", use_container_width=True, type="primary")
        st.button("View Logs", use_container_width=True)

st.markdown("")
st.markdown("### Recent Admin Activity")

with st.container(border=True):
    h1, h2, h3 = st.columns([3, 2, 2])
    h1.markdown("**ACTIVITY**")
    h2.markdown("**USER**")
    h3.markdown("**TIME**")
    st.divider()

    activity = [
        ("Approved event: Spring Career Mixer", "Admin", "10 min ago"),
        ("Backup completed successfully", "System", "1 hour ago"),
        ("Storage warning triggered", "System", "2 hours ago"),
        ("Role updated for user 104", "Admin", "Today"),
    ]

    for action, user, time in activity:
        c1, c2, c3 = st.columns([3, 2, 2])
        c1.write(action)
        c2.write(user)
        c3.write(time)
        st.divider()
        