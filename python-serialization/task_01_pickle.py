#!/usr/bin/python3
"""Serialize and deserialize python objects"""


import pickle


class CustomObject:
    """the class object"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_studemt = is_student

    def diplay(self):
        """display the information required"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialize the file and check if file is not malformed"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
                print(f"Object serialized to {filename}")
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
