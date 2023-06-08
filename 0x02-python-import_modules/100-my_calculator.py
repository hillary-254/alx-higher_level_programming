#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    arg_size = len(argv) - 1

    if arg_size != 4:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])

    if op == "+":
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
        exit(0)

    elif op == "-":
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
        exit(0)

    elif op == "*":
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
        exit(0)

    elif op == "/":
        print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
        exit(0)

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

else:
    print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    exit(1)
