#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def reversed_list(my_list=[]):
    """Print all integers of a list in reverse order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for n in my_list:
            print("{:d}".format(n))
