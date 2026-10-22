from sqlalchemy.orm import Session
from database.models import User
from auth.password import (verify_password)
from auth.session_manager import (set_user_session)

def authenticate_user(db: Session,username: str,password: str):
	user = (db.query(User).filter(User.username == username).first())
	if not user:
		return False, "Invalid username"
	if not user.active:
		return False, "User inactive"
	if not verify_password(password,user.password_hash):
		return False, "Invalid password"
	set_user_session(user)
	return True, "Login successful"