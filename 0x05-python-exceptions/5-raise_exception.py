#!/usr/bin/python3

def raise_exception():
    name = 21
    if type(name) is not str:
        raise TypeError("Not a string")
