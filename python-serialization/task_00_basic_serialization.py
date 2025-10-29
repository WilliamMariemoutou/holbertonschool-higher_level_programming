#!/usr/bin/python3
"""functions to serialize a Python dictionary
into a JSON file and back into a dictionary
"""


import json


def serialize_and_save_to_file(data, filename):
    """serialize a dictionary and save it in a file"""

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        """returns the serialized file"""


def load_and_deserialze(filename):
    """load and deserialize Json file into  python dictionary"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
    """returns the deserialized file"""
