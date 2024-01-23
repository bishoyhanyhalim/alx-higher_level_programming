#!/usr/bin/python3
"""object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """object to a text file"""
    with open(filename, "w") as book:
        json.dump(my_obj, book)
