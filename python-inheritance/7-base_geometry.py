#!/usr/bin/python3
"""the class basegeometry"""


class BaseGeometry:
    """the class with are and integer_validation"""

    def area(self):
        raise Exception("area()is not implemented")
    """raise exception if area is not implemented"""

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        """return typeerror is value is not an integer"""
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        """return value error is value is not greater than 0"""
