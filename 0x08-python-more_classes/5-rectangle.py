#!/usr/bin/python3

"""this is a cool class"""


class Rectangle:
    """this is a cool class"""

    def __init__(self, width=0, height=0):
        """this is a cool class

        Args:
             this is an arg func
        """
        self.width = width

        self.height = height

    @property
    def width(self):
        """this is an step class getter"""

        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """this is an step class getter"""
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return finally value good"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Return finally value good"""

        if self.__width == 0 or self.__height == 0:
            return (0)

        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return finally value good"""

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []

        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]

            if i != self.__height - 1:
                rect.append("\n")

        return ("".join(rect))

    def __repr__(self):
        """Return finally value good"""

        rect = "Rectangle(" + str(self.__width)

        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """print the finally value good"""

        print("Bye rectangle...")
