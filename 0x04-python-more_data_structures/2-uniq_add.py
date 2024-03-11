#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).
    """

    unique_sum = 0
    new_list = []

    for num in my_list:
        if num not in new_list:
            unique_sum += num
            new_list.append(num)

    return unique_sum
