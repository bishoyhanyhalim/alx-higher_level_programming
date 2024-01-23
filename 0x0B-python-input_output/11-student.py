#!/usr/bin/python3

"""let have a class Student."""


class Student:
    """this is an a student."""

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

    def reload_from_json(self, json):
        """this is a func

        Args:
            of the student now
        """
        for k, v in json.items():
            setattr(self, k, v)
