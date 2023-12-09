#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    locks = list(a_dictionary.keys())

    for goods in locks:

        if value == a_dictionary.get(goods):
            del a_dictionary[goods]

    return (a_dictionary)
