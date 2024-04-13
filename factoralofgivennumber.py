#! /usr/bin/env python3
# Time Complexity: Given number is O(n), where n is the number itself.
def factorial(n):
    if n < 0: # Defines a function 'factorial(n) that takes an integer 'n' as input.
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1 # Initializes a variable 'result' to 1.
    for i in range(1, n + 1): # Iterates from 1 to 'n' (inclusive) using a 'for' loop.
        result *= i # In each iteration, this multiplies 'result' by the current value of 'i'.
    return result # After the loop completes, 'result' contains the factorial of 'n' which is returned.

# Tests the functions
num = 5
print(f"The factorial of {num} is {factorial(num)}")
    
