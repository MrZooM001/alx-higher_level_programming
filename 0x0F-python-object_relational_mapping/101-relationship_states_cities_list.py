#!/usr/bin/python3
"""Module that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""


if __name__ == '__main__':
    from sys import argv
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    selected_state = session.query(State).order_by(State.id)
    for state in selected_state:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("{}{}: {}".format("\t".expandtabs(4), city.id, city.name))

    session.close()
