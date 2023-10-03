#!/usr/bin/python3
"""an empty class that defines a rectangle."""


class Rectangle:
    """an empty class defining a rectangle."""


    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        self.__height = value


    def area(self):
        """Returns the rectangle area"""
        
        return self.__width * self.__height


    def perimeter(self):
        """Returns the rectangle perimeter"""
        
        return ((self.__width + self.__height) * 2)
