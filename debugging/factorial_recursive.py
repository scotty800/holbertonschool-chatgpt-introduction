#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given integer using recursion.

    The factorial of a non-negative integer n is defined as the product of all positive integers
    less than or equal to n. The factorial of 0 is defined as 1.

    Args:
        n (int): The integer whose factorial is to be calculated.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# The main function of the script
# The script takes a command-line argument, converts it to an integer,
# then calculates and prints the factorial of that number.
if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
