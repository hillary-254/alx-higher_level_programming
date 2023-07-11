#!/usr/bin/python3
"""module with method is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    Checks if `obj` is same class or inherit from `a_class`

    Args:
        obj (any): The object to compare
        a_class (any): The class to compare with the object

    Returns:
        `True` if the object is an instance or inherit from the
        specified class; otherwise `False`
    """

    return isinstance(obj, a_class)
