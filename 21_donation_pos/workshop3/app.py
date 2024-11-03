import os
import sys
import time
from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

# os and global varaibles
roundup_admin = os.environ['roundup_admin']
roundup_password = os.environ['roundup_pw']
database = {
             roundup_admin: roundup_password
            }

donations = []
authorized_user = ""

while True:
    ### initialize app
    show_homepage()
    # check auth state
    if authorized_user == "":
        print("\n🔴   You must be logged in to donate.\n")
    else:
        print(f"\n🟢  Logged in as: {authorized_user}")

    ### user selection from start menu
    user_choice = input("Choose an option by entering a number: ")
    
    # login
    if user_choice == "1" or user_choice.lower() == "login":
        username = input("Enter username: ").lower()
        password = input("Enter password: ")
        authorized_user = login(database=database, username=username, password=password)
        user_choice == ""   #reset
        if authorized_user == None:
            authorized_user = ""
        continue
    
    # register
    elif user_choice == "2" or user_choice.lower() == "register":
        username = input("Register username: ").lower()
        password = input("Register password: ")
        registered_user = register(database=database, username=username)
        if registered_user == None:
            continue
        else:
            database[f'{registered_user}'] = f'{password}'
        user_choice == ""   #reset
        continue
    
    # donate
    elif user_choice == "3" or user_choice.lower() == "donations":
        if authorized_user == "":
            print("❌ You must be logged in to donate.\n")
        else:
            gift = donate(username=authorized_user)
            donations.append([authorized_user, gift])
        user_choice == ""   #reset
        continue

    # display donations
    elif user_choice == "4" or user_choice.lower() == "show donations":
        show_donations(donations=donations)
        user_choice == ""   #reset
        continue
    
    # logout
    elif user_choice == "5" or user_choice.lower() == "logout":
        authorized_user = ""
        print("Thanks for using Roundup! to donate and have a wonderful day!")
        continue
    
    # quit application
    elif user_choice.lower() == "q" or user_choice.lower() == "x" or user_choice.lower() == "quit" or user_choice.lower() == "exit":
        loading_exit = "\n\nQuitting..."
        for i in loading_exit:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.25)
        quit()
    
    # invalid entry handling
    else:
        print(f"\n  ❌ ERROR: Sorry, I didn't understand your choice. \n Let's try again.")
        print(f"\n\n  Returning to main menu...")
    
    


