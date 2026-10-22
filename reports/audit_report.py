import pandas as pd
from database.db import (SessionLocal)
from database.models import (AuditLog)

class AuditReport:
	@staticmethod
	def get_dataframe():
		db = SessionLocal()
		try:
			logs = (db.query(AuditLog).order_by(AuditLog.timestamp.desc()).all())
			rows = []
			for log in logs:
				rows.append({"User":log.user_name,"Action":log.action,"Entity Type":log.entity_type,"Entity ID":log.entity_id,"Timestamp":log.timestamp.strftime("%d-%m-%Y %H:%M") if log.timestamp else ""})
			return pd.DataFrame(rows)
		finally:
			db.close()
	@staticmethod
	def export_excel(file_path):
		df = (AuditReport.get_dataframe())
		df.to_excel(file_path,index=False)
		return file_path
	@staticmethod
	def user_activity_summary():
		df = (AuditReport.get_dataframe())
		if df.empty:
			return pd.DataFrame()
		return (df.groupby("User").size().reset_index(name="Activity Count").sort_values("Activity Count",ascending=False))