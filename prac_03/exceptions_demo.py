"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if the user inputs something
that cannot be converted to an integer

2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if the user enters a denominator of 0.
Division by zero is undefined in mathematics, so attempting to divide by zero in Python

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, you can avoid the possibility of a ZeroDivisionError by checking the value
of the denominator before performing the division.
Here's an updated version of the code that includes such a check:
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")