#!/usr/bin/python3
import sys

# Function description:
# The factorial function calculates the factorial of a given number 'n' using recursion.
# Factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n.
# For example, 5! = 5 * 4 * 3 * 2 * 1 = 120, and 0! = 1 by definition.

# Parameters:
# n (int): The number for which the factorial is to be calculated.
# It is expected to be a non-negative integer (n >= 0).

# Returns:
# int: The factorial of the input number 'n'. 
# If n == 0, the function returns 1, since 0! is defined as 1.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the input number from command-line arguments and calculate its factorial.
# sys.argv[1] is used to get the argument passed when the script is executed.
f = factorial(int(sys.argv[1]))

# Print the result (factorial of the number passed as input).
print(f)
