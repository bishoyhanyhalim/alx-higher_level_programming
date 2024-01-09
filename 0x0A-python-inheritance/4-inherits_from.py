#!/usr/bin/python3

"""this is a new class and func"""


def inherits_from(obj, a_class):
    """return the finally result ok

    Args:
        this is an arf
    Returns:
        return the finally result ok

    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)

    return (False)
