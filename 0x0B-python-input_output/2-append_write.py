#!/usr/bin/python3
"""module with function that appends string to txt file"""


def append_write(filename="", text=""):
    """appends string to file"""
    with open (filename, "w", encoding="utf-8") as f:
        f.write(text)
