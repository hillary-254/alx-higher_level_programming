#!/usr/bin/python3
def inherits_from(obj, a_class):
    """

    Args:
        obj: Object being checked
        a_class: class to compare against

    Returns:
        True if object is instance of a class inherited
        directly, false otherwise
    """
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
