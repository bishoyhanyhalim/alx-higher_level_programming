#!/usr/bin/python3

def multiple_returns(sentence):
    hellos = ()
    if len(sentence) == 0:
        hellos = 0, "None"
    else:
        hellos = len(sentence), sentence[0]
    return (hellos)
