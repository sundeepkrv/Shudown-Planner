import streamlit as st
from auth.permissions import (get_menu_for_role)

def render_sidebar():
	st.sidebar.title("⚡Shutdown Planning And Approval System⚡")
	st.sidebar.markdown("<hr style='margin: 1px 0px;'/>",unsafe_allow_html=True)
	st.sidebar.write(f"""👤 {st.session_state.full_name}""")
	st.sidebar.write(f"""🔐 {st.session_state.role}""")
	st.sidebar.markdown("<hr style='margin: 1px 0px;'/>",unsafe_allow_html=True)
	menu_items = get_menu_for_role(st.session_state.role)
	selected_menu = st.sidebar.radio("Navigation",menu_items)
	logout_clicked = (st.sidebar.button("🚪 Logout"))
	return (selected_menu,logout_clicked)