#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers (or floats). If any input is a float, it is cast to an integer.

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
