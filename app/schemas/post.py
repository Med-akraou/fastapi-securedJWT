from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4


class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True


class PostCreate(BaseModel):
    title: str
    content: str
    published: bool = True


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None
