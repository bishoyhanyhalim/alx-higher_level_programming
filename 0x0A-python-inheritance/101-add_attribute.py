#!/usr/bin/python3

"""return the finally result ok"""


def add_attribute(obj, att, value):
    """this  class so cool

    Args:
        this is an arg
    Raises:
        TypeError: wow errors
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, att, value)
