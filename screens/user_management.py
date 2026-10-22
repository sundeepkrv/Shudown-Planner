import streamlit as st
from components.header import (render_header)
from services.user_service import (UserService)

def show():
	render_header("⚙️ User Management","Manage Users as Administrator")
	users = (UserService.get_all_users())
	rows = []
	for user in users:
		rows.append({"Username":user.username,"Full Name":user.full_name,"Role":user.role,"Active":user.active})
	st.dataframe(rows,width='stretch')
	st.subheader("Reset Password")
	username = st.selectbox("Select User",[u.username for u in users])
	new_password = (st.text_input("New Password",type="password"))
	if st.button("Reset"):
		UserService.reset_password(username,new_password)
		st.success("Password Reset")