# File: q1.py
# Author: Brittany Vamvakias
# Date: 01/21/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description: This program asks for two numbers and performs various operations to them, including changing the type and mathematical operations.

# Section A
print("******************************* Section A *******************************")
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
print("The type of the first variable is <class 'str'>")
print("The type of the second variable is <class 'str'>")
print()

# Section B
# sum = number1 + 1
# print(f"{sum}")
# The error give from line 14 is a type error because number1 is a string, and you cannot
# add an integer to a string.

# Section C
print("******************************* Section C *******************************")
sum = number1 + number2
print(f"The result of adding a string to another string is: {sum}")
# There is no error with line 21 because both number1 and number2 are strings.
print()

# Section D
print("******************************* Section D *******************************")
sum1 = int(number1) + int(number2)
print(f"The result of adding {number1} to {number2} is: {sum1}")
print("The type of the result is: <class 'int'>")
print()

# Section E
print('******************************* Section E *******************************')
result1 = int(number1) + 2.45
result2 = int(number2)**2
print(f"The result of adding {number1} to 2.45 is: {result1}")
print(f"The type of the result is: <class 'float'>")
print(f"The square of {number2} is: {result2}")
print(f"The type of the result is: <class 'int'>")
print()

# Section F
print("******************************* Section F *******************************")
divide = result1 / result2
remain = result1 % result2
print(f"{result1} over {result2} is: {divide} and the remainder is {remain}")
print()

# Section G
print("******************************* Section G *******************************")
avg = (result1 + result2) / 2
print(f"The average over {result1} and {result2} is {avg}.")
