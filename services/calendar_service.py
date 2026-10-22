from database.db import SessionLocal
from database.models import (ShutdownRequest)

class CalendarService:
	@staticmethod
	def get_calendar_events():
		db = SessionLocal()
		try:
			requests = (db.query(ShutdownRequest).all())
			events = []
			for req in requests:
				color = "#f39c12"
				if req.status == "Approved":
					color = "#27ae60"
				elif req.status == "Rejected":
					color = "#e74c3c"
				events.append({"title":req.request_no,"start":req.start_time.isoformat(),"end":req.end_time.isoformat(),"color":color})
			return events
		finally:
			db.close()