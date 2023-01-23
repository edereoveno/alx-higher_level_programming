#!/usr/bin/python3

def uppercase(str):
    output = ''
    for character in str:
        if ord(character) in range(97, 123):
            output += chr(ord(character) - 32)
        else:
            output += character
    print("{}".format(output))
