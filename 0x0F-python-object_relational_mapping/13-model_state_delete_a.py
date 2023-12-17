#!/usr/bin/python3
"""Module that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa"""


if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    selected_state = session.query(State).where(State.name.contains('a'))
    for state in selected_state:
        session.delete(state)
        session.commit()

    session.close()
