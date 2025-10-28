#!/usr/bin/python3
"""returns the dictionary description of a data structure"""


def class_to_json(obj):
    """return the dictionary description for JSon serialization of an object"""
    return obj.__dict__
