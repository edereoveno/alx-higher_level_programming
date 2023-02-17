#!/usr/bin/poython3
"""Defines a class and inherited class-checking function."""


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
