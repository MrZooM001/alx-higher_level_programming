#!/usr/bin/python3
"""Module that read a file.

This supplies one function, read_file().
"""


def read_file(filename=""):
    """Function that read file's contents.

    Args:
        filename (str): file to be read.

    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
