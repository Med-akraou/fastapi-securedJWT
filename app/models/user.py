from ..db.database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey
from typing import List

user_roles = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("role_id", Integer, ForeignKey("roles.id")),
)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True)
    firstname: Mapped[str] = Column(String, index=True)
    lastname: Mapped[str] = Column(String, index=True)
    email: Mapped[str] = Column(String, unique=True, index=True)
    password: Mapped[str] = Column(String)

    # Relationship with Post model
    posts: Mapped[List["Post"]] = relationship("Post", back_populates="user")

    # many to many Relationship with Role
    roles: Mapped[List["Role"]] = relationship(
        "Role", secondary=user_roles, back_populates="users"
    )


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, unique=True)

    # many to many relationship with User
    users: Mapped[List["User"]] = relationship(
        "User", secondary=user_roles, back_populates="roles"
    )
