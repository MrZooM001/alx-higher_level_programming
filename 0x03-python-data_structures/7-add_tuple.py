#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        tup_a0 = tuple_a[0]
        tup_a1 = 0
        tuple_a = (tup_a0, tup_a1)
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tup_b0 = tuple_b[0]
        tup_b1 = 0
        tuple_b = (tup_b0, tup_b1)
    tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple_c
