#!/usr/bin/python3
def print_last_digit(number):
    lst_dgt = abs(number) % 10
    if number < 0:
        lst_dgt = -lst_dgt
    print("{:d}".format(lst_dgt), end="")
    return lst_dgt

