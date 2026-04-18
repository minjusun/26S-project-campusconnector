import os
import logging
logger = logging.getLogger(__name__)

import streamlit as st
from datetime import date, timedelta
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

API = os.environ.get("WEB_API_URL", "http://localhost:4000")

# api calls
try:
    users_res = requests.get(f"{API}/users", timeout=5)
    users = users_res.json() if users_res.ok else []

    new_users_res = requests.get(f"{API}/users", params={"recent": "true"}, timeout=5)
    new_users = new_users_res.json() if new_users_res.ok else []

    events_res = requests.get(f"{API}/events", params={"upcoming": "true"}, timeout=5)
    events = events_res.json() if events_res.ok else []

    pending_res = requests.get(f"{API}/events", params={"status": "pending"}, timeout=5)
    pending_events = pending_res.json() if pending_res.ok else []

    logs_res = requests.get(f"{API}/logs", timeout=5)
    logs = logs_res.json() if logs_res.ok else []

except requests.exceptions.RequestException:
    st.error("API failed")
    users, new_users, events, pending_events, logs = [], [], [], [], []

# date filter
today = date.today()
week_ahead = today + timedelta(days=7)

events_this_week = []
for e in events:
    try:
        d = date.fromisoformat(e["date"])
        if today <= d <= week_ahead:
            events_this_week.append(e)
    except:
        continue

# system check
system_ok = isinstance(users, list) and isinstance(events, list) and isinstance(logs, list)


st.title('Administrator Dashboard')

top1, top2, top3, top4 = st.columns(4)

with top1:
    st.write("##### Registered Users")
    st.write(f"### {len(users)}")
    st.caption(f"{len(new_users)} new this week")

with top2:
    st.write("##### Upcoming Events")
    st.write(f"### {len(events)}")
    st.caption(f"{len(events_this_week)} this week")

with top3:
    st.write("##### Pending Approvals")
    st.write(f"### {len(pending_events)}")

    if pending_events:
        st.warning("needs review")
    else:
        st.success("all clear")

with top4:
    st.write("##### System Status")
    st.write("### Healthy" if system_ok else "### Degraded")

    if system_ok:
        st.success("all services operational")
    else:
        st.error("service issue detected")

st.markdown("")
left_col, right_col = st.columns([2.2, 1])

with left_col:
    with st.container(border=True):
        st.markdown("### System Overview")

        items = [
            ("Users loaded", f"{len(users)} records", "ok"),
            ("Events loaded", f"{len(events)} records", "ok"),
            ("Pending approvals", f"{len(pending_events)} items", "warning" if pending_events else "ok"),
            ("Logs loaded", f"{len(logs)} entries", "ok"),
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

    for log in logs[:10]:
        c1, c2, c3 = st.columns([3, 2, 2])
        c1.write(log.get("description", "no description"))
        c2.write(f"user {log.get('user_id', 'system')}")
        c3.write(log.get("created_at", "—"))
        st.divider()
        
