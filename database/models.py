from sqlalchemy import (Column,Integer,String,Text,DateTime,Boolean,ForeignKey)
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

# =====================================================
# USERS
# =====================================================

class User(Base):
	__tablename__ = "users"
	id = Column(Integer,primary_key=True)
	username = Column(String(100),unique=True,nullable=False)
	full_name = Column(String(200))
	email = Column(String(200))
	password_hash = Column(String(255),nullable=False)
	role = Column(String(50),nullable=False)
	active = Column(Boolean,default=True)
	created_at = Column(DateTime,default=datetime.utcnow)
	updated_at = Column(DateTime,default=datetime.utcnow)

# =====================================================
# SHUTDOWN REQUESTS
# =====================================================

class ShutdownRequest(Base):
	__tablename__ = "shutdown_requests"
	id = Column(Integer,primary_key=True)
	request_no = Column(String(50),unique=True)
	asset = Column(String(200))
	location = Column(String(200))
	reason = Column(Text)
	priority = Column(String(20))
	start_time = Column(DateTime)
	end_time = Column(DateTime)
	status = Column(String(50),default="Pending")
	current_role = Column(String(50),default="Reviewer")
	created_by = Column(String(100))
	created_at = Column(DateTime,default=datetime.utcnow)
	updated_at = Column(DateTime,default=datetime.utcnow)

# =====================================================
# APPROVAL HISTORY
# =====================================================

class ApprovalHistory(Base):
	__tablename__ = "approval_history"
	id = Column(Integer,primary_key=True)
	request_no = Column(String(50))
	action_by = Column(String(100))
	role = Column(String(50))
	action = Column(String(50))
	remarks = Column(Text)
	action_time = Column(DateTime,default=datetime.utcnow)

# =====================================================
# AUDIT LOGS
# =====================================================

class AuditLog(Base):
	__tablename__ = "audit_logs"
	id = Column(Integer,primary_key=True)
	user_name = Column(String(100))
	action = Column(String(200))
	entity_type = Column(String(100))
	entity_id = Column(String(100))
	timestamp = Column(DateTime,default=datetime.utcnow)

# =====================================================
# WORKFLOWS
# =====================================================

class Workflow(Base):
	__tablename__ = "workflows"
	id = Column(Integer,primary_key=True)
	workflow_name = Column(String(100))
	role_sequence = Column(Text)
	active = Column(Boolean,default=True)