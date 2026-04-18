import os
import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

st.set_page_config(layout='wide')

SideBarLinks()

st.write("# User Management")
st.caption("Manage and update user information and permissions.")

users = []

try:
    API = os.environ.get("WEB_API_URL", "http://localhost:4000")
    users = requests.get(f"{API}/users").json()

except requests.exceptions.RequestException:
    st.write("**Important**: Could not connect to API, using dummy data.")

    users = [
        {
            "user_id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "role_id": 1,
            "status": "active"
        },
        {
            "user_id": 2,
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane@example.com",
            "role_id": 2,
            "status": "active"
        }
    ]

st.markdown("### Current Users")


search_term = st.text_input(
    "Search users",
    placeholder="Search by user ID, name, email, role, or status"
)

formatted_users = [
    {
        "User ID": user.get("user_id", ""),
        "Name": f"{user.get('first_name', '')} {user.get('last_name', '')}".strip(),
        "Email": user.get("email", ""),
        "Role": user.get("role_id", ""),
        "Status": user.get("status", "")
    }
    for user in users
]

if search_term:
    q = search_term.lower().strip()
    filtered_users = [
        user for user in formatted_users
        if q in str(user["User ID"]).lower()
        or q in user["Name"].lower()
        or q in str(user["Email"]).lower()
        or q in str(user["Role"]).lower()
        or q in str(user["Status"]).lower()
    ]
else:
    filtered_users = formatted_users

st.dataframe(filtered_users, use_container_width=True, hide_index=True)


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Create User")

    new_email = st.text_input("Email", key="create_email")
    new_role = st.selectbox("Role", [1, 2, 3, 4], key="create_role")

    if st.button("Create"):
        payload = {
            "first_name": "New",
            "last_name": "User",
            "email": new_email,
            "role_id": new_role,
            "password_hash": "demo"
        }

        try:
            res = requests.post(f"{API}/users", json=payload)
            st.success("User created")
        except:
            st.error("Failed to create user")

with col2:
    st.markdown("### Update User")

    update_id = st.number_input("User ID", step=1, key="update_id")
    update_email = st.text_input("New Email", key="update_email")

    if st.button("Update"):
        payload = {
            "email": update_email,
            "role_id": 1,
            "status": "active"
        }

        try:
            res = requests.put(f"{API}/users/{int(update_id)}", json=payload)
            st.success("User updated")
        except:
            st.error("Update failed")


with col3:
    st.markdown("### Delete User")

    delete_id = st.number_input("User ID", step=1, key="delete_id")

    if st.button("Delete"):
        try:
            res = requests.delete(f"{API}/users/{int(delete_id)}")
            st.success("User deleted")
        except:
            st.error("Delete failed")

st.button("Refresh Users")