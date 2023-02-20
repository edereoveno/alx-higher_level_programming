#!/usr/bin/python3
"""module with function that returns from its JSON representation"""
import json


def to_json_string(my_obj):
    """returns an object represented by JSON string"""
    return json.loads(my_obj)
