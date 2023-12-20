#!/usr/bin/python3


"""this task to defined list good"""


class Square:

    """this task to defined list good"""

    def __init__(self, size=0, position=(0, 0)):
        """this task to defined list good

        Args:
            this is an arg for func
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """this is a data and size of class"""

        return (self.__position)

    @position.setter
    def position(self, value):

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """this is a data and size of class"""

        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]

        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def area(self):
        """this task to defined list good"""

        return (self.__size * self.__size)

    def __str__(self):
        """this is a data and size of class"""

        if self.__size != 0:

            [print("") for i in range(0, self.__position[1])]

        for i in range(0, self.__size):

            [print(" ", end="") for j in range(0, self.__position[0])]

            [print("#", end="") for k in range(0, self.__size)]

            if i != self.__size - 1:
                print("")

        return ("")
