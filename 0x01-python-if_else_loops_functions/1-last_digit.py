#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lDigit = abs(number) % 10
if lDigit > 5:
    print(f"Last digit of {number} is {lDigit} and is greater than 5")
elif lDigit == 0:
    print(f"Last digit of {number} is {lDigit} and is 0")
elif lDigit < 6 and lDigit != 0:
    print(f"Last digit of {number} is {lDigit} and is less than 6 and not 0")
