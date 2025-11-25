#!/usr/bin/python3
"""
Define a State class that links to the `states` table in the database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for declarative models
Base = declarative_base()


class State(Base):
    """ State class that links to the `states` table in the database """
    __tablename__ = 'states'  # Link to the states table

    # Define the columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """ Return the string representation of a State object """
        return f"<State(id={self.id}, name={self.name})>"
