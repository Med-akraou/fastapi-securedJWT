from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.user import *
from ..models import user
from ..db import user_crud


def get_user_by_username(db: Session, username: str):
    user = user_crud.get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def create_user_service(db: Session, user_data: UserCreate):
    from ..core.auth import get_password_hash

    db_user = user_crud.get_user_by_username(db, user_data.email)

    if db_user:
        raise HTTPException(
            status_code=409, detail="Conflict! Email already registered"
        )

    hashed_password = get_password_hash(user_data.password)
    db_user = user.User(
        firstname=user_data.firstname,
        lastname=user_data.lastname,
        email=user_data.email,
        password=hashed_password,
    )
    user_crud.create_user(db, db_user)
    return status.HTTP_201_CREATED


def add_role_to_user(db: Session, username: str, role_name: str):
    db_user = get_user_by_username(db, username)
    db_role = user_crud.get_role(db, role_name)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    db_user.roles.append(db_role)
    user_crud.add_role_to_user(db, db_user)
