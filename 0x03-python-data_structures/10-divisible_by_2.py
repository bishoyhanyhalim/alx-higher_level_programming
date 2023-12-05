#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    what_my = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            what_my.append(True)
        else:
            what_my.append(False)
    return (what_my)
