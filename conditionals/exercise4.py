# Exercise 4

# Create a program that simulates an ATM (automatic teller machine) with an initial balance of $ 2,000.- with the following menu:

# 1. Deposit cash 
# 2. Withdraw cash
# 3. Show balance
# 4. Exit

# My solution

balance = 2000.0

#print("\nWelcome to BankATM.\nPlease select an option:\n\n1. Deposit cash\n2. Withdraw cash\n3. Show balance\n4. Exit\n")

# My solution

actionable_options = ["1. Deposit cash","2. Withdraw cash","3. Show balance", "4. Exit"]
selection = 0
print("My solution:\n")
print("\nWelcome to BankATM.")

while selection != 4:
    print("Please select an option to proceed:\n")
    for option in range(len(actionable_options)):
        print(actionable_options[option])

    selection = int(input("\nEnter here: "))

    print(f"You selected '{actionable_options[selection-1]}'")
    if selection == 1:
        operation = float(input("Please enter the amount you wish to deposit: $"))
        balance += operation
        print("The operation was performed succesfully.\n")
        print(f"New account balance is ${balance}")
    elif selection == 2:
        operation = float(input("Please enter the amount you wish to withdraw: $"))
        if operation <= balance:
            balance -= operation
            print("The operation was performed succesfully.\n")
            print(f"New account balance is ${balance}")
        elif operation > balance:
            print("Error. Insufficient funds.")
        else:
            print("Error. Invalid input.")
    elif selection == 3:
        print(f"The current balance is ${balance:.2f}\n")
print("Exiting.")

# Teachers solution

balance2 = 2000

print("Teacher's solution:\n")
print("1. Deposit money")
print("2. Withdraw money")
print("3.Show money")
print("4. Exit")

selection2 = int(input("Choose an option: "))

if selection2 == 1:
    entry = float(input("Money to add to the account: "))
    balance2 += entry
    print(f"New balance in the account: {balance2}")
elif selection2 == 2:
    outgoing = float(input("Money to substract: "))
    if outgoing > balance2:
        print("Insufficient funds.")
    else:
        balance2 -= outgoing
        print(f"New available balance: {balance2}")
elif selection2 == 3:
    print(f"Available balance: {balance2}")
elif selection2 == 4:
    print("Ends.") 
else:
    print("Selected option is invalid.")