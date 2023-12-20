#!/usr/bin/python3


"""lets to do a class"""


class Square:

    """lets to do a class"""

    def __init__(self, size=0):
        """lets to do a class

        Args:
            this is an arg for size
        """

        self.size = size

    @property
    def size(self):
        """this is a data and size of class"""

        return (self.__size)

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """return the finally output value"""

        return (self.__size * self.__size)

    def __eq__(self, other):
        """return the finally output value"""

        return self.area() == other.area()

    def __ne__(self, other):
        """return the finally output value"""

        return self.area() != other.area()

    def __lt__(self, other):
        """return the finally output value"""

        return self.area() < other.area()

    def __le__(self, other):
        """return the finally output value"""

        return self.area() <= other.area()

    def __gt__(self, other):
        """return the finally output value"""

        return self.area() > other.area()

    def __ge__(self, other):
        """return the finally output value"""

        return self.area() >= other.area()
