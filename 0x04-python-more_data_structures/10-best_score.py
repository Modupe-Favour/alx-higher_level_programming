#!/usr/bin/python3
# Python program that:
# demonstrates how to return a key with the biggest integer value
#
#(C) 2023 Modupe Favour, Ibadan, Nigeria
#email modups05@gmail.comemail modups05@gmail.com

def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key=a_dictionary.get))
