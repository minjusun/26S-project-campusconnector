# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has functions to add links to the left sidebar based on the user's role.

import streamlit as st


# ---- General ----------------------------------------------------------------

def home_nav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def about_page_nav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")


# ---- Role: pol_strat_advisor ------------------------------------------------

def pol_strat_home_nav():
    st.sidebar.page_link(
        "pages/00_Pol_Strat_Home.py", label="Political Strategist Home", icon="👤"
    )


def world_bank_viz_nav():
    st.sidebar.page_link(
        "pages/01_World_Bank_Viz.py", label="World Bank Visualization", icon="🏦"
    )


def map_demo_nav():
    st.sidebar.page_link("pages/02_Map_Demo.py", label="Map Demonstration", icon="🗺️")


# ---- Role: Data Analyst -----------------------------------------------------

def data_analyst_home_nav():
    st.sidebar.page_link(
        "pages/31_Data_Analyst_Home.py", label="Data Analyst Home", icon="🏠"
    )

def engagement_analytics_nav():
    st.sidebar.page_link("pages/32_Engagement_Analytics.py", label="Engagement Analytics", icon="📊")


def event_performance_nav():
    st.sidebar.page_link("pages/33_Event_Performance.py", label="Event Performance", icon="🏆")

def insights_prediction_nav():
    st.sidebar.page_link(
        "pages/34_Insights_Predictions.py", label="Insights & Predictions", icon="📈"
    )

# ---- Role: student ----------------------------------------------------------

def student_home_nav():
    st.sidebar.page_link(
        "pages/40_Student_Home.py", label="Student Home", icon="🎓"
    )


def browse_events_nav():
    st.sidebar.page_link(
        "pages/41_Browse_Events.py", label="Browse Events", icon="🔎"
    )


def my_events_nav():
    st.sidebar.page_link(
        "pages/43_My_Events.py", label="My Events", icon="📅"
    )


def notifications_nav():
    st.sidebar.page_link(
        "pages/44_Notifications.py", label="Notifications", icon="🔔"
    )


# ---- Role: event_coordinator -----------------------------------------------

def event_coord_home_nav():
    st.sidebar.page_link(
        "pages/50_Event_Coord_Home.py", label="Coordinator Home", icon="🗂️"
    )


def create_event_nav():
    st.sidebar.page_link(
        "pages/51_Create_Event.py", label="Create Event", icon="➕"
    )


def manage_events_nav():
    st.sidebar.page_link(
        "pages/52_Manage_Events.py", label="Manage Events", icon="🛠️"
    )


def manage_attendance_nav():
    st.sidebar.page_link(
        "pages/54_Manage_Attendance.py", label="Manage Attendance", icon="✅"
    )


# ---- Role: administrator ----------------------------------------------------

def admin_home_nav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon="🖥️")


def administrator_dashboard_nav():
    st.sidebar.page_link(
        "pages/21_Administrator_Dashboard.py", label="Administrator Dashboard", icon="🏢"
    )

def system_status_nav():
    st.sidebar.page_link(
        "pages/22_System_Status.py", label="System Status", icon="🛠️"
    )

def backups_nav():
    st.sidebar.page_link(
        "pages/23_Backups.py", label="Backups", icon="💾"
    )

def logs_nav():
    st.sidebar.page_link(
        "pages/24_Logs.py", label="Logs", icon="📝"
    )

def user_management_nav():
    st.sidebar.page_link(
        "pages/25_Admin_User_Management.py", label="User Management", icon="✏️"
    )

# ---- Role: data analyst ----------------------------------------------------



# ---- Sidebar assembly -------------------------------------------------------

def SideBarLinks(show_home=False):
    """
    Renders sidebar navigation links based on the logged-in user's role.
    The role is stored in st.session_state when the user logs in on Home.py.
    """

    # Logo appears at the top of the sidebar on every page
    st.sidebar.image("/app/static/Campus_Connector_Logo.png", width=150)

    # If no one is logged in, send them to the Home (login) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        home_nav()

    if st.session_state["authenticated"]:

        if st.session_state["role"] == "pol_strat_advisor":
            pol_strat_home_nav()
            world_bank_viz_nav()
            map_demo_nav()

        if st.session_state["role"] == "data_analyst":
            data_analyst_home_nav()
            engagement_analytics_nav()
            event_performance_nav()
            insights_prediction_nav()


        if st.session_state["role"] == "administrator":
            admin_home_nav()
            administrator_dashboard_nav()
            system_status_nav()
            backups_nav()
            logs_nav()
            user_management_nav()
        if st.session_state["role"] == "student":
            student_home_nav()
            browse_events_nav()
            my_events_nav()
            notifications_nav()

        if st.session_state["role"] == "event_coordinator":
            event_coord_home_nav()
            create_event_nav()
            manage_events_nav()
            manage_attendance_nav()

    # About link appears at the bottom for all roles
    about_page_nav()

    if st.session_state["authenticated"]:
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
