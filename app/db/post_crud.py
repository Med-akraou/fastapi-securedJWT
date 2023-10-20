
from sqlalchemy.orm import Session
from ..schemas import post
from ..models.post import Post 


def get_all_posts(db: Session , skip: int, limit: int):
    return db.query(Post).offset(skip).limit(limit).all()

def get_post(db: Session, id: int):
    return db.query(Post).filter(Post.id == id).first()

def save_post(db: Session, post_data: post.PostCreate):
    db.add(post_data)
    db.commit()
    db.refresh(post_data)
    return post_data


def update_post(db: Session, post_data: post.PostUpdate):
    db.commit()
    db.refresh(post_data)
    return post_data


def delete_post(db: Session, db_post):
    db.delete(db_post)
    db.commit()


