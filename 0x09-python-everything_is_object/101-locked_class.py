#!/usr/bin/python3
"""Module with no class or object attribute"""


class LockedClass:
    """Prevents creating new instance attributes dynamically"""
    __slots__ = ["first_name"]
