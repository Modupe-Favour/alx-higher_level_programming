#!/usr/bin/python3
# 0-print_list_integer.py


def my_list_of_integers(my_list=[]):
    """Print all integers of a list."""
    for n in range(len(my_list)):
        print("{:d}".format(my_list[n]))
