# Exercise 4

# Obtain the final price you have to pay if a discount of 36% is applied to the total purchase.

# My first answer

item1 = float(input("Item 1: "))
item2 = float(input("Item 2: "))
item3 = float(input("Item 3: "))

total_purchase = item1 + item2 + item3

print(f"The total price of the items is {total_purchase:.2f}")

discount = float(input("What discount (in %) is applicable? "))

final_price = total_purchase * (1 - discount/100)

print(f"The final price after discount is {final_price:.2f}")

# Teacher's answer

initial_price = float(input("Enter the price: "))
discount = initial_price*(36/100)
final_price = initial_price - discount

print(f"Final price is: {final_price:.2f}")
