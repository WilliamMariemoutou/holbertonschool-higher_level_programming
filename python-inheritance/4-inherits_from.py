#!/usr/bin/python3
"""the class that the object will be checked from"""


def inherits_from(obj, a_class):
    """check if the object is inherited directly or indirectly
    from the specified class, otherwise false
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
