#!/usr/bin/python3
"""Task 6. Find a peak"""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers

    Args:
        list_of_integers (list): a list of integers
    """
    if (list_of_integers):
        if len(list_of_integers) < 3:
            return None
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
