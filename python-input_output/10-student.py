#!/usr/bin/python3
"""creates a class student"""


class Student:
    """defines a student class"""

    def __init__(self, first_name, last_name, age):
        """initialize a new student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return the dictionary representation of the student class
        if attrs is a list of string, retrieves the attributes name
        else returns all attributes
        """
        if isinstance(attrs, list):
            result = {}
            for key in attrs:
                if isinstance(key, str) and hasattr(self, key):
                    result[key] = getattr(self, key)
            return result

        return self.__dict__
