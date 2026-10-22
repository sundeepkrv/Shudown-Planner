from datetime import datetime
from database.db import SessionLocal
from database.models import (ShutdownRequest)
from services.timeline_service import (TimelineService)
from services.audit_service import (AuditService)

class ShutdownService:
	@staticmethod
	def generate_request_no():
		return ("SHD-"+datetime.now().strftime("%Y%m%d%H%M%S"))
	@staticmethod
	def create_request(asset,location,reason,priority,start_time,end_time,created_by):
		request_no = (ShutdownService.generate_request_no())
		db = SessionLocal()
		try:
			request = ShutdownRequest(request_no=request_no,asset=asset,location=location,reason=reason,priority=priority,start_time=start_time,end_time=end_time,status="Pending",current_role="Reviewer",created_by=created_by)
			db.add(request)
			db.commit()
			TimelineService.add_event(request_no=request_no,action_by=created_by,role="Requestor",action="Created",remarks=reason)
			AuditService.log(user_name=created_by,action="Created Shutdown Request",entity_type="ShutdownRequest",entity_id=request_no)
			return request_no
		finally:
			db.close()
	@staticmethod
	def get_all_requests():
		db = SessionLocal()
		try:
			return db.query(ShutdownRequest).all()
		finally:
			db.close()
	@staticmethod
	def get_request(request_no):
		db = SessionLocal()
		try:
			return (db.query(ShutdownRequest).filter(ShutdownRequest.request_no==request_no).first())
		finally:
			db.close()
	@staticmethod
	def get_requests_by_user(username):
		db = SessionLocal()
		try:
			return (db.query(ShutdownRequest).filter(ShutdownRequest.created_by==username).all())
		finally:
			db.close()