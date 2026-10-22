import streamlit as st
from components.header import render_header
from components.metrics import render_metrics
from services.shutdown_service import (ShutdownService)
from services.approval_service import (ApprovalService)
from services.user_service import (UserService)

def show():
	role = st.session_state.role
	render_header("📈 Dashboard","System Overview")

	# Requestor Dashboard
	if role == "Requestor":
		requests = (ShutdownService.get_requests_by_user(st.session_state.username))
		total = len(requests)
		pending = len([r for r in requests if r.status=="Pending"])
		approved = len([r for r in requests if r.status=="Approved"])
		rejected = len([r for r in requests if r.status=="Rejected"])
		render_metrics([("My Requests",total),("Pending",pending),("Approved",approved),("Rejected",rejected)])

	# Reviewer / Manager / Approver Dashboard
	elif role in ["Reviewer","Manager","Approver"]:
		approvals = (ApprovalService.pending_for_role(role))
		render_metrics([("Pending Approvals",len(approvals))])

	# Admin Dashboard
	elif role == "Admin":
		users = (UserService.get_all_users())
		requests = (ShutdownService.get_all_requests())
		render_metrics([("Total Users",len(users)),("Total Requests",len(requests))])
	st.success(f"Logged in as {role}")