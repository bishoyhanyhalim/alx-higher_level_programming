#!/usr/bin/python3

def best_score(a_dictionary):
    """
    for return the end value
    """

    if a_dictionary:

        my_list = list(a_dictionary.keys())

        leader = ""
        score = 0

        for i in my_list:

            if a_dictionary[i] > score:

                score = a_dictionary[i]
                leader = i

        return (leader)
