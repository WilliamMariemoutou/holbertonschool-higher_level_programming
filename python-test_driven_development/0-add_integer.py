#!/usr/bin/python3
"""
Module to add two integers.

This module contains the function `add_integer` which adds two integers or floats,
and returns the result as an integer. If the input values are not integers or floats,
it raises a TypeError with a specific error message.
"""

def add_integer(a, b=98):
    """
    Adds two integers (or floats) and returns the sum as an integer.

    Parameters:
    a (int or float): The first number.
    b (int or float, optional): The second number (default is 98).

    Returns:
    int: The sum of a and b, cast to an integer.

    Raises:
    TypeError: If either a or b are not integers or floats.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
