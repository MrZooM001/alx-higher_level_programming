#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            asci = 32
        elif ord(c) < 91 or ord(c) > 122:
            asci = 0
        print("{:c}".format(ord(c) - asci), end="")
    print()
