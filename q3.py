# File: q3.py
# Author: Brittany Vamvakias
# Date: 01/21/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description: This program evaluates 8 different operations and prints the result.

a = -3 + 8 * 12 / 3 - 2
b = 6 % 2 + 4 * (-4 + 2) * 8 - 3 / 2
c = 27 % 4 % 2 * 3 + 2 * 2 / 2 + (7 * 3 + 2)
d = 13.5 // 2
e = 13.5 / 2
f = 13 // 2
g = 13 / 2
h = 2.1 + 3 ** 7 / 3 - 16 % 2 * 3**4.2

# Section b returns a syntax error without the multiplication operator * between (-4+2) and 8 because the code doesn't know what to do without the multiplication operator. Adding the multiplication operator fixes it.

print(f"a. : {a}")
print(f"b. : {b}")
print(f"c. : {c}")
print(f"d. : {d}")
print(f"e. : {e}")
print(f"f. : {f}")
print(f"g. : {g}")
print(f"h. : {h}")

# ()
# **
# + - (positive and negative)
# * / % //
# + - (plus and minus)
