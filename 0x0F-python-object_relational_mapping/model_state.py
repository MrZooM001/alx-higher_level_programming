#!/usr/bin/python3
"""Module that contains the class definition of a State and an instance Base = declarative_base()"""


from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

meta_data = MetaData()
Base = declarative_base(metadata=meta_data)


class State(Base):
    """Class to represent a State model with an inheritance from Base class

    Attributes:
        id (int): state id as primary key.
        name (str): state name.
        __tablename__ (str): table name in the database in MySQL server.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
