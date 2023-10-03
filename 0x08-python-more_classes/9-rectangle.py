#!/usr/bin/python3
"""Module that defines a rectangle."""


class Rectangle:
    """Class that represents a rectangle.

    Args:
        number_of_instances (int): number of instantiated instances
        print_symbol (any): symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiate a new rectangle with default values of 0

        Args:
            width (int): rectangle's width
            height (int): rectangle's height
        """
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
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieve rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle's area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Return the printable representation of the Rectangle as #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_symbol = []
        for i in range(self.__height):
            [rect_symbol.append(str(self.print_symbol))
             for j in range(self.__width)]
            if i != (self.__height - 1):
                rect_symbol.append('\n')
        return "".join(rect_symbol)

    def __repr__(self):
        """Return a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        r = "{}({}, {})".format(self.__class__.__name__,
                                self.width, self.height)
        return (r)

    def __del__(self):
        """Return a message when an instance of a class is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area

        Args:
            rect_1 (object): an instance of Rectangle class
            rect_2 (object): an instance of Rectangle class
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size

        Args:
            size (int): represents the Width & Height of the Rectangle
        """
        return cls(size, size)
