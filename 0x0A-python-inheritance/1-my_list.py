#!/usr/bin/python3
"""Module presents MyList class"""


class MyList(list):
    """A class that inherits from 'list' object"""

    def print_sorted(self):
        """Function to print sorted copy of the initialized list"""

        sorted_list = sorted(self)
        print(sorted_list)
