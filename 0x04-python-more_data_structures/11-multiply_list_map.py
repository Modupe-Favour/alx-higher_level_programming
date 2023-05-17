#!/usr/bin/python3
# Python program that:
# demonstrates how to return a list with all values multiplied by a number
# without using any loops
#
#(C) 2023 Modupe Favour, Ibadan, Nigeria
#email modups05@gmail.comemail modups05@gmail.com

def multiply_list_map(my_list=[], number=0):
    return (list(map((lambda i: i * number), my_list)))
