from ..db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = Column(Integer, primary_key=True)
    title: Mapped[str] = Column(String, nullable=False)
    content: Mapped[str] = Column(String, nullable=False)
    published: Mapped[bool] = Column(Boolean, default=True)

    # Foreign key for the user who created the post
    user_id: Mapped[int] = Column(Integer, ForeignKey("users.id"))

    # Relationship with User model
    user: Mapped["User"] = relationship("User", back_populates="posts")
