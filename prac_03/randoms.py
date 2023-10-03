import random

dir(random)
print(random.randint(5, 20))  # line 1 produce random number between 5 and 20
print(random.randrange(3, 10, 2))  # line 2 3 - This is the lower bound of the range (inclusive).
# The random integer will be greater than or equal to 3.

# 10 - This is the upper bound of the range (exclusive).
# The random integer will be less than 10.

# 2 - This is the step size.
# It means that the generated random integer will be one of the following values: 3, 5, 7, or 9.
# It skips every other integer between 3 and 9.

print(random.uniform(2.5, 5.5))  # line 3

# Produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))