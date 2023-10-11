#!/usr/bin/python3
"""Module presents MyList class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represnts rectangle & inhereting from BaseGeometry class"""

    def __init__(self, width, height):
        """Initialization of Rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
