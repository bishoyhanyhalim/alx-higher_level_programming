#!/usr/bin/python3
"""this is the base class for all project"""
import json
import csv


class Base:
    """now this is the class cold base"""
    __no_object_yet = 0

    def __init__(self, id=None):
        """func ths base class"""

        if id is not None:
            self.id = id
        else:
            Base.__no_object_yet += 1
            self.id = Base.__no_object_yet

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

    @staticmethod
    def from_json_string(json_string):
        """return json file to dictionaries"""
        if (json_string is None) or (json_string is "[]"):
            return []
        else:
            return json.loads(json_string)

# #######do_nothing########
    @classmethod
    def create(cls, **dictionary):
        """return the create"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                add_new = cls(1, 1)
            else:
                add_new = cls(1)
            add_new.update(**dictionary)
            return add_new

    @classmethod
    def load_from_file(cls):
        """Return load file"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as to_json_file:
                list_dicts = Base.from_json_string(to_json_file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as to_csv_file:
            if list_objs is None or list_objs == []:
                to_csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(to_csv_file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return load_from_file_csv
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as to_csv_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(to_csv_file, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
