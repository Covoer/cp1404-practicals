# 1.Ask the user for their name, write it to "name.txt," and then read and print the name:
# Writing the name to "name.txt"
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# Reading and printing the name from "name.txt"
with open("name.txt", "r") as file:
    stored_name = file.read()
    print(f"Your name is {stored_name}")

# 2.Open "numbers.txt," read the first two numbers, add them together, and print the result:
with open("numbers.txt", "r") as file:
    number1 = int(file.readline())
    number2 = int(file.readline())

result = number1 + number2
print("Result:", result)  # Should print "Result: 59"


# 3.Print the total for all lines in "numbers.txt" (or any file with any number of numbers):
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        number = int(line)
        total += number

print("Total:", total)  # This will print the sum of all numbers in "numbers.txt"
