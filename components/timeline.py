import streamlit as st

def render_timeline(events):
	st.subheader("Approval Timeline")
	for event in events:
		with st.container():
			st.markdown(f"""### ✅ {event['action']} **User:** {event['user']} **Role:** {event['role']} **Time:** {event['time']}""")
			if event.get("remarks"):
				st.info(event["remarks"])
			st.markdown("---")