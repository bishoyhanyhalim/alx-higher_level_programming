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

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
