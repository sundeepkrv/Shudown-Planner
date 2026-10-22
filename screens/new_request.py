import streamlit as st
from services.shutdown_service import (ShutdownService)
from components.header import (render_header)

def show():
	render_header("🔌 Create Shutdown Request","Create a Request for Shutdown Proposal")
	with st.form("shutdown_form"):
		asset = st.selectbox("Asset",options=["Transformer","Reactor","ICT","Busbar","Bay","Circuit Breaker","Isolator","Aux System"],placeholder="Select Asset ...",index=None)
		location = st.text_input("Location or Asset ID")
		reason = st.text_area("Reason")
		priority = st.selectbox("Priority",["Low","Medium","High","Critical"],placeholder="Select Priority ...",index=None)
		start_time = (st.datetime_input("Start Time"))
		end_time = (st.datetime_input("End Time"))
		submitted = (st.form_submit_button("Submit"))
	if submitted:
		request_no = (ShutdownService.create_request(asset,location,reason,priority,start_time,end_time,st.session_state.username))
		st.success(f"Created: {request_no}")