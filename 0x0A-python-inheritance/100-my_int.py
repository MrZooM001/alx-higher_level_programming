#!/usr/bin/python3
"""Module presents a class"""


class MyInt(int):
    """A class that inherits from int"""

    def __eq__(self, __value):
        """Check for equality"""
        return self.real != __value

    def __ne__(self, __value):
        """Check for not inequality"""
        return self.real == __value
