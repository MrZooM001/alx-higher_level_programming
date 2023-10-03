#!/usr/bin/python3
"""Module with no class or object attribute"""


class LockedClass:
    """Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name"""

    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError()
