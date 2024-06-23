#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        mysql_username, mysql_password, database_name
    ))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    states_to_delete = session.query(State).filter(
        State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()

    session.close()
