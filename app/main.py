from fastapi import FastAPI
from app.db.database import Base, engine
from .routes import posts


app = FastAPI()
app.include_router(posts.router)

Base.metadata.create_all(bind=engine)

