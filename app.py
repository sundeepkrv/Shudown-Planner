import streamlit as st

# =====================================================
# CONFIG
# =====================================================

from config import (APP_NAME,APP_VERSION,DEFAULT_LAYOUT,APP_DEVELOPER)

# =====================================================
# DATABASE INITIALIZATION
# =====================================================

from database.seed_data import (seed_database)

# =====================================================
# AUTHENTICATION
# =====================================================

from auth.login import (authenticate_user)
from auth.logout import (logout)
from auth.session_manager import (initialize_session,is_authenticated)

# =====================================================
# DATABASE SESSION
# =====================================================

from database.db import (SessionLocal)

# =====================================================
# SCREENS
# =====================================================

from screens.dashboard import (show as show_dashboard)
from screens.new_request import (show as show_new_request)
from screens.my_requests import (show as show_my_requests)
from screens.approvals import (show as show_approvals)
from screens.reports import (show as show_reports)
from screens.calendar_view import (show as show_calendar)
from screens.audit_logs import (show as show_audit_logs)
from screens.user_management import (show as show_user_management)
from screens.change_password import (show as show_change_password)
from screens.profile import (show as show_profile)

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(page_title=APP_NAME,layout=DEFAULT_LAYOUT)
# st.markdown("""<style>[data-testid="stSidebar"] {display: none;}[data-testid="collapsedControl"] {display: none;}</style>""", unsafe_allow_html=True)

# =====================================================
# SESSION INITIALIZATION
# =====================================================

initialize_session()

# =====================================================
# CUSTOM STYLING
# =====================================================

st.markdown("""<style>.login-box{padding:25px;border-radius:12px;border:1px solid #d9d9d9;}</style>""",unsafe_allow_html=True)

# =====================================================
# LOGIN PAGE
# =====================================================

if not is_authenticated():
	st.markdown(f"""<h3 style='color:#1F4E79;'>⚡{APP_NAME}⚡</h3>""",unsafe_allow_html=True,text_alignment="center")
	st.caption(f"Version {APP_VERSION}",text_alignment="center")
	st.markdown("---")
	username = st.text_input("Username")
	password = st.text_input("Password",type="password")
	login_clicked = st.button("Login",width="stretch")
	st.markdown("<hr style='margin: 1px 0px;'/>",unsafe_allow_html=True)
	st.caption(f"{APP_NAME} | Version {APP_VERSION} | {APP_DEVELOPER}",text_alignment="center")
	if login_clicked:
		db = SessionLocal()
		try:
			success, message = (authenticate_user(db,username,password))
			if success:
				st.success(message)
				st.rerun()
			else:
				st.error(message)
		finally:
			db.close()
	st.stop()

# =====================================================
# MAIN APPLICATION
# =====================================================

from components.sidebar import (render_sidebar)
selected_menu, logout_clicked = (render_sidebar())

# =====================================================
# LOGOUT
# =====================================================

if logout_clicked:
	logout()

# =====================================================
# PAGE ROUTING
# =====================================================

if selected_menu == "Dashboard":
	show_dashboard()
elif selected_menu == "New Request":
	show_new_request()
elif selected_menu == "My Requests":
	show_my_requests()
elif selected_menu == "Approvals":
	show_approvals()
elif selected_menu == "Reports":
	show_reports()
elif selected_menu == "Calendar":
	show_calendar()
elif selected_menu == "Audit Logs":
	show_audit_logs()
elif selected_menu == "User Management":
	show_user_management()
elif selected_menu == "Change Password":
	show_change_password()
elif selected_menu == "Profile":
	show_profile()
else:
	st.warning("Page not implemented.")

# =====================================================
# FOOTER
# =====================================================

st.markdown("<hr style='margin: 1px 0px;'/>",unsafe_allow_html=True)
st.caption(f"{APP_NAME} | Version {APP_VERSION} | {APP_DEVELOPER}",text_alignment="center")