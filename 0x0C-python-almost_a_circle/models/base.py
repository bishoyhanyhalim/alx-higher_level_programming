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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return dictionaries to json file"""
        if (list_dictionaries is None) or (list_dictionaries is []):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        filename = cls.__name__ + ".json"

        with open(filename, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(list_dicts))
