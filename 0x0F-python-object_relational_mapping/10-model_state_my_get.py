#!/usr/bin/python3
"""Module that lists all State objects from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    selected_state = session.query(State).filter(State.name == argv[4])
    try:
        print("{}".format(selected_state[0].id))
    except IndexError:
        print("Not found")
