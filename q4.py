# File: q4.py
# Author: Brittany Vamvakias
# Date: 01/21/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description: This program asks for the height and radius of a cone and calculates and prints both the volume and surface area.

radius = int(input("Enter the radius of a cone: "))
height = int(input("Enter the height of a cone: "))
pi = 3.14
print()

volume = pi * radius**2 * height / 3
print(f"The volume of a cone with radius {radius} and height {height} is {volume}.")

surface_area = pi * radius * (radius * (height**2 + radius**2)**(1 / 2))
print(f"The surface area of a cone with radius {radius} and height {height} is {surface_area}.")
