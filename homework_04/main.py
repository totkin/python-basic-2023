"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
import sys

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from jsonplaceholder_requests import async_fetch_users, async_fetch_posts
from models import Base, User, Post, async_engine


metadata = MetaData()


async def create_schemas():
    async with async_engine.begin() as schema_connection:
        await schema_connection.run_sync(Base.metadata.drop_all)
        await schema_connection.run_sync(Base.metadata.create_all)


async def async_create_users_and_posts():
    users_data, posts_data = await asyncio.gather(async_fetch_users(), async_fetch_posts())
    async with AsyncSession(async_engine) as session:
        async with session.begin():
            for user in users_data:
                session.add(User(id=user['id'], name=user['name'], username=user['username'], email=user['email']))
            for post in posts_data:
                session.add(Post(id=post['id'], user_id=post['userId'], title=post['title'], body=post['body']))
        await session.commit()
        await session.close()


async def async_main():
    await create_schemas()
    await async_create_users_and_posts()
    await async_engine.dispose()


def main():
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
