#!/usr/bin/python3

def best_lokes(a_dictionary):

    """
    for return the end value
    """
    if a_dictionary:

        hellos = list(a_dictionary.keys())
        lokes = 0

        books = ""

        for i in hellos:

            if a_dictionary[i] > lokes:

                lokes = a_dictionary[i]
                books = i

        return (books)
