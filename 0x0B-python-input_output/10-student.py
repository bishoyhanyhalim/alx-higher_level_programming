#!/usr/bin/python3

"""Defines this is a func"""


class Student:
    """this is a func"""

    def __init__(self, first_name, last_name, age):
        """this is a func

        Args:
            of the student now
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """this is a func

        Args:
            of the student now
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):

            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return self.__dict__
