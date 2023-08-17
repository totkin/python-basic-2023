"""
Create
Read
Update
Delete
"""
from typing import Optional

from pydantic import BaseModel
from .schemas import User


class Storage(BaseModel):
    users: dict[int, User] = {}
    last_id: int = 0

    @property
    def next_id(self):
        self.last_id += 1
        return self.last_id

    def create_user(self, username: str) -> User:
        user = User(id=self.next_id, username=username)
        self.users[user.id] = user
        return user


storage = Storage()

storage.create_user("Ivan")
storage.create_user("Sam")
storage.create_user("Petr")


async def get_users() -> list[User]:
    return list(storage.users.values())


async def create_user(username: str) -> User:
    return storage.create_user(username=username)


async def get_user_by_id(user_id: int) -> Optional[User]:
    return storage.users.get(user_id)
