#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_newList = []
    for num in my_list:
        if num % 2 == 0:
            my_newList.append(True)
        else:
            my_newList.append(False)

    return my_newList
