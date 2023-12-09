#!/usr/bin/python3

def new_look(form_n):

    suns = 0
    fully_l = max(form_n)

    for n in form_n:

        if fully_l > n:
            suns += n

    return (fully_l - suns)


def roman_to_int(roman_string):

    if not roman_string:

        return 0

    if not isinstance(roman_string, str):

        return 0

    homes = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    cools = list(homes.keys())

    valuse = 0
    form_ro = 0
    form_n = [0]

    for ch in roman_string:

        for r_num in cools:
            if r_num == ch:

                if homes.get(ch) <= form_ro:
                    valuse += new_look(form_n)
                    form_n = [homes.get(ch)]

                else:
                    form_n.append(homes.get(ch))

                form_ro = homes.get(ch)

    valuse += new_look(form_n)

    return (valuse)
