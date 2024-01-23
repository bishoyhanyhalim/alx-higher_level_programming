#!/usr/bin/python3
"""the func to name and age"""


class Student:
    """the func to name and age"""

    def __init__(self, first_name, last_name, age):
        """the func to name and age

        Args:
            this is and arg
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """this is a json"""
        return self.__dict__
