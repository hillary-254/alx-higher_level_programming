#!/usr/bin/python3
"""module with method is_same_class"""


def is_same_class(obj, a_class):
    """
    Checks if `obj` is exactly an instance of the specified class

    Args:
        obj (any): The object to compare
        a_class (any): The class to compare with the object

    Returns:
        `True` if object is exactly an instance of 
        specified class otherwise `False`
    """

    return type(obj) is a_class
