import streamlit as st

def render_request_card(request):
	with st.container(border=True):
		st.markdown(f"""### {request.request_no} **Asset:** {request.asset} **Location:** {request.location} **Status:** {request.status} **Priority:** {request.priority} **Created By:** {request.created_by}""")