#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers a and b. If a or b are floats, they are changed to integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
