import streamlit as st
from components.header import (render_header)

def show():
	render_header("👤 Profile","View Your Profile")
	st.write(f"Username: "f"{st.session_state.username}")
	st.write(f"Full Name: "f"{st.session_state.full_name}")
	st.write(f"Role: "f"{st.session_state.role}")