#!/usr/bin/python3
"""this is function print text"""


def read_file(filename=""):
    """this is read file func
    """
    with open(filename, encoding="utf-8") as books:

        print(books.read())
