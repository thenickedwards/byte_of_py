import re 

''' Business requirements in triple quotes '''

#####

def show_balance(balance):
    print(f"\nYour Current Balance:\n{balance:.2f}\n\n")

'''First, define a function named show_balance with 1 parameter of balance. When called, the code in this function should display the account balance of the logged-in user, using the print function.'''

#####

def deposit(balance):
    while True:
        amount = input("How much would you like to deposit?\n Enter amount in dollars and cents (e.g. 10.00, 10, etc): $").strip() # strip whitespace
        
        ### validate amount
        try:    
            amount = round(float(amount), 2)
            print(" Please confirm amount to deposit below:")
            print(f"    ${amount:.2f}")
            confirm_deposit = input("Enter 1 to confirm deposit or 2 to re-enter deposit amount: ")
            if confirm_deposit == "1" or confirm_deposit.lower() == "y":
                print(f"Great! We'll deposit ${amount:.2f}.")
                return balance + amount
            else:
                continue
        except:
            print("ERROR\nInvalid amount.")
            print("\nI didn't understand the amount you want to deposit. Let's try again.\n")
            continue
    
'''Second, define a function named deposit with 1 parameter of balance. In this function, declare a variable with a name such as amount, and set its value to an input function to prompt the user with: "Enter amount to deposit: ". Use a return statement to return the result of adding the balance and the amount together.'''

#####

def withdraw(balance):
    while True:
        amount = input("How much would you like to withdraw?\n Enter amount in dollars and cents (e.g. 10.00, 10, etc): $").strip() # strip whitespace
        
        ### validate amount
        try:    
            amount = round(float(amount), 2)
            print(" Please confirm amount to withdraw below:")
            print(f"    ${amount:.2f}")
            if amount > balance:
                print(f"\nUnfortunately, there are not enough funds in your account to withdraw ${amount:.2f}. Let's try again.\n")
                continue
            confirm_withdrawal = input("Enter 1 to confirm withdraw or 2 to re-enter withdrawal amount: ")
            if confirm_withdrawal == "1" or confirm_withdrawal.lower() == "y":
                print(f"Great! We'll withdraw ${amount:.2f}.")
                return balance - amount
            else:
                continue
        except:
            print("ERROR\nInvalid amount.")
            print("\nI didn't understand the amount you want to withdraw. Let's try again.\n")
            continue

'''Third, define a function named withdraw with 1 parameter of balance. This function will be similar to the deposit() function but will ask the user to "Enter amount to withdraw: " instead of deposit, and its return value will be the result of subtracting the amount from the balance.'''

#####

def logout(name):
    print(f"\nGoodbye {name}! \nThanks for banking with us.\n\n")
    
'''Finally, define a function named logout with 1 parameter of name. In this function, you only need to print "Goodbye" followed by the value of name.'''