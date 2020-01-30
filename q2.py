# File: q2.py
# Author: Brittany Vamvakias
# Date: 01/21/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description: This program asks for two student's name, age, and UIN and uses these inputs to greet the students and state how old they will be in the next year.

print("*****************************************************************")

student1 = input("Enter the first student's name: ")
student1_age = input("Enter the first student's age: ")
student1_uin = input("Enter the first student's UIN: ")

student2 = input("Enter the second student's name: ")
student2_age = input("Enter the second student's age: ")
student2_uin = input("Enter the second student's UIN: ")

print(" __    __    ______   ____    __    ____  _______  ____    ____  ")
print("|  |  |  |  /  __  \  \   \  /  \  /   / |       \ \   \  /   / ")
print("|  |__|  | |  |  |  |  \   \/    \/   /  |  .--.  | \   \/   / ")
print("|   __   | |  |  |  |   \            /   |  |  |  |  \_    _/   ")
print("|  |  |  | |  `--'  |    \    /\    /    |  '--'  |    |  |   ")
print("|__|  |__|  \______/      \__/  \__/     |_______/     |__|  ")
print()

print(f"Next year, {student1} with UIN number {student1_uin} will be {int(student1_age)+1} and {student2} with UIN number {student2_uin} will be {int(student2_age)+1}.")
print("*****************************************************************")
