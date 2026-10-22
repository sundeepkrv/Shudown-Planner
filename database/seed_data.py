from sqlalchemy.orm import Session
from database.db import engine
from database.models import (Base,User,Workflow)
from auth.password import hash_password

def seed_database():
	Base.metadata.create_all(bind=engine)
	db = Session(bind=engine)
	try:
		existing_users = (db.query(User).count())
		if existing_users == 0:
			users = [
				User(username="engineer",full_name="Requestor User",email="engineer@test.com",password_hash=hash_password("123"),role="Requestor"),
				User(username="reviewer",full_name="Reviewer User",email="reviewer@test.com",password_hash=hash_password("123"),role="Reviewer"),
				User(username="manager",full_name="Manager User",email="manager@test.com",password_hash=hash_password("123"),role="Manager"),
				User(username="approver",full_name="Approver User",email="approver@test.com",password_hash=hash_password("123"),role="Approver"),
				User(username="admin",full_name="System Admin",email="admin@test.com",password_hash=hash_password("123"),role="Admin")
			]
			db.add_all(users)
		workflow_count = (db.query(Workflow).count())
		if workflow_count == 0:
			workflow = Workflow(workflow_name="Default Shutdown Workflow",role_sequence="Reviewer,Manager,Approver",active=True)
			db.add(workflow)
		db.commit()
		print("Database initialized successfully.")
	except Exception as ex:
		db.rollback()
		print(ex)
	finally:
		db.close()

if __name__ == "__main__":
	seed_database()