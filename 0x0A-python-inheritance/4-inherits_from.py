#!/usr/bin/python3
"""module with method inherits_from"""


def inherits_from(obj, a_class):
    """

    Args:
        obj: Object being checked
        a_class: class to compare against

    Returns:
        True if object is instance of a class inherited
        directly, false otherwise
    """

    return False if type(obj) is a_class else isinstance(obj, a_class)
