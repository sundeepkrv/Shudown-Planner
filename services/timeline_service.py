from datetime import datetime
from database.db import SessionLocal
from database.models import (ApprovalHistory)

class TimelineService:
	@staticmethod
	def add_event(request_no,action_by,role,action,remarks=None):
		db = SessionLocal()
		try:
			event = ApprovalHistory(request_no=request_no,action_by=action_by,role=role,action=action,remarks=remarks,action_time=datetime.utcnow())
			db.add(event)
			db.commit()
		finally:
			db.close()
	@staticmethod
	def get_timeline(request_no):
		db = SessionLocal()
		try:
			return (db.query(ApprovalHistory).filter(ApprovalHistory.request_no==request_no).order_by(ApprovalHistory.action_time).all())
		finally:
			db.close()