#!/usr/bin/python3
Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """the class inherits from rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        """validates size"""

        super().__init__(size, size)

    def area(self):
        """returns the area of the square"""
        return self._Rectangle__width ** 2
