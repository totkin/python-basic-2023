"""
для модели User обязательными являются name, username, email
"""

from sqlalchemy import (Column,String,)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin


class BaseUser(CreatedAtMixin, Base):
    __abstract__ = True

    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=True, unique=True)


class User(BaseUser):
    name = Column(String(32), nullable=False, unique=True)
    posts = relationship("Post",back_populates="user",uselist=True,)

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r}, name={self.name!r}, email={self.email!r})"

    def __repr__(self):
        return str(self)
