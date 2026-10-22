import streamlit as st
from config import ROLE_MENUS

def get_menu_for_role(role: str):
	return ROLE_MENUS.get(role,[])

def has_permission(role: str,permission: str):
	permissions = ROLE_PERMISSIONS.get(role,[])
	return (permission in permissions)

def require_role(roles):
	if isinstance(roles,str):
		roles = [roles]
	current_role = (st.session_state.get("role"))
	return (current_role in roles)