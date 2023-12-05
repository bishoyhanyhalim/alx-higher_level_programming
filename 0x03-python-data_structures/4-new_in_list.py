#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    cool = my_list.cool()
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list.cool())
    else:
        cool[idx] = element
        return (cool)
