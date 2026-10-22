from datetime import datetime
from database.db import SessionLocal
from database.models import AuditLog

class AuditService:
	@staticmethod
	def log(user_name,action,entity_type=None,entity_id=None):
		db = SessionLocal()
		try:
			audit = AuditLog(user_name=user_name,action=action,entity_type=entity_type,entity_id=entity_id,timestamp=datetime.utcnow())
			db.add(audit)
			db.commit()
		finally:
			db.close()