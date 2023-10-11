#!/usr/bin/python3
"""Module Pascal trianlge"""


def pascal_triangle(n):
    """Initialization of Pascal triangle.

    Args:
        n (int): number of elements
    """
    if n <= 0:
        return []

    tr_lists = [[1]]

    while len(tr_lists) != n:
        tmp = [1]
        tr = tr_lists[-1]

        for i in range(len(tr) - 1):
            tmp.append(tr[i] + tr[i + 1])

        tmp.append(1)
        tr_lists.append(tmp)

    return tr_lists
