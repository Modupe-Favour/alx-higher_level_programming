#!/usr/bin/python3
# 4-new_in_list.py


def new_item_in_list(my_list, num1, num2):
    """Replace an element in a copied list at a specific position."""
    if num1 < 0 or num2 > (len(my_list) - 1):
        return (my_list)

    copy = [x for x in my_list]
    copy[num1] = num2
    return (copy)
