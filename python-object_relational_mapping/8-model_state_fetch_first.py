#!/usr/bin/python3
"""
Print the first State object from the database hbtn_0e_6_usa.
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

    # Query the first state, ordered by id
    state = session.query(State).order_by(State.id).first()

    # Check if the table is empty
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
