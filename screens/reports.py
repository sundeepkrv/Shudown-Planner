import streamlit as st
from pathlib import Path
from datetime import datetime
from reports.shutdown_report import (ShutdownReport)
from reports.approval_report import (ApprovalReport)
from reports.audit_report import (AuditReport)
from components.header import (render_header)

EXPORT_FOLDER = Path("exports")

def generate_filename(report_type):
	username = st.session_state.username
	timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
	return str(EXPORT_FOLDER / f"{report_type}_{username}_{timestamp}.xlsx")

def report_row(title,report_type,export_function,session_key,generate_icon="📄"):
	col1, col2, col3 = st.columns([5, 1, 1])
	with col1:
		st.markdown(f"""**{title}**""")
	with col2:
		if st.button(f"{generate_icon} Generate",key=f"gen_{report_type}"):
			file_path = generate_filename(report_type)
			export_function(file_path)
			st.session_state[session_key] = file_path
			st.toast(f"{Path(file_path).name} created.")
	with col3:
		if session_key in st.session_state:
			report_file = (st.session_state[session_key])
			if Path(report_file).exists():
				with open(report_file,"rb") as f:
					st.download_button("⬇️ Download",data=f,file_name=Path(report_file).name,mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",key=f"dl_{report_type}")

def show():
	render_header("📊 Reports","Generate and Download Operational Reports")
	report_row(title="Shutdown Report",report_type="shutdown_report",export_function=ShutdownReport.export_excel,session_key="shutdown_report_file",generate_icon="📄")
	report_row(title="Approval Report",report_type="approval_report",export_function=ApprovalReport.export_excel,session_key="approval_report_file",generate_icon="✅")
	report_row(title="Audit Report",report_type="audit_report",export_function=AuditReport.export_excel,session_key="audit_report_file",generate_icon="📝")