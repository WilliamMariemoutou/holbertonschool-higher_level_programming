#!/usr/bin/python3
"""creates a class student"""


class Student:
    """defines a student class"""
    
    def __init__(self, first_name, last_name, age):
        """initialize a new student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self):
        """return the dictionary representation of the student class"""
        return self.__dict__
