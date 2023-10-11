from sqlalchemy.orm import Session
from ..models.user import User 
from ..schemas.user import UserCreate

def create_user(db: Session, user: UserCreate): 
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.email == username).first()
