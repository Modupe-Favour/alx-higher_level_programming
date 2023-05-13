#!/usr/bin/python3
# 1-element_at.py


def retrieve_my_element(my_list, num):
    """Retrive an element from a list."""
    if num < 0 or num > (len(my_list) - 1):
        return None
    return (my_list[num])
