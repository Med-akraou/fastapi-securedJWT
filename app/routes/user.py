from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services import user_service
from ..db.database import get_db
from ..schemas.user import * 
from ..schemas.token import *
from ..core.auth import authenticate_user, create_access_token
from datetime import datetime, timedelta

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user_service(db, user)


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form: FormLogin,db: Session = Depends(get_db)
):
    u = authenticate_user(db,form.username, form.password)
    if not u:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": u.email,"id":u.id,"roles": [role.name for role in u.roles]}, expires_delta = access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# add role to user given user username and role name json
@router.post("/users/role", response_model=User)
def add_role_to_user(user_role: UserRole, db: Session = Depends(get_db)):
    return user_service.add_role_to_user(db, user_role.username, user_role.role_name)



