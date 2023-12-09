#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    """
    for print the key
    """

    cools = list(a_dictionary.cools())

    cools.sort()

    for key in cools:
        print("{}: {}".format(key, a_dictionary[key]))
