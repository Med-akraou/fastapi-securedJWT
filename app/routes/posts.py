from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services import post_service
from ..db.database import get_db
from ..schemas.post import * 
from typing import Annotated
from ..schemas.token import CurrentUser
from ..core.auth import has_role, get_current_user
from typing import List


router = APIRouter()


@router.get('/posts')
def get_all_posts(
    current_user: Annotated[CurrentUser, Depends(has_role("admin"))],
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    ):
    return post_service.fetch_all_posts(db,skip,limit)


@router.get("/posts/{id}", response_model=Post)
def get_post(
    id: int, 
    current_user: Annotated[CurrentUser, Depends(get_current_user)],
    db: Session = Depends(get_db)
    ):
    return post_service.fetch_post_by_id(db,current_user,id)


@router.post("/posts", response_model=Post)
def create_post(
    post: PostCreate,
    current_user: Annotated[CurrentUser, Depends(get_current_user)],
    db: Session = Depends(get_db)
    ):
    return post_service.create_post(db, current_user, post)


@router.put("/posts/{id}", response_model=Post)
def update_post(
    id: int,
    post: PostUpdate,
    current_user: Annotated[CurrentUser, Depends(get_current_user)],
    db: Session = Depends(get_db)
    ):
    return post_service.update_post(db, current_user, id, post)


@router.delete("/posts/{id}")
def delete_post(
    id: int,
    current_user: Annotated[CurrentUser, Depends(get_current_user)],
    db: Session = Depends(get_db)
    ):
    return post_service.remove_post(db, current_user, id)


@router.get('/users/{id}/posts', response_model=List[Post])
def get_posts_of_user(
    id: int,
    current_user: Annotated[CurrentUser, Depends(get_current_user)],
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
):
    return post_service.fetch_posts_of_user(db, current_user,id, skip=skip, limit=limit)
