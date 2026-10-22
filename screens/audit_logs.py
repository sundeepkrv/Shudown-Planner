import streamlit as st
from database.db import (SessionLocal)
from database.models import (AuditLog)
from components.header import (render_header)

def show():
	render_header("📜 Audit Logs","Trackers of Requests and Actions")
	db = SessionLocal()
	try:
		logs = (db.query(AuditLog).order_by(AuditLog.timestamp.desc()).all())
		rows = []
		for log in logs:
			rows.append({"User":log.user_name,"Action":log.action,"Timestamp":log.timestamp})
		st.dataframe(rows,width='stretch')
	finally:
		db.close()