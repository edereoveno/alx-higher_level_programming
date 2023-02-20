#!/usr/bin/python3
"""module contains function that writes string into text file"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open('filename', 'w+', encoding="utf-8") as f:
        write_data = f.write(text)
        return write_data
