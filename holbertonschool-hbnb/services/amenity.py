#!/usr/bin/python3

# services/facade.py
"""
Facade Layer
-------------
This class helps manage the business logic for amenities in the HBnB app.
It acts as a middleman between the API and the data storage.

The methods below handle creating, reading, and updating amenities.
"""

from models.amenity import Amenity
from uuid import UUID


class HBnBFacade:
    """Handles business logic for amenities in the HBnB system."""

    def __init__(self, storage):
        """
        Initialize the Facade with a storage engine.

        :param storage: The storage system used to save and retrieve data
        """
        self.storage = storage

    def create_amenity(self, amenity_data):
        """
        Create a new amenity.

        :param amenity_data: A dictionary with 'name' of the amenity
        :return: The newly created Amenity object
        :raises ValueError: If the name is missing or invalid
        """
        name = amenity_data.get("name")
        if not name or not name.strip():
            raise ValueError("Name is required")

        new_amenity = Amenity(name=name.strip())
        self.storage.new(new_amenity)
        self.storage.save()
        return new_amenity

    def get_amenity(self, amenity_id):
        """
        Get an amenity by its ID.

        :param amenity_id: The unique ID of the amenity
        :return: The Amenity object or None if not found
        """
        try:
            UUID(amenity_id)  # Check if ID is valid
        except ValueError:
            return None  # If the ID is not valid

        return self.storage.get(Amenity, amenity_id)

    def get_all_amenities(self):
        """
        Get all amenities.

        :return: A list of all Amenity objects
        """
        return list(self.storage.all(Amenity).values())

    def update_amenity(self, amenity_id, amenity_data):
        """
        Update an amenity by ID.

        :param amenity_id: The ID of the amenity
        :param amenity_data: A dictionary with the new 'name'
        :return: The updated Amenity object, or None if not found
        :raises ValueError: If the name is invalid
        """
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None  # Amenity not found

        name = amenity_data.get("name")
        if not name or not name.strip():
            raise ValueError("Name is required")

        amenity.name = name.strip()
        self.storage.save()
        return amenity
