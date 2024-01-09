#!/usr/bin/python3

"""this is a new class and func"""


class BaseGeometry:
    """this is a new class and func"""

    def area(self):
        """this is a new class and func"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this is a new class and func

        Args:
            name (str): this si an str name
            value (int): this is an vlaue
        Raises:
            TypeError: this is an error
            ValueError: this is an error
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
