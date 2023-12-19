#!/usr/bin/python3

from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        hello = fct(*args)

    except Exception as book:
        print(f"Exception: {book}", file=sys.stderr)
        return (None)

    else:
        return (hello)
