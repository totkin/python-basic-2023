from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, declared_attr

import config

async_engine = create_async_engine(
    url=config.ASYNC_DB_URL,
    echo=config.DB_ECHO,
)

engine = create_engine(url=config.DB_URL, echo=config.DB_ECHO)

class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)

Session = sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
