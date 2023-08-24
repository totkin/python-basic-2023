from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import declarative_base, declared_attr

import config

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
)


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)