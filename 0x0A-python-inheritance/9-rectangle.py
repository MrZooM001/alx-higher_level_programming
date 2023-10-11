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

    def area(self):
        """Function to get the area"""
        return self.__width * self.__height

    def __str__(self):
        """represent print() & str() output of Rectangle class"""
        output = "[{}] {}/{}".format(str(self.__class__.__name__),
                                     str(self.__width), str(self.__height))
        return output
