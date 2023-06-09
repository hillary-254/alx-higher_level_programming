#!/usr/bin/python3
def no_c(my_string):
    str_new = ''
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            str_new += ch
    return str_new
