#!/usr/bin/python3

"""
Module defines a function that checks the class of an object
"""


def is_kind_of_class(obj, a _class):
    """checks if object is instance of class of inherited class
    Args:
        obj: object checked
        a_class: Class to match the type of obj with
    Returns:
        return true if is instance, else false
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
