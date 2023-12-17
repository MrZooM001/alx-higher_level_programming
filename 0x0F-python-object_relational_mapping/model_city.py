#!/usr/bin/python3
"""Module that contains the class definition of a City
and an instance Base = declarative_base()"""


from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Class to represent a City model with an inheritance from Base class

    Attributes:
        id (int): city id as primary key.
        name (str): city name.
        __tablename__ (str): table name in the database in MySQL server.
        state_id (int): state id as foreign key.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
