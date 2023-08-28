"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio

import aiohttp
import ujson as ujson
from loguru import logger

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> dict:
    logger.info("fetch url {}", url)
    async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
        async with session.get(url) as response:
            logger.info("fetched url {} and got data {}", response.url, response)
            return await response.json(loads=ujson.loads)


async def async_fetch_users() -> dict:
    return await fetch_json(USERS_DATA_URL)


async def async_fetch_posts() -> dict:
    return await fetch_json(POSTS_DATA_URL)


async def make_all_fetch():
    await async_fetch_users()
    await async_fetch_posts()
    await fetch_json(USERS_DATA_URL)


# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(make_all_fetch())

