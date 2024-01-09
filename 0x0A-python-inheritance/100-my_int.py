#!/usr/bin/python3

"""Defines this is a new class and func"""


class MyInt(int):
    """Defines this is a new class and func"""

    def __eq__(self, value):
        """return the finally result ok"""

        return self.real != value

    def __ne__(self, value):
        """return the finally result ok"""

        return self.real == value
