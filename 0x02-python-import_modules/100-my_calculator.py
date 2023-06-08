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
        res = add(a, b)
    elif op == "-":
        res = sub(a, b)
    elif op == "*":
        res = mul(a, b)
    elif op == "/":
        res = div(a, b)
    else:
        print("The operator is unknown")
        sys.exit(1)

    print(f"{a} {op} {b} = {res}")
    sys.exit(0)
