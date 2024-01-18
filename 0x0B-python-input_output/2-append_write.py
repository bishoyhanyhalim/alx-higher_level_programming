#!/usr/bin/python3
"""        this is print text file"""


def append_write(filename="", text=""):
    """ this is print text file

    Args:
        this is print text file

    Returns:
        return the text count finally
    """
    with open(filename, "a", encoding="utf-8") as text_file:

        return (text_file.write(text))
