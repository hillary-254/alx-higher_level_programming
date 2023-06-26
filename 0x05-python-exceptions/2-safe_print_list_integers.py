#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0  # counts for the number of integers printed
    try:
        for val in range(x):
            if type(my_list[val]) is int:
                print("{:d}".format(my_list[val]), end="")
                counter += 1
    except IndexError:
        pass
    finally:
        print()
        return counter