#!/usr/bin/python3
"""Module presents Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represnts Square & inhereting from Rectangle class"""

    def __init__(self, size):
        """Initialization of Square class

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Get the area of the square"""
        sqr_area = self.__size ** 2
        return sqr_area
