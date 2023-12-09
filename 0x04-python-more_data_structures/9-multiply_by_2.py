#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    moons = {}

    for key, value in a_dictionary.items():
        moons.update({key: (value * 2)})

    return (moons)
