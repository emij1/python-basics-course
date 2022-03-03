# Exercise 2

# Create an algorithm to swap the values of two variables.
# For example: a = 20 and b = 30
# End result has to be a = 30 and b = 20

# Attempt 1, without watching the video

a = input("Define the value of a: ")
b = input("Define the value of b: ")

print(f"The initial values are: a = {a} y b = {b}")

swap_variable = ""

swap_variable = a
a = b
b = swap_variable

print(f"The final values are: a = {a} y b = {b}")

# Turns out, the teacher explains that this operation is already incorporated into python sintax. It is the following:

c = input("Define the value of c: ")
d = input("Define the value of d: ")

print(f"The initial values are: c = {c} y d = {d}")

c,d = d,c

print(f"The final values are: c = {c} y d = {d}")

# Nice!
