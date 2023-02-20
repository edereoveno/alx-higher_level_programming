#!/usr/bin/python3
"""module with function that appends string to txt file"""


def append_write(filename="", text=""):
    """appends string to file"""
    with open(filename, "a", encoding="utf-8") as f:
        append_data = f.write(text)
        return append_data
