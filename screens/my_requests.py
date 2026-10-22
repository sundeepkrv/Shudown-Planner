import streamlit as st
from services.shutdown_service import (ShutdownService)
from components.header import (render_header)

def show():
	render_header("📝 My Requests","Requests Made by Me")
	requests = (ShutdownService.get_requests_by_user(st.session_state.username))
	if not requests:
		st.info("No requests found.")
		return
	request_data = []
	for request in requests:
		request_data.append({"Request No":request.request_no,"Asset":request.asset,"Location":request.location,"Status":request.status,"Priority":request.priority})
	st.dataframe(request_data,width='stretch')