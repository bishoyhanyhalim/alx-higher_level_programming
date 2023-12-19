#!/usr/bin/python3

def magic_calculation(a, b):

    helloing = 0

    for num in range(1, 3):

        try:

            if num > a:
                raise Exception('Too far')

            helloing += a ** b / num

        except Exception:

            helloing = (b + a)

            break

    return (helloing)
