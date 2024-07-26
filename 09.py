# Write a program to swap two numbers without using third variables.

num1 = 10
num2 = 20

# Swap the numbers without using a third variable
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

# Display the swapped numbers
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)