#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """Prints the argument list passed to the program

    The program takes all the arguments starting from the second
    and prints the number of arguments and their value

    """

    argc = len(sys.argv) - 1  # Subtracting 1 to exclude the script name

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print(f"{argc} arguments:")

    if argc > 0:
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
