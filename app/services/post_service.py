from sqlalchemy.orm import Session
from ..db import post_crud
from fastapi import HTTPException
from ..models.post import Post
from ..schemas import post
from ..schemas.token import CurrentUser


def fetch_all_posts(db: Session, skip: int, limit: int ):
    return post_crud.get_all_posts(db, skip, limit)


def fetch_post_by_id(db: Session, current_user: CurrentUser , id: int):
    post = post_crud.get_post(db, id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.user_id == current_user.id or "admin" in current_user.roles:
        return post
    
    raise HTTPException(status_code=403, detail="Unauthorized: You don't have access")

def create_post(db: Session,current_user: CurrentUser , post_data: post.PostCreate):
    new_post = Post(**post_data.dict())
    new_post.user_id = current_user.id
    db_post = post_crud.save_post(db, new_post)
    if db_post is None:
        raise HTTPException(status_code=400, detail="Error creating the post")
    return db_post


def update_post(db: Session, current_user: CurrentUser , id: int, post_data: post.PostUpdate):
    db_post = fetch_post_by_id(db,current_user,id)
    # Convert the post data to a dictionary and filter out None values
    update_data = {k: v for k, v in post_data.dict().items() if v is not None}
    for key, value in update_data.items():
        setattr(db_post, key, value)

    return post_crud.update_post(db, db_post)

    

def remove_post(db: Session, current_user: CurrentUser , id: int):
    db_post = fetch_post_by_id(db,current_user,id)
    post_crud.delete_post(db, db_post)
    return {"status": "success", "message": "Post deleted successfully"}


def fetch_posts_of_user(db: Session, current_user:CurrentUser ,id: int, skip: int, limit: int):
    if current_user.id != id and "admin" not in current_user.roles:
        raise HTTPException(status_code=403, detail="Unauthorized: You don't have access")
        
    return post_crud.get_posts_of_user(db, id, skip=skip, limit=limit)

