#!/usr/bin/python3
# Python program that:
# demonstrates how to compute the square value of all integers of a matrix
# using map
#
#(C) 2023 Modupe Favour, Ibadan, Nigeria
#email modups05@gmail.comemail modups05@gmail.com

def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda i: i ** 2, x)), matrix))
