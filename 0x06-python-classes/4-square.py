#!/usr/bin/python3


"""this is a new class book"""


class Square:

    """this is a new class book"""

    def __init__(self, size=0):
        """this is a new class book

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """this is self func"""

        return (self.__size)

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """finally return the result"""

        return (self.__size * self.__size)
