#!/usr/bin/python3
"""
Contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class City(Base):
    """
    City class that links to the MySQL table cities
    """
    __tablename__ = "cities"

    id = Column(Integer, unique=True,  primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
