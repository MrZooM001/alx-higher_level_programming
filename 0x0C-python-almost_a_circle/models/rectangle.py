#!/usr/bin/python3
"""Module to define a base class"""
from models.base import Base


class Rectangle(Base):
    """Class to represent a Rectangle model with inheritance from Base class

    Attributes:
        print_symbol (str): character that used by display()
        to represent a Rectangle.
    """

    print_symbol = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new instance of Rectangle class

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x axis of rectangle
            y (int): y axis of rectangle
        """
        super().__init__(id)
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """Retrieve rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle's width

        Args:
            value (int): value passed to set as new width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set rectangle's height

        Args:
            value (int): value passed to set as new height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieve rectangle's x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set rectangle's x

        Args:
            value (int): value passed to set as new x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve rectangle's y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set rectangle's y

        Args:
            value (int): value passed to set as new y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the rectangle's area"""
        return self.__width * self.__height

    def display(self):
        """Print in stdout the Rectangle instance with character '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_symbol = []
        for k in range(self.y):
            print("")
        for i in range(self.__height):
            [rect_symbol.append(" ") for j in range(self.__x)]
            [rect_symbol.append(str(self.print_symbol))
             for j in range(self.__width)]
            if i != (self.__height - 1):
                rect_symbol.append("\n")
        print("".join(rect_symbol))

    def __str__(self):
        """Return a formated printable representation of the Rectangle"""
        result = "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id,
            self.x, self.y, self.width, self.height)
        return result

    def update(self, *args, **kwargs):
        """Update the class by assigning an argument to each attribute

        Args:
            args (tuple): unknown arguments count
            kwargs (dict): keyworded arguments with unknown count.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle"""
        rectangle_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return rectangle_dict
