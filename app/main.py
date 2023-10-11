from fastapi import FastAPI
from app.db.database import Base, engine
from .routes import posts,user


app = FastAPI()
app.include_router(posts.router)
app.include_router(user.router)

Base.metadata.create_all(bind=engine)

