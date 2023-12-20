#!/usr/bin/python3


"""this is a new class book"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """this is a new class book

        Args:
            ok this is a size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """this is a new class book"""

        return (self.__size * self.__size)
