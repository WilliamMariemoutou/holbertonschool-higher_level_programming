#!/usr/bin/python3
"""the base geometry class """


class BaseGeometry:
    """the class with are and integer_validation"""

    def area(self):
        raise Exception("area() is not implemented")
    """raise exception if area is not implemented"""

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        """return typeerror is value is not an integer"""
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        """return value error is value is not greater than 0"""


"""the class rectangle"""


class Rectangle(BaseGeometry):
    """the class inherits from basegeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        """validates width and height"""

        self.__width = width
        self.__height = height
        """calls child and parent method"""

    def area(self):
        """claculate the area of the rectangle
        Returns: area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Shows the string representation of the rectangle
        Returns a string with the format [Rectangle] <width>/<height>"""
        return f"[Rectangle] {self.__width}/{self.__height}"
    
class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        
        super().__init__(size, size)
        
    def __str__(self):
        return f"[Rectangle] {self._Rectangle__width}/{self._Rectangle__height}"
        
    def area(self):
        return self._Rectangle__width ** 2
