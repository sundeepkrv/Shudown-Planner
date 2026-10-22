import streamlit as st
from auth.session_manager import (clear_session)

def logout():
	clear_session()
	st.rerun()