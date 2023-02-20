#!/usr/bin/python3
"""module converts JSON string to data structure"""
import JSON


def from_json_strung(my_str):
     """returns python data structure represented by JSON string"""
    return json.loads(my_str)
