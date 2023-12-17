#!/usr/bin/python3
"""Module that prints all City objects from the database hbtn_0e_14_usa"""


if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    all_cities = session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id)
    for city in all_cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))

    session.close()
