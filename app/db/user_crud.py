from sqlalchemy.orm import Session
from ..models.user import User, Role
from ..schemas.user import UserCreate


def create_user(db: Session, user: UserCreate):
    db.add(user)
    db.commit()
    db.refresh(user)


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.email == username).first()


def get_role(db: Session, role_name: str):
    return db.query(Role).filter(Role.name == role_name).first()


def add_role_to_user(db: Session, db_user):
    db.commit()
    db.refresh(db_user)
