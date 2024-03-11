#!/usr/bin/python3

def element_at(my_list, idx):
    """Return my_list at the index specified by idx"""
    if idx < 0 or idx > len(my_list) - 1:
        return 'None'
    else:
        return my_list[idx]
