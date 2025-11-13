#!/usr/bin/python3

"""
Data Model for Amenity
----------------------
Defines the structure and behavior of an Amenity object in the HBnB system.
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity model class representing a feature or facility."""

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
