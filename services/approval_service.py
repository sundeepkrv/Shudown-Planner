from database.db import SessionLocal
from database.models import (ShutdownRequest)
from services.workflow_service import (WorkflowService)
from services.timeline_service import (TimelineService)
from services.audit_service import (AuditService)

class ApprovalService:
	@staticmethod
	def approve(request_no,approver,role,remarks):
		db = SessionLocal()
		try:
			request = (db.query(ShutdownRequest).filter(ShutdownRequest.request_no==request_no).first())
			if not request:
				return False
			if (WorkflowService.is_final_approver(role)):
				request.status = ("Approved")
				request.current_role = ("Completed")
			else:
				request.current_role = (WorkflowService.get_next_role(role))
			db.commit()
			TimelineService.add_event(request_no,approver,role,"Approved",remarks)
			AuditService.log(approver,"Approved Request","ShutdownRequest",request_no)
			return True
		finally:
			db.close()
	@staticmethod
	def reject(request_no,approver,role,remarks):
		db = SessionLocal()
		try:
			request = (db.query(ShutdownRequest).filter(ShutdownRequest.request_no==request_no).first())
			request.status = ("Rejected")
			db.commit()
			TimelineService.add_event(request_no,approver,role,"Rejected",remarks)
			AuditService.log(approver,"Rejected Request","ShutdownRequest",request_no)
			return True
		finally:
			db.close()
	@staticmethod
	def pending_for_role(role):
		db = SessionLocal()
		try:
			return (db.query(ShutdownRequest).filter(ShutdownRequest.current_role==role,ShutdownRequest.status=="Pending").all())
		finally:
			db.close()