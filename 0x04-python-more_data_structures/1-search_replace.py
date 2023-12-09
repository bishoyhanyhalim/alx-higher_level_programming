#!/usr/bin/python3

def search_replace(my_list, search, replace):

    looks = []

    for element in my_list:
        if element == search:
            looks.append(replace)

        else:
            looks.append(element)

    return (looks)
