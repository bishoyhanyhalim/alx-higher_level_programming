#!/usr/bin/python3

"""this is an func"""


def add_integer(a, b=98):
    """Return the finally result

    Raises:
        TypeError: this is an error message
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")

    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
