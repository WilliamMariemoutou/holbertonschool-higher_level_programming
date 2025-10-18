#!/usr/bin/python3

"""
This module defines a function add_integer(a, b=98).
The function takes two arguments, adds them, and returns the result.
It handles integers and floats, casting floats to integers.
"""


def add_integer(a, b=98):
    """
    Adds two values. If any input is a float, it is
    changed to an integer.

    Arguments:
    a -- First number (int or float)
    b -- Second number (int or float, default is 98)

    Returns:
    The sum of a and b as an integer.

    Raises:
    TypeError -- if a or b is neither an integer nor a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
