#!/usr/bin/python3
"""module that contains function, read_file"""


def read_file(filename=""):
    """reads file and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
