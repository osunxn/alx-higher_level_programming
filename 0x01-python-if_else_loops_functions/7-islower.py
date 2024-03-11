#!/usr/bin/python3
def islower(c):
    """Checks if the given character is lowercase"""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
# This can also be done using the char directly c >= 'a' and c <= 'z':
