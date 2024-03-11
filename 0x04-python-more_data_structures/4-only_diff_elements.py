#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Write a function that returns a
    set of all elements present in only one set.
    this is a short solution return '(set_1 ^ set_2)'
    """

    rset = set()

    for i in set_1:
        if i not in set_2:
            rset.add(i)

    for j in set_2:
        if j not in set_1:
            rset.add(j)

    return rset
