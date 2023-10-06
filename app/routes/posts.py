from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services import post_service
from ..db.database import get_db
from ..schemas.post import * 

router = APIRouter()

@router.get('/posts')
def get_all_posts_endpoint(db: Session = Depends(get_db)):
    return post_service.fetch_all_posts(db)

@router.get("/posts/{id}", response_model=Post)
def get_post(id: int, db: Session = Depends(get_db)):
    return post_service.fetch_post_by_id(db, id)

@router.post("/posts", response_model=Post)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return post_service.create_post(db, post)

@router.put("/posts/{id}", response_model=Post)
def update_post(id: int, post: PostUpdate, db: Session = Depends(get_db)):
    return post_service.update_post(db, id, post)

@router.delete("/posts/{id}")
def delete_post(id: int, db: Session = Depends(get_db)):
    return post_service.remove_post(db, id)
