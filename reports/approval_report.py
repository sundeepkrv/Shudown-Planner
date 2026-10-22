import pandas as pd
from database.db import (SessionLocal)
from database.models import (ApprovalHistory)

class ApprovalReport:
	@staticmethod
	def get_dataframe():
		db = SessionLocal()
		try:
			history = (db.query(ApprovalHistory).all())
			rows = []
			for item in history:
				rows.append({"Request No":item.request_no,"Role":item.role,"Action":item.action,"Action By":item.action_by,"Remarks":item.remarks,"Action Time":item.action_time.strftime("%d-%m-%Y %H:%M") if item.action_time else ""})
			return pd.DataFrame(rows)
		finally:
			db.close()
	@staticmethod
	def export_excel(file_path):
		df = (ApprovalReport.get_dataframe())
		df.to_excel(file_path,index=False)
		return file_path
	@staticmethod
	def approval_count_by_role():
		df = (ApprovalReport.get_dataframe())
		if df.empty:
			return pd.DataFrame()
		return (df.groupby("Role").size().reset_index(name="Count"))