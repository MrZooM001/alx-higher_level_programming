#!/usr/bin/python3
"""Module that lists all City objects from the database hbtn_0e_101_usa"""


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

    selected_cities = session.query(City.id, City.name, State.name).filter(
        City.state_id == State.id)
    for city in selected_cities:
        print("{}: {} -> {}".format(city[0], city[1], city[2]))

    session.close()
