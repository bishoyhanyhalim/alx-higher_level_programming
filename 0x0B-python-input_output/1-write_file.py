#!/usr/bin/python3
""" this func to print the text count"""


def write_file(filename="", text=""):
    """this func to print the text count

    Args:
        this func to print the text count args
    """

    with open(filename, "w", encoding="utf-8") as text_file:

        return(text_file.write(text))
