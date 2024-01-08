#!/usr/bin/python3

"""this si a func"""


def say_my_name(first_name, last_name=""):
    """func to print

    Args:
       the cool arg
    Raises:
        TypeError: ok this is raies error
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

