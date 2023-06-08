#!/usr/bin/python3
import sys

if __name__ == '__main__':
    arguments = sys.argv[1:]  # Get all arguments except the script name
    res = 0

    for arg in arguments:
        res += int(arg)

    print(res)
