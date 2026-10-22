import streamlit as st
from database.db import (SessionLocal)
from database.models import (User)
from auth.password import (verify_password,hash_password)
from components.header import (render_header)

def show():
	render_header("🔑 Change Password","Manage or Change Your Password")
	current_password = (st.text_input("Current Password",type="password"))
	new_password = (st.text_input("New Password",type="password"))
	confirm_password = (st.text_input("Confirm Password",type="password"))
	if st.button("Update Password"):
		if (new_password != confirm_password):
			st.error("Passwords do not match.")
			return
		db = SessionLocal()
		try:
			user = (db.query(User).filter(User.username==st.session_state.username).first())
			if not verify_password(current_password,user.password_hash):
				st.error("Incorrect password.")
				return
			user.password_hash = (hash_password(new_password))
			db.commit()
			st.success("Password updated.")
		finally:
			db.close()