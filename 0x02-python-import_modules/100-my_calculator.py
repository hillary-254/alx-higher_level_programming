#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("The argument list size might be too few or more")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    res = None
    if op == "+":
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
        sys.exit(0)

    elif op == "-":
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
        sys.exit(0)

    elif op == "*":
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
        sys.exit(0)

    elif op == "/":
        print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
        sys.exit(0)

    else:
        print("The operator is unknown")
        sys.exit(1)

    # print(f"{a} {op} {b} = {res}")
    # sys.exit(0)
