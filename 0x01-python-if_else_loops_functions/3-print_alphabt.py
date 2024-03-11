#!/usr/bin/python3

# Print the ASCII alphabet in lowercase except e and q
for char in range(97, 123):
    if chr(char) not in ['q', 'e']:
        print("{}".format(chr(char)), end="")
