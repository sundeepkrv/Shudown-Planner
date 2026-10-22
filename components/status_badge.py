import streamlit as st

def render_status(status):
	color = "gray"
	match status:
		case "Approved":
			color = "green"
		case "Rejected":
			color = "red"
		case "Pending":
			color = "orange"
	st.markdown(f"""<span style="background:{color};padding:5px;border-radius:5px;color:white;">{status}</span>""",unsafe_allow_html=True)