# Task 1: Calculate Factorial Using a Function

def factorial(n):
    result = 1
    # Using a loop
    for i in range(1, n + 1):
        result *= i
    return result

num = 5

print("The factorial of", num, "is:", factorial(num))


# Task 2: Using the Math Module for Calculations


import math

num = float(input("Enter a number: "))

sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)

print("\nResults:")
print(f"Square root of {num} = {sqrt_val}")
print(f"Natural logarithm of {num} = {log_val}")
print(f"Sine of {num} radians = {sine_val}")