# -*- coding: utf-8 -*-


from sqlalchemy import (Column, Float, Integer, String, Text, create_engine,
                        func)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import TIMESTAMP

from .config import DB_CONNECTION

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(DB_CONNECTION, encoding="utf8")


def create_table(engine):
    Base.metadata.create_all(engine)


class HouseInfoModel(Base):
    __tablename__ = "house_info"

    id = Column(Integer, primary_key=True)
    community_name = Column("community_name", String(255), index=True)
    url = Column("url", Text(), unique=True)
    square_meter = Column("square_meter", Float)
    avg_square_meter = Column("avg_square_meter", String(50))
    total = Column("total_price", String(50), index=True)
    floor_plan = Column("floor_plan", String(15), index=True)
    type = Column("type", String(15), index=True)
    direction = Column("direction", String(15), index=True)
    created_time = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_time = Column(
        TIMESTAMP,
        nullable=False,
        default=func.now(),
    )
