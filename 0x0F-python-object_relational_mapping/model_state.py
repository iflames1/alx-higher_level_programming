#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table states
    """
    __tablename__ = "states"

    id = Column(Integer,  primary_key=True, autoincrement=tuple,
                nullable=False)
    name = Column(String(128), nullable=False)
