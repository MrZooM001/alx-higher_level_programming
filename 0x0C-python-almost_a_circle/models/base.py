#!/usr/bin/python3
"""Module to define a base class"""
import json
import csv


class Base:
    """Class to represent a Base model for all classes

    Attributes:
        __nb_objects (int): Count created instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Method to initialize a new instance of Base class

        Args:
            id (int): id of the instantiated instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that return the JSON string representation
        of 'list_dictionaries'

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string representation
        of 'list_objs' to a file

        Args:
            list_objs (list): list of instances who inherits of Base class
            cls (class): class object
        """
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, 'w', encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [j.to_dictionary() for j in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list
        of the JSON string representation json_string

        Args:
            json_string (str): a string representing a list of dictionaries
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method that writes the JSON string representation
        of 'list_objs' to a file

        Args:
            cls (class): class object
            dictionary (dict): dictionary of dictionaries
            containing all the attributes of cls
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                dummy = cls(2)
            else:
                dummy = cls(2, 2)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """class method that returns a list of instances of cls object

        Args:
            cls (class): class object
        """
        json_file = "{}.json".format(str(cls.__name__))
        try:
            with open(json_file, "r", encoding="utf-8") as file:
                list_insta = Base.from_json_string(file.read())
                return [cls.create(**ls) for ls in list_insta]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """class method that serializes (save) to a CSV file

        Args:
            cls (class): class object
            list_objs (list): list of objects to be saved in a csv file
        """
        file_name = "{}.csv".format(str(cls.__name__))
        with open(file_name, 'w', newline="", encoding="utf-8") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]

                csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
                [csv_writer.writerow(obj.to_dictionary()) for obj in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        """class method that deserializes (load) from a CSV file

        Args:
            cls (class): class object
        """
        file_name = "{}.csv".format(str(cls.__name__))
        try:
            with open(file_name, 'r', newline="", encoding="utf-8") as csv_f:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]

                csv_reader = csv.DictReader(csv_f, fieldnames=field_names)
                new_reader = []
                for dictionary in csv_reader:
                    new_dictionary = {}
                    for key, value in dictionary.items():
                        new_dictionary[key] = int(value)
                    new_reader.append(new_dictionary)
                csv_reader = new_reader
                return [cls.create(**obj) for obj in csv_reader]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """static method that opens a window
        and draws all the Rectangles and Squares

        Args:
            list_rectangles (class): class object
            list_squares (class): class object
        """
        turtle.Screen().setup(1280, 720, startx=60, starty=60)
        colors = ['#F44336', '#E91E63', '#3F51B5', '#009688', '#C0CA33',
                  '#FBC02D', '#F4511E', '#673AB7', '#607D8B']
        for rect in list_rectangles:
            turtle.penup()
            if rect.x is not None or rect.y is not None:
                turtle.goto(rect.y, rect.x)
            turtle.pendown()
            turtle.color(random.sample(colors, 1))
            turtle.pensize(1.5)
            turtle.showturtle()
            turtle.begin_fill()
            for i in range(2):
                if i == 0:
                    turtle.penup()
                    turtle.forward(144)
                    turtle.pendown()
                turtle.left(-90)
                turtle.shape("circle")
                turtle.forward(rect.width)
                turtle.left(-90)
                turtle.shape("triangle")
                turtle.forward(rect.height)
            turtle.end_fill()
            turtle.hideturtle()
            turtle.penup()
            turtle.left(120)
            turtle.forward(60)
            turtle.pendown()
        for squar in list_squares:
            turtle.penup()
            if squar.x is not None or squar.y is not None:
                turtle.goto(squar.y, squar.x)
            turtle.pendown()
            turtle.color(random.sample(colors, 1))
            turtle.pensize(1.5)
            turtle.showturtle()
            turtle.begin_fill()
            for i in range(2):
                if i == 0:
                    turtle.penup()
                    turtle.forward(-144)
                    turtle.pendown()
                turtle.left(-90)
                turtle.shape("square")
                turtle.forward(squar.width)
                turtle.left(-90)
                turtle.shape("turtle")
                turtle.forward(squar.height)
            turtle.end_fill()
            turtle.hideturtle()
            turtle.penup()
            turtle.left(-90)
            turtle.forward(-90)
            turtle.pendown()
        turtle.exitonclick()
