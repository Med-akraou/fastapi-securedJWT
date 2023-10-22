from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    roles: List[str] = []

    class Config:
        orm_mode = True

class FormLogin(BaseModel):
    username: str
    password: str

class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True

class UserRole(BaseModel):
    username: str
    role: str

