from database.db import SessionLocal
from database.models import User
from auth.password import (hash_password)

class UserService:
	@staticmethod
	def get_all_users():
		db = SessionLocal()
		try:
			return db.query(User).all()
		finally:
			db.close()
	@staticmethod
	def get_user(username):
		db = SessionLocal()
		try:
			return (db.query(User).filter(User.username==username).first())
		finally:
			db.close()
	@staticmethod
	def reset_password(username,new_password):
		db = SessionLocal()
		try:
			user = (db.query(User).filter(User.username==username).first())
			if not user:
				return False
			user.password_hash = (hash_password(new_password))
			db.commit()
			return True
		finally:
			db.close()