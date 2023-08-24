#!/usr/bin/python3
"""
This script lists all State objects
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    Base.metadata.create_all(engine)

    s_tate = session.query(State).order_by(State.id).all()
    for state in s_tate:
        print("{}: {}".format(state.id, state.name))
    session.close()
