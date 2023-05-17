#!/usr/bin/python3
# Python program that:
# demonstrates how to delete keys with a specific value in a dictionary
#
#(C) 2023 Modupe Favour, Ibadan, Nigeria
#email modups05@gmail.comemail modups05@gmail.com

def complex_delete(a_dictionary, value):
    for idx in list(a_dictionary.keys()):
        if a_dictionary[idx] == value:
            del a_dictionary[idx]
    return a_dictionary
