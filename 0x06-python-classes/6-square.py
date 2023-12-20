#!/usr/bin/python3


"""this is a new class home"""


class Square:
    """this is a new class home"""

    def __init__(self, size=0, position=(0, 0)):
        """this is a new class home

        Args:
            this is a size of class
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """this is a size of class"""

        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):

            raise TypeError("size must be an integer")

        elif value < 0:

            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """this is a size of class"""

        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):

            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """finally return the result"""

        return (self.__size * self.__size)

    def my_print(self):
        """finally return the result"""

        if self.__size == 0:

            print("")
            return

        [print("") for i in range(0, self.__position[1])]

        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]

            [print("#", end="") for k in range(0, self.__size)]

            print("")
