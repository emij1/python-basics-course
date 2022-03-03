# Exercise 1

# Create a program that shows the sum of all numbers between 0 and 100.

# I'm going to write it in a way that the user can define the range, instead of being static.

sum = 0
print("Hello. I can sum all the integer numbers within a range that you specify, and return it to you.\nIncluding the last number of the range.\n")
first_number = int(input("Enter the first number: "))
last_number = int(input("Enter the last number: "))

for number in range(first_number,last_number+1):
    sum += number

print(f"The sum of all numbers between {first_number} and {last_number} (not inluding 100) is {sum}")

