#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0  # counts the number of integers printed
    
    for val in range(x):
        try:
            if type(my_list[val]) is int:
                print("{:d}".format(my_list[val]), end="")
                counter += 1
        except TypeError:
            continue
        finally:
            print()
            return counter