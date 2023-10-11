#!/usr/bin/python3
"""Module presents MyList class"""


class MyList(list):
    """A class that inherits from 'list' object"""

    def __init__(self):
        """Initialization of MyList class"""

        self.__o_list = self

    def print_sorted(self):
        """Function to print sorted copy of the initialized list"""

        sorted_list = sorted(self.__o_list)
        print(sorted_list)
