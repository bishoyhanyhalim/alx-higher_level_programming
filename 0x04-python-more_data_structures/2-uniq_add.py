#!/usr/bin/python3

def uniq_add(my_list=[]):

    gos = []
    sum = 0

    for num in my_list:

        if num not in gos:

            sum += num
            gos.append(num)
    return (sum)
