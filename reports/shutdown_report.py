import pandas as pd
from services.shutdown_service import (ShutdownService)

class ShutdownReport:
	@staticmethod
	def get_dataframe():
		requests = (ShutdownService.get_all_requests())
		rows = []
		for req in requests:
			rows.append({"Request No":req.request_no,"Asset":req.asset,"Location":req.location,"Priority":req.priority,"Status":req.status,"Current Role":req.current_role,"Created By":req.created_by,"Start Time":req.start_time.strftime("%d-%m-%Y %H:%M") if req.start_time else "","End Time":req.end_time.strftime("%d-%m-%Y %H:%M") if req.end_time else "","Created At":req.created_at.strftime("%d-%m-%Y %H:%M") if req.created_at else ""})
		return pd.DataFrame(rows)
	@staticmethod
	def export_excel(file_path):
		df = (ShutdownReport.get_dataframe())
		df.to_excel(file_path,index=False)
		return file_path
	@staticmethod
	def get_summary():
		df = (ShutdownReport.get_dataframe())
		return {"total":len(df),"approved":len(df[df["Status"]=="Approved"]),"pending":len(df[df["Status"]=="Pending"]),"rejected":len(df[df["Status"]=="Rejected"])}