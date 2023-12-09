#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    """
    now this taks return this dictionary
    """

    if key in a_dictionary:
        del a_dictionary[key]

    return (a_dictionary)
