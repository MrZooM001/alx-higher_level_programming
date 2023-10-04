#!/usr/bin/python3
"""Module with no class or object attribute"""


__slots__ = ["first_name"]


class LockedClass:
    """Prevents creating new instance attributes dynamically"""
    def __setattr__(self, name, value):
        """Only set when attribute's name == firt_name"""
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("'{}' object has no attribute '{}'"
                                 .format(type(self).__name__, name))
