#!/usr/bin/python3
"""Module presents MyList class"""


class BaseGeometry():
    """A class that represented as base class"""

    def __init__(self) -> None:
        """Initialization of BaseGeometry class"""
        pass

    def area(self):
        """Function to get the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validate value's type

        Args:
            name (str): name of the object
            value (int): value of the object, it should be > 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
