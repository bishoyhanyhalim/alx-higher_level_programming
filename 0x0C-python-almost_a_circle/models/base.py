#!/usr/bin/python3
"""this is the base class for all project"""


class Base:
    """now this is the class cold base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """func ths base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
