#!/usr/bin/python3
"""object to a text file"""
import json


def load_from_json_file(filename):
    """this is object to a text file"""
    with open(filename) as files:
        return json.load(files)
