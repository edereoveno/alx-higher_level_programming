#!/usr/bin/python3
"""
Module with function that write json representation of an object to text file
"""
import json


def save_to_json_file(my_obj, filename):
    ""
        "write an object to text ile using json representation
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
