#!/usr/bin/python3
"""this is a new class and func"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this is a new class and func"""

    def __init__(self, width, height):
        """return the finally result ok

        Args:
            this is an arg

        """

        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """return the finally result ok"""

        return self.__width * self.__height

    def __str__(self):
        """return the finally result ok"""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
