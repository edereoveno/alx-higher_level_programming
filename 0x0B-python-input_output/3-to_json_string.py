#!/usr/bin/python3
"""module with function that return the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """returns JSON representation of object(string)"""
    return json.dumps(my_obj)
