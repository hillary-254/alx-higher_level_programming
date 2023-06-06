#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str

    result = ""
    for x in range(len(str)):
        if x != n:
            result += str[x]
    return result
