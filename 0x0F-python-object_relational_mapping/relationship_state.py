#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    State class that links to the MySQL table states
    """
    __tablename__ = "states"

    id = Column(Integer, unique=True,  primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")
