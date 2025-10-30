#!/usr/bin/python3
"""Serialize and deserialize python objects"""


import pickle


class CustomObject:
    """the custom object for serializing and deserializing"""
    def __init__(self, name, age, is_student):
        """initializes the class with the given attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """display the attributes required"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialize the file and check if file is not malformed"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error during serialization: {e}")

    @classmethod
    def deserialize(cls, filename):
        """deserialize the file and check again for any malformation"""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                return obj
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Error during deserialization: {e}")
            return None
