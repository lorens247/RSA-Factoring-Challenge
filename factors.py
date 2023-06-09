#!/usr/bin/python3
"""
factorize given set of numbers in a file to product of two numbers
"""
from sys import argv


def factorize(number):
    """"find two small numbers that multiply to give a given number"""
    i = 2

    if number < 2:
        return
    while number % i:
        i += 1
    print("{:.0f}={:.0f}*{:.0f}".format(number, number / i, i))


if len(argv) != 2:
    exit()

try:
    with open(argv[1]) as file:
        line = file.readline()

        while line != "":
            number = int(line.split('\n')[0])
            factorize(number)
            line = file.readline()
except ValueError:
    pass
