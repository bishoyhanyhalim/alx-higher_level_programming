#!/usr/bin/python3

def weight_average(my_list=[]):

    if not my_list:
        return (0)

    soons = 0

    home = 0

    for tup in my_list:

        home += tup[0] * tup[1]
        soons += tup[1]

    return (home / soons)
