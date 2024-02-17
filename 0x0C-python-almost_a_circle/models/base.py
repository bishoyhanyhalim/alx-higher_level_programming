#!/usr/bin/python3
"""this is the base class for all project"""

import json


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

    def to_json_string(list_dictionaries):
        """ return dictionaries to json file"""
        if (list_dictionaries == None) or (list_dictionaries == []):
            return "[]"
        else:
            return json.dumps(list_dictionaries)
