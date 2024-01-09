#!/usr/bin/python3
"""this is a new class and func"""


class BaseGeometry:
    """this  class so cool"""

    def area(self):
        """this  class so cool"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """return the finally result ok

        Args:
            this is an arf
        Returns:
            return the finally result ok

        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
