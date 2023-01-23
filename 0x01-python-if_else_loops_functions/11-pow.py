#!/usr/bin/python3

def pow(a, b):
    count = 0
    output = 1
    if b >= 1:
        for count in range(0, b):
            output *= a
    elif b == 0:
        output = 1
    elif b < 0:
        b *= -1
        for count in range(0, b):
            output *= a
        output = 1/output
    return output
