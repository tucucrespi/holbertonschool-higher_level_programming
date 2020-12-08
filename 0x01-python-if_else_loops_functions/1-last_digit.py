#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    LD = (number * -1) % 10
    if LD != 0:
        LD *= -1
else:
    LD = number % 10
if LD == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, LD))
elif LD < 6:
    print("Last digit of {:d} is".format(number), end=" ")
    print("{:d} and is less than 6 and not 0".format(LD))
if LD > 5:
    print("Last digit of {:d} is".format(number), end=" ")
    print("{:d} and is greater than 5".format(LD))
