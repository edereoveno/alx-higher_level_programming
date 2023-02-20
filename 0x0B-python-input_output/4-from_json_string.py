#!/usr/bin/python3
"""
Module with function that returns from its JSON representation
"""

import json


def from_json_string(my_str):
    """
        Function returns an object represented by JSON string
    """

    return json.loads(my_str)
