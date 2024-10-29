from sqlalchemy.orm import Session
from models import user
from schemas import UserCreate
from routers.auth import get_password_hash, verify_password

def get_user_by_email(db: Session, email: str):
    return db.query(user).filter(user.email == email).first()

from sqlalchemy.orm import Session
from app.models import User

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email, password=user.password)  # Use the hashed password
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



def authenticate_user(db: Session, username: str, password: str):
    user = db.query(user).filter(user.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
