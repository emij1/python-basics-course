#Exercise 1

# Create a program that asks the user for 2 number values, and returns as a result which one is an even number or if both are even numbers

print("Hello. I can tell you wheter one or both of the numbers you give me are even numbers.\n")

num1 = int(input("Enter the first number: "))
num2 = int(input("Great! Now enter the second number: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Okay! Both numbers you entered are even numbers.")
elif num1 % 2 == 0:
    print(f"Well, {num1} is an even number, but {num2} is odd.")
elif num2 % 2 == 0:
    print(f"Well, {num2} is an even number, but {num1} is odd.")
else:
    print(f"Oops! Neither {num1} or {num2} is an even number.")
