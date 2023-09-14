#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for _, v in a_dictionary.items():
        new_dict[_] = v * 2
    return (new_dict)
