def show_homepage():
    print("")
    print("       === Roundup Donations Homepage ===       ")
    print("------------------------------------------------")
    print("| 1.    Login       | 2.    Register           |")
    print("------------------------------------------------")
    print("------------------------------------------------")
    print("| 3.    Donate      | 4.    Show Donations     |")
    print("------------------------------------------------")
    print("------------------------------------------------")
    print("|               5.  Logout                     |")
    print("------------------------------------------------")
    print("|                              X or Q to Quit  |")

def donate(username):
    while True:
        donation_amt = input("Enter amount to donate: ")
        try: 
            donation_amt = round(float(donation_amt), 2)
            if donation_amt <= 0:
                print(f"\n❌  Cannot process that amount to donate. \n Please try AGAIN.")
                print(f"\n\n  Returning to main menu...")
                break
        except:
            print(f"\n❌  Cannot process that entry. \n Please try again.")
            print(f"\n\n  Returning to main menu...")
            break
        confirm_amt = input(f"\n\nEnter Y to confirm a donation of: ${donation_amt:.2f} or enter N to cancel: ")
        if confirm_amt.lower() != "y":
            continue
        else:
            donation_string = f"\n  Thank you!\n    {username} has donated {donation_amt:.2f}."
            print(donation_string)
            return donation_amt

def show_donations(donations):
    if donations == []:
        print("Currently, there are no donations.")
    else:
        print("")
        print("           === Roundup Donations ===            ")
        total = 0
        for gift in donations:
            print(f"{gift[0]} has generously donated ${gift[1]:.2f}")
            total += gift[1]
        print(f"\nFor a grand total of donatations ${total}\n\n")
            

