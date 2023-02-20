#!/usr/bin/python3
"""
Module with function that write json representation of an object to text file
"""
import json


def save_to_json(my_obj, filename):
    with open(filename, "w", encoding='utf-8') as file:
        file.write(json.dumps(file))
