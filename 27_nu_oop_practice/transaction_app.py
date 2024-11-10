class User:
    def __init__(self, username, password, pin):
    ## set and validate user data
        # set username
        try: 
            username = "".join(username.split()).lower() # remove all whitespace and lower
            if len(username) <= 1 or len(username) >= 11:
                raise ValueError("❌ Sorry, username must be between 2 and 10 characters.")
        except ValueError as e:
            print(e)
            return
        else:
            self.username = username
        # set password
        try: 
            if len(password) <= 5:
                raise ValueError("❌ Sorry, password must be at least 5 characters.")
        except ValueError as e:
            print(e)
            return
        else:
            self.password = password
        # set pin
        try:
            pin = int(pin)
            if len(str(pin)) != 4:
                raise ValueError("❌ Sorry, PIN must be 4 digits.")
        except ValueError as e:
            print(e)
            return
        else:
            self.pin = pin
    ## update user data
    def change_username(self, new_username):
        try: 
            new_username = "".join(new_username.split()).lower() # remove all whitespace and lower
            if len(new_username) <= 1 or len(new_username) >= 11:
                raise ValueError("❌ Sorry, username must be between 2 and 10 characters.")
        except ValueError as e:
            print(e)
            return
        else:
            self.username = new_username

    def change_password(self, new_password):
        try: 
            if new_password == self.password:
                raise ValueError("❌ Sorry, please choose a new password of at leasst 5 characters.")
            if len(new_password) <= 5:
                raise ValueError("❌ Sorry, password must be at least 5 characters.")
        except ValueError as e:
            print(e)
            return
        else:
            self.password = new_password
    
    def change_pin(self, new_pin):
        try:
            if new_pin == self.pin:
                raise ValueError("❌ Sorry, please choose a new 4 digit PIN.")
            if len(str(new_pin)) != 4:
                raise ValueError("❌ Sorry, PIN must be 4 digits.")
            new_pin = int(new_pin)
        except ValueError as e:
            print(e)
            return
        else:
            self.pin = new_pin

""" Driver Code for User Instantiaion """
# user_1 = User("nick", "password123", 1234)
# user_2 = User(" B ob ", "password321", 5678)    # username cleanup
# user_3 = User("nako", "password987", 9876)
# user_4 = User("a", "password", 1234)            # fail username validation
# user_5 = User("andrew", "p", 1234)              # fail password validation
# user_6 = User("andrew", "pw", 1)                # fail pin validation
# for u in [user_1, user_2, user_3]:
#     print(u.username, u.password, u.pin)
""" Driver Code for User Methods """
# user_1.change_username("thenick")
# user_2.change_password("newpa55!")
# user_2.change_password("newpa55!")              # fail password validation
# user_3.change_pin(5555)
# for u in [user_1, user_2, user_3]:
#     print(u.username, u.password, u.pin)

class BankUser(User):
    def __init__(self, username, pin, password):
        super().__init__(username, pin, password)
        self.balance = 0
        self.holding = False
    
    def show_balance(self):
        print(f"\033[1m{self.username}\033[0m has an account balance of ${self.balance:.2f}")
    
    def validate_amount(self, amount):
        try:
            int(amount)
            if amount <= 0:
                raise ValueError("❌ Enter a valid amount to withdraw.")
        except ValueError as e:
            print(e)
            return
        else:
            return True
    
    def withdraw(self, funds):
        if self.validate_amount(funds) == True:
            self.balance -= funds
            print(f"\033[1m{self.username}\033[0m has withdrawn ${funds:.2f} and has an account balance of ${self.balance:.2f}")
    
    def deposit(self, funds):
        if self.validate_amount(funds) == True:
            self.balance += funds
            print(f"\033[1m{self.username}\033[0m has deposited ${funds:.2f} and has an account balance of ${self.balance:.2f}")
        
    def transfer_money(self, funds, recipient):
        if self.validate_amount(funds) == True:
            print(f"\033[1m{self.username}\033[0m is transferring ${funds:.2f} to {recipient.username}.")
            auth_pin = input("Authentication required\nEnter PIN to transfer: ")
            try:
                if self.holding == True:
                    raise ValueError("Requests and transfers cannot be processed while on hold.")
                if recipient.holding == True:
                    raise ValueError("Requests and transfers cannot be processed while recipient is on hold.")
                auth_pin = int(auth_pin)
                if auth_pin != self.pin:
                    raise ValueError("❌ Sorry, invalid PIN.")
                if funds > self.balance:
                    raise ValueError("❌ Sorry, insufficient funds.")
            except ValueError as e:
                print(e)
                return
            else:
                print("Transfer authorized!")
                self.withdraw(funds)
                print(f"Tranferring ${funds:.2f} to {recipient.username}...")
                recipient.deposit(funds)
    
    def request_money(self, funds, giver):
        if self.validate_amount(funds) == True:
            print(f"\033[1m{self.username}\033[0m is requesting ${funds:.2f} from {giver.username}.")
            auth_pin = input("Authentication required\nEnter PIN to request: ")
            try:
                if self.holding == True:
                    raise ValueError("Requests and transfers cannot be processed while on hold.")
                if giver.holding == True:
                    raise ValueError("Requests and transfers cannot be processed while giver is on hold.")
                auth_pin = int(auth_pin)
                if auth_pin != self.pin:
                    raise ValueError("❌ Sorry, invalid PIN.")
                if funds > giver.balance:
                    raise ValueError("❌ Sorry, cannot send that request.")
            except ValueError as e:
                print(e)
                return
            
            print(f"To complete this request, you must have authorization from the user sending funds.")
            giver_pw = input("Enter password of user receiving your request: ")
            try:
                if giver_pw != giver.password:
                    raise ValueError("❌ Sorry, invalid password. Please check with the user receiving your request.")
            except ValueError as e:
                print(e)
                return
            
            else:
                print("Request authorized!")
                giver.withdraw(funds)
                print(f"Transferring ${funds:.2f} from {giver.username} to {self.username}...")
                self.deposit(funds)

    def on_hold(self):
        if self.holding == False:
            self.holding = True
            print(f"\033[1m{self.username}\033[0m is currently on hold.\nRequests and transfers cannot be processed.")
        else:
            self.holding = False
            print(f"\033[1m{self.username}\033[0m is no longer on hold.\nRequests and transfers are available again.")


""" Driver Code for BankUser Instantiaion """ 
# bank_user_1 = BankUser("nick", "password123", 1234)
# bank_user_2 = BankUser("bob", "password321", 5678)
# bank_user_3 = BankUser("nako", "password987", 9876)
# for bu in [bank_user_1, bank_user_2, bank_user_3]:
#     print(bu.username, bu.password, bu.pin, bu.balance)
""" Driver Code for BankUser Methods """
# # display balance
# bank_user_1.show_balance()
# # withdraw
# bank_user_2.balance = 10.00
# bank_user_2.show_balance()
# bank_user_2.withdraw(9)
# bank_user_2.show_balance()
# bank_user_2.withdraw(-9)                        # fail amount validation
# bank_user_2.withdraw("two")                     # fail amount validation
# # deposit
# bank_user_3.show_balance
# bank_user_3.deposit(100000)
# bank_user_3.show_balance
# # transfer $
# bank_user_3.transfer_money(500, bank_user_1)
# bank_user_1.transfer_money(1000, bank_user_3)   # fail insufficient funds check
# # request $
# bank_user_1.request_money(500, bank_user_3)
# bank_user_3.request_money(1000000, bank_user_1) # fail insufficient funds check
# # holding
# bank_user_2.on_hold()
# bank_user_2.transfer_money(1, bank_user_1)
# bank_user_2.on_hold()
# bank_user_2.transfer_money(1, bank_user_1)


'''
BONUS WORK
✔ 1. Add validation thus that only positive numbers can be deposited, withdrawn, transferred, and requested. If a string or negative number is entered, an appropriate message should be shown.

✔ 2. Take Task 1 further and update the transfer_money() and request_money() methods so that no amount greater than what is available can be transferred from one account to another.

✔ 3. Decide on validation parameters for the name, password, and PIN and update the change_name(), change_pin(), and change_password() methods to enforce those parameters. Examples:
    ✔ The username can only be changed if the new name is >= 2 characters and <= 10 characters.
    ✔ The password can only be changed if the new password is >= 5 characters.
    ✔ The PIN can only be changed if the new PIN is exactly 4 numbers.
    ✔ The new value cannot be the same as the previous value.
    ✔ No space characters are allowed.

✔ 4. Format the outputs so that dollar amounts display 2 digits after the decimal point instead of 1.
    Example: $500.00 instead of $500.0.

✔ 5. Add an instance attribute on the BankUser class called on_hold and initialize it to False.
    ✔ Add a method that can be called to toggle this on_hold class to the opposite of its current Boolean value. (So if it is True, flip it to False, and if it is False, flip it to True.)
    ✔ Add a check for each of the withdraw(), deposit(), transfer_money(), and withdraw_money() methods thus that if the on_hold attribute for any user involved in the transaction is True, the transaction is rejected with an appropriate failure message.
'''