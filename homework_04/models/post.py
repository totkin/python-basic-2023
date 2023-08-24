"""
для модели Post обязательными являются user_id, title, body
"""

from datetime import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Text,
    func,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin


class Post(CreatedAtMixin, Base):
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )
    title = Column(
        String(120),
        nullable=False,
        unique=False,
    )
    body = Column(
        Text,
        nullable=False,
        unique=False,
        default="",
        server_default="",
    )

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )

    @property
    def body_len(self):
        return len(self.body)

    def __str__(self):
        return f"Post(id={self.id}, title={self.title!r})"

    def __repr__(self):
        return str(self)
