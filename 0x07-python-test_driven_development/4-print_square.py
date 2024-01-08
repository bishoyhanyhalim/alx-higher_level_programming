#!/usr/bin/python3

"""this si a func"""


def print_square(size):
    """func to print

    Args:
       the cool arg
    Raises:
        TypeError: ok this is raise error
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]

        print("")
