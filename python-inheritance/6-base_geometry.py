#!/usr/bin/python3
"""the class base geometry"""


class BaseGeometry:
    """the area being defined"""
    def area(self):
        """exception will be raised if the area is not implemented"""
        raise Exception("area() is not implemented")
