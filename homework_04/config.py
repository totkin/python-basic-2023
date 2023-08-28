DB_URL = "postgresql+pg8000://username:passwd@localhost:5432/blog"
ASYNC_DB_URL = DB_URL.replace("pg8000", "asyncpg")
DB_ECHO = False
PG_USER = username
PG_PASS = passwd
PG_DB = blog
# DB_ECHO = True
