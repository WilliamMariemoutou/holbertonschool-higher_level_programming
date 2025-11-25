#!/usr/bin/python3
"""
Change the name of the State object where id = 2
to "New Mexico" in the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the engine to connect to MySQL
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # If state is found, update the name
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
