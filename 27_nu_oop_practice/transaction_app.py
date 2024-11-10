class User:
    def __init__(self, username, password, pin):
        self.username = username
        self.password = password
        self.pin = pin
        
    def change_username(self, new_username):
        self.username = new_username

    def change_password(self, new_password):
        self.password = new_password
    
    def change_pin(self, new_pin):
        self.pin = new_pin

""" Driver Code for User Instantiaion """
# user_1 = User("nick", "password123", 1234)
# user_2 = User("bob", "password321", 5678)
# user_3 = User("nako", "password987", 9876)
# for u in [user_1, user_2, user_3]:
#     print(u.username, u.password, u.pin)
""" Driver Code for User Methods """
# user_1.change_username("thenickedwards")
# user_2.change_password("newpa55!")
# user_3.change_pin(5555)
# for u in [user_1, user_2, user_3]:
#     print(u.username, u.password, u.pin)

class BankUser(User):
    def __init__(self, username, pin, password):
        super().__init__(username, pin, password)
        self.balance = 0
    
    def show_balance(self):
        print(f"\033[1m{self.username}\033[0m has an account balance of ${self.balance:.2f}")
    
    def withdraw(self, funds):
        self.balance -= funds
        print(f"\033[1m{self.username}\033[0m has withdrawn ${funds:.2f} and has an account balance of ${self.balance:.2f}")
    
    def deposit(self, funds):
        self.balance += funds
        print(f"\033[1m{self.username}\033[0m has deposited ${funds:.2f} and has an account balance of ${self.balance:.2f}")
        
    def transfer_money(self, funds, recipient):
        print(f"You are transferring ${funds:.2f} to {recipient.username}.")
        auth_pin = input("Authentication required\nEnter PIN to transfer: ")
        try:
            auth_pin = int(auth_pin)
            if auth_pin != self.pin:
                raise ValueError("❌ Sorry, invalid PIN.")
        except ValueError as e:
            print(e)
            return
        else:
            print("Transfer authorized!")
            self.withdraw(funds)
            print(f"Tranferring ${funds:.2f} to {recipient.username}...")
            recipient.deposit(funds)
    
    def request_money(self, funds, giver):
        print(f"You are requesting ${funds:.2f} from {giver.username}.")
        auth_pin = input("Authentication required\nEnter PIN to request: ")
        try:
            auth_pin = int(auth_pin)
            if auth_pin != self.pin:
                raise ValueError("❌ Sorry, invalid PIN.")
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


""" Driver Code for BankUser Instantiaion """ 
bank_user_1 = BankUser("nick", "password123", 1234)
bank_user_2 = BankUser("bob", "password321", 5678)
bank_user_3 = BankUser("nako", "password987", 9876)
for bu in [bank_user_1, bank_user_2, bank_user_3]:
    print(bu.username, bu.password, bu.pin, bu.balance)
""" Driver Code for BankUser Methods """
# display balance
bank_user_1.show_balance()
# withdraw
bank_user_2.balance = 10.00
bank_user_2.show_balance()
bank_user_2.withdraw(9)
bank_user_2.show_balance()
# deposit
bank_user_3.show_balance
bank_user_3.deposit(1000000)
bank_user_3.show_balance
# transfer $
bank_user_3.transfer_money(500, bank_user_1)
# request $
bank_user_1.request_money(500, bank_user_3)