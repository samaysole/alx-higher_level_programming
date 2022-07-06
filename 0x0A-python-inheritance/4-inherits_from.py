#!/usr/bin/python3
def inherits_from(obj, a_class) -> bool:
    """ Function that returns True/False if obj is an instance of a_class
    Args:
        obj: object
        a_class: class type
    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
