#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list"""
    return [True if i % 2 == 0 else False for i in my_list]
