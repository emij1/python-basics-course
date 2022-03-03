# Exercise 2

# Create a program that asks the user for 3 numbers and determine which one is the larger.

print("Hello. I can tell which one of the numbers you give me is the largest.\n")

num1 = int(input("Enter the first number: "))
num2 = int(input("Great! Now enter the second number: "))
num3 = int(input("Awesome! Now enter the third number: "))

if num1 == num2 and num2 == num3:
    print(f"The only number recieved is {num1}")
elif num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")