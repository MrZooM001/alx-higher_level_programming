#!/usr/bin/python3
for i in range(90, 64, -1):
    if i % 2 == 0:
        asci = 32
    else:
        asci = 0
    print("{}".format(chr(i + asci)), end="")
