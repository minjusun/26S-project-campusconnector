import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title('Backups Dashboard')

st.write('## Model 1 Maintenance')

if st.button("Backups", type='primary', use_container_width=True):
    # TODO: wire this to a POST /train route on the API that triggers retraining
    st.info("Training route not yet implemented.")
