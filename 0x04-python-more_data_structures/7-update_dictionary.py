#!/usr/bin/python3
# Python program that:
# demonstrates how to replace or add key/value in a dictionary
#
#(C) 2023 Modupe Favour, Ibadan, Nigeria
#email modups05@gmail.comemail modups05@gmail.com

def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for i in a_dictionary:
            if i == key:
                a_dictionary[i] = value
    return a_dictionary
