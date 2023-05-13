#!/usr/bin/python3
# 2-replace_in_list.py


def replace_element(my_list, num1, num2):
    """Replace an element of a list at a specific position."""
    if num1 >= 0 and num1 < len(my_list):
        my_list[num1] = num2
    return (my_list)
