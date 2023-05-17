#!/usr/bin/python3
# Python program that:
# demonstrates how to return a new dictionary with all values multiplied by 2
#
#(C) 2023 Modupe Favour, Ibadan, Nigeria
#email modups05@gmail.comemail modups05@gmail.com

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key, value in new_dict.items():
        new_dict[key] = value * 2
    return new_dict
