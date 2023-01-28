#!/usr/bin/python3

def remove_char_at(str, n):
    new_string = ""
    for char in str:
        if str.index(char) is n:
            continue
        else:
            new_string += char
    return new_string
