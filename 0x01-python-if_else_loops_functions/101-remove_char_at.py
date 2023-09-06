#!/usr/bin/python3
def remove_char_at(str, n):
    cpy_str = ""
    for i in range(len(str)):
        if i != n:
            cpy_str += str[i]
    return cpy_str
