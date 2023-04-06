#!/usr/bin/python3
import sys

# Define a function to factorize a given number into two smaller numbers
def factorize(num):
    # Loop from 2 to the square root of the number (inclusive)
    for i in range(2, int(num ** 0.5) + 1):
        # If i is a factor of the number, return i and the quotient of num and i
        if num % i == 0:
            return i, num // i
    # If no factors are found, return None for both factors
    return None, None

# Get the filename from the command-line arguments
filename = sys.argv[1]

# Open the file and iterate over its lines
with open(filename, 'r') as f:
    for line in f:
        # Parse the line as an integer
        num = int(line.strip())
        # Factorize the number
        p, q = factorize(num)
        # Print the factorization in the required format
        print(f"{num}={p}*{q}")
