"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio

import aiohttp
import ujson as ujson

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> dict:
    async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
        async with session.get(url) as response:
            return await response.json(loads=ujson.loads)


async def async_fetch_users() -> dict:
    return await fetch_json(USERS_DATA_URL)


async def async_fetch_posts() -> dict:
    return await fetch_json(POSTS_DATA_URL)


async def make_all_fetch():
    await async_fetch_users()
    await async_fetch_posts()
    await fetch_json(USERS_DATA_URL)
