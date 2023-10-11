#!/usr/bin/python3
"""Module for reading a file"""


def read_file(filename=""):
    """Function that read file's contents.

    Args:
        filename (str): file to be read.
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
