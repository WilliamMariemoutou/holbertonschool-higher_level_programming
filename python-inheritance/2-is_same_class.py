#!/usr/bin/python3
"""creates an object to check if its in the same class"""


def is_same_class(obj, a_class):
    """checks if an obkect is the instance of a specified class
    obj: the object to check
    a_class: the class to compare the object to
    returns: true if it is an instance of the class
    """
    return type(obj) is a_class
