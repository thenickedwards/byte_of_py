import banking_pkg
import re

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

### AUTHENTICATION v1
def register():
    global name
    global pin
    print("\n          === Automated Teller Machine ===          ")
    while name == "" or pin == "":
        name = input("Enter name to register: ")
        pin = input("Enter PIN to register: ")
        if name == "":
            print("ERROR\nInvalid name to register. Please register a name for login.")
            print("\nLet's start over with registration.\n")
            continue
        elif len(pin) != 4 or not re.match("\d\d\d\d", pin):    # Negation Logic - could als be written elif len(pin) == 4 and re.match("\d\d\d\d", pin):
            print("ERROR \nInvalid PIN to register. Please register a 4 digit PIN for login.")
            pin = ""
            print("\n   Let's start over with registration.\n")
            continue
        else:
            print(f"Thank you, {name}! Your name and pin have been registered for login.")
            print(f"Hello {name}, your account shows a starting balance of $0.00.")
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
    start_menu()
    while True:
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
    print("🔥 Out of first while loop‼️")


    
if __name__ == "__main__":
    main_atm()