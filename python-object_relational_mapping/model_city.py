#!/usr/bin/python3
"""
Class definition for City that maps to the cities table in MySQL
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    Class representing a City linked to the 'cities' table in the database
    """
    __tablename__ = 'cities'

    # Define columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Relationship with the State table (optional, but can be useful for ORM)
    state = relationship("State", back_populates="cities")
