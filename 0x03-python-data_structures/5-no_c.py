#!/usr/bin/python3

def no_c(my_string):
    book_n = my_string.translate({ord(i): None for i in 'cC'})
    return (book_n)
