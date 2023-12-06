#!/usr/bin/python3

def uppercase(str):
    for s in range(len(str)):
        c = ord(str[s])
        if c in range(97, 123):
            c = c - 32
        print("{}".format(chr(c)), end="")


    print()
