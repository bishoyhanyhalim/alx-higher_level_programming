#!/usr/bin/python3
"""this is a new class and func"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this is a new class and func"""

    def __init__(self, size):
        """return the finally result ok

        Args:
            this is an arf
        """

        self.integer_validator("size", size)

        super().__init__(size, size)
        self.__size = size
