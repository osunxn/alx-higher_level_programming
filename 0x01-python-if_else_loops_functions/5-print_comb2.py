#!/usr/bin/python3

# Print numbers from 0 to 99
for i in range(100):
    if i == 99:
        print("{:02d}".format(i))
    else:
        print("{:02d}".format(i), end=", ")
