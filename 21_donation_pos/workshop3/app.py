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
    if user_choice == "1":
        username = input("Enter username: ").lower()
        password = input("Enter password: ")
        authorized_user = login(database=database, username=username, password=password)
        user_choice == ""   #reset
        if authorized_user == None:
            authorized_user = ""
        continue
    
    # register
    elif user_choice == "2":
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
    elif user_choice == "3":
        if authorized_user == "":
            print("❌ You must be logged in to donate.\n")
        else:
            gift = donate(username=authorized_user)
            donations.append([authorized_user, gift])
        user_choice == ""   #reset
        continue

    # display donations
    elif user_choice == "4":
        show_donations(donations=donations)
        user_choice == ""   #reset
        continue
    
    # quit
    elif user_choice == "5":
        authorized_user = ""
        print("Thanks for using Roundup! to donate and have a wonderful day!")
        continue
    
    elif user_choice.lower() == "q" or user_choice.lower() == "x":
        loading_exit = "\n\nQuitting..."
        for i in loading_exit:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.25)
        quit()
    
    


