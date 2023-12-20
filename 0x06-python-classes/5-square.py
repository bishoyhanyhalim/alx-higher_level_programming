#!/usr/bin/python3


"""this is a new class home"""


class Square:
    """this is a new class home"""

    def __init__(self, size):
        """this is a new class home

        Args:
           this is a size of class
        """
        self.size = size

    @property
    def size(self):
        """this is a self size"""

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

    def my_print(self):
        """finally return the result"""

        for i in range(0, self.__size):

            [print("#", end="") for j in range(self.__size)]
            print()

        if self.__size == 0:
            print()
