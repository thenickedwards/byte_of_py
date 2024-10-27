import sys
import re
import time
import json
from banking_pkg.account import show_balance, deposit, withdraw, logout


name = ""
pin = ""
balance = 0.00


### MENUS
def start_menu():
    print("")
    print("          === Automated Teller Machine ===          ")
    print("Hello! Please choose to register or login.")
    print("------------------------------------------")
    print("| 1.    Register    | 2.    Login        |")
    print("------------------------------------------")

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

def loading_bar():
    loading_bar = "Loading menu..."
    for i in loading_bar:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.25)

### AUTHENTICATION v1
def register():
    global name
    global pin
    print("\n          === Automated Teller Machine ===          ")
    while name == "" or pin == "":
        name = input("Enter name to register: ")
        pin = input("Enter PIN to register: ")
        if name == "" or len(name) > 10:
            print("ERROR\nInvalid name to register. Please register a name for login. Note: names must be 10 characters or less.")
            print("\nLet's start over with registration.\n")
            continue
        elif len(pin) != 4 or not re.match(r"\d\d\d\d", pin):    # Negation Logic - could also be written elif len(pin) == 4 and re.match("\d\d\d\d", pin):
            print("ERROR \nInvalid PIN to register. Please register a 4 digit PIN for login.")
            pin = ""
            print("\n   Let's start over with registration.\n")
            continue
        else:
            print(f"Thank you, {name}! Your name and pin have been registered for login.")
            print(f"Hello {name}, your account shows a starting balance of ${balance:.2f}.")
            break

def login():
    global name
    global pin
    print("\n          === Automated Teller Machine ===          ")
    while True:
        login_name = input("Enter name to login: ")
        login_pin = input("Enter PIN to login: ")
        if login_name == name and login_pin == pin:
            print(f"\nWelcome {name}! \nYour have successfully logged in.\n\n")
            break
        else: 
            print("\n   Invalid Credentials.\n  We cannot verify the name and PIN. Please try to login again.")
            continue



##### MAIN APPLICATION BELOW #####

def main_atm():
    global name
    global pin
    global balance
    
    # register or login
    while True:
        start_menu()            # display start menu
        start_choice = input("Enter 1 to register or 2 to login: ")
        if start_choice == "1":
            register()
            break
        if start_choice == "2":
            if name == "" or pin == "":
                print("\nWe encountered an unexpected error. \n\nThanks for your patience. Please try again.")
                continue
            login()
            break
        else:
            print("\n   Sorry, I can't understand that choice.\n  Please choose to register or login.")
            continue
    
    # main menu
    while True:
        atm_menu(name=name)          # display account menu
        menu_choice = input("How can I help you?\n Enter choice: ")
        if menu_choice == "1":
            show_balance(balance=balance)
            loading_bar()
            continue
        elif menu_choice == "2":
            balance = deposit(balance=balance)
            print(f"\nThanks {name}! Your account now shows a balance of ${balance:.2f}\n\n")
            loading_bar()
            continue
        elif menu_choice == "3":
            balance = withdraw(balance=balance)
            print(f"\nThanks {name}! Your account now shows a balance of ${balance:.2f}\n\n")
            loading_bar()
            continue
        elif menu_choice == "4":
            logout(name)
            name=""
            pin=""
            main_atm()
        else:
            print("\n   Sorry, I can't understand that choice.\n  Please choose to register or login.")
            continue


'''
BUSINESS "NICE-TO-HAVE" FEATURES:
Bonus Feature 1
✓ In the registration step, allow only names with a length between 1 and 10 characters as a valid name.
✓ If an invalid name is entered, show a helpful error message, then ask for the registration name again.

Bonus Feature 2
✓ In the registration step, allow only a PIN to be entered that has a length of 4 characters.
✓ If an invalid PIN is entered, show a helpful error message, then ask for the registration PIN again.

Bonus Feature 3
✓ Write code to prevent a withdrawal that is larger than the current balance.
✓ When an attempt is made, show an appropriate error message.

Bonus Tasks Infinite
It's your turn to take the wheels: How else can you improve upon the existing code? More features? Improved formatting? Better error checking? Come up with some ideas of your own and try to implement them.
✓ Validation for deposit and withdrawl. We verify user input is a number and ask the user to confirm amount.
'''

    
if __name__ == "__main__":
    main_atm()