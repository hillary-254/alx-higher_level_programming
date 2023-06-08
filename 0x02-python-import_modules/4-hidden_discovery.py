#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    name = dir(hidden_4)
    x = 0

    while x < len(name):
        if not name[x].startswith('__'):
            print(name[x])
        x += 1
