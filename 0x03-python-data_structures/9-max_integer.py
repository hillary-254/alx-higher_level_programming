#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        valMax = my_list[0]
        for num in my_list:
            if num > valMax:
                valMax = num

    return valMax
