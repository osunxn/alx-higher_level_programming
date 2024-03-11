#!/usr/bin/python3

# Print the ASCII alphabet in lowercase without a new line
# The letters can also be used "char in range(ord('a'), ord('z') + 1)"
for char in range(97, 123):
    print("{}".format(chr(char)), end="")
