from pydantic import BaseModel
from typing import List


class Token(BaseModel):
    access_token: str
    token_type: str


class CurrentUser(BaseModel):
    username: str
    id: int
    roles: List[str]
