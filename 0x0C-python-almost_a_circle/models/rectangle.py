#!/usr/bin/python3
"""this is a rectangle class for project"""

from base import Base


class Rectangle(Base):

    """this is a rectangle class for project"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """this is a defined func

        Args:
            this is variable of ths class
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """set and get width"""
        return self.__width

    @width.setter
    def width(self, new_value):
        self.__width = new_value

    @property
    def height(self):
        """set and get height"""
        return self.__height

    @height.setter
    def height(self, new_value):
        self.__height = new_value

    @property
    def x(self):
        """set and get x"""
        return self.__x

    @x.setter
    def x(self, new_value):
        self.__x = new_value

    @property
    def y(self):
        """set and get y"""
        return self.__y

    @y.setter
    def y(self, new_value):
        self.__y = new_value
