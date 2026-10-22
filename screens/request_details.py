import streamlit as st
from components.header import (render_header)
from components.timeline import (render_timeline)
from services.shutdown_service import (ShutdownService)
from services.timeline_service import (TimelineService)

def show(request_no):
	request = (ShutdownService.get_request(request_no))
	if not request:
		st.error("Request not found.")
		return
	render_header(request_no)
	st.write(f"Asset: {request.asset}")
	st.write(f"Location: {request.location}")
	st.write(f"Status: {request.status}")
	events = []
	history = (TimelineService.get_timeline(request_no))
	for row in history:
		events.append({"action":row.action,"user":row.action_by,"role":row.role,"time":row.action_time,"remarks":row.remarks})
	render_timeline(events)