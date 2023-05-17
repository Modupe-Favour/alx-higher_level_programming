#!/usr/bin/python3
# Python program that:
# demonstrates how to delete a key in a dictionary
#
#(C) 2023 Modupe Favour, Ibadan, Nigeria
#email modups05@gmail.comemail modups05@gmail.com

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
