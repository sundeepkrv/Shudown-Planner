import streamlit as st
from services.approval_service import (ApprovalService)
from components.header import (render_header)

def show():
	render_header("⌛ Pending Approvals","Requests pending for approval")
	role = st.session_state.role
	requests = (ApprovalService.pending_for_role(role))
	if not requests:
		st.info("No pending approvals.")
		return
	for request in requests:
		with st.expander(request.request_no):
			st.write(f"Asset: {request.asset}")
			st.write(f"Location: {request.location}")
			st.write(f"Priority: {request.priority}")
			remarks = st.text_area("Remarks",key=f"rm_{request.id}")
			col1, col2 = (st.columns(2))
			approve = (col1.button("Approve",key=f"ap_{request.id}"))
			reject = (col2.button("Reject",key=f"rj_{request.id}"))
			if approve:
				ApprovalService.approve(request.request_no,st.session_state.username,role,remarks)
				st.success("Approved")
				st.rerun()
			if reject:
				ApprovalService.reject(request.request_no,st.session_state.username,role,remarks)
				st.warning("Rejected")
				st.rerun()