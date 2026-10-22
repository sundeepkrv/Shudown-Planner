import streamlit as st

def initialize_session():
	default_values = {"logged_in": False,"username": None,"full_name": None,"role": None,"user_id": None}
	for key, value in default_values.items():
		if key not in st.session_state:
			st.session_state[key] = value

def set_user_session(user):
	st.session_state.logged_in = True
	st.session_state.user_id = user.id
	st.session_state.username = user.username
	st.session_state.full_name = user.full_name
	st.session_state.role = user.role

def clear_session():
	for key in list(st.session_state.keys()):
		del st.session_state[key]

def is_authenticated():
	return st.session_state.get("logged_in",False)

def get_current_user():
	return {
		"user_id":st.session_state.get("user_id"),
		"username":st.session_state.get("username"),
		"full_name":st.session_state.get("full_name"),
		"role":st.session_state.get("role")
	}
