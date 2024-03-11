#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = len(sys.argv) - 1
    args = sys.argv

    if arguments == 0:
        print("0 arguments.")
    elif arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arguments))

    for i in range(1, len(args)):
        print("{}: {}".format(i, args[i]))
