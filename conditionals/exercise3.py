# Exercise 3

# Create a program that compares two names and:
# - Checks if both start with the same letter
# - Or if both end with the same letter.


# My solution

print("My solution:\n")

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

if name1.lower()[0] == name2.lower()[0] and name1.lower()[-1] == name2.lower()[-1]:
    print("Both names start and end with the same letter.")
elif name1.lower()[0] == name2.lower()[0]:
    print("Both names start with the same letter.")
elif name1.lower()[-1] == name2.lower()[-1]:
    print("Both names end with the same letter.")
else:
    print("First and last letters do not match.")

# Teacher's solution

print("\nTeacher's solution\n")

name_1 = input("Name 1: ")
name_2 = input("Name 2: ")

if name_1[0] == name_2[0] or name_1[-1] == name_2[-1]:
    print("There's a match.")
else:
    print("No match.")
