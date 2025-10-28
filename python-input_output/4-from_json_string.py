#!/usr/bin/python3
"""functions that return an obhect"""


import json


def from_json_string(my_str):
    """returns the object representedd by JSON string"""
    return json.loads(my_str)
