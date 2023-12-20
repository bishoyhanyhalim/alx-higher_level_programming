#!/usr/bin/python3


"""this is the new class that do magic things"""


import math


class MagicClass:

    """a new task called magic"""

    def __init__(self, radius=0):
        """this is a self and radius

        Arg:
            this is the new class that do magic things
        """

        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:

            raise TypeError("radius must be a number")

        self.__radius = radius

    def circumference(self):
        """get the finally result of value"""

        return (2 * math.pi * self.__radius)

    def area(self):
        """get the finally result of value"""

        return (self.__radius ** 2 * math.pi)
