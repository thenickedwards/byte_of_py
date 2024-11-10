class User:
    def __init__(self, username, pin, password):
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

""" Driver Code for BankUser Instantiaion """ 
bank_user_1 = BankUser("nick", "password123", 1234)
bank_user_2 = BankUser("bob", "password321", 5678)
bank_user_3 = BankUser("nako", "password987", 9876)
for bu in [bank_user_1, bank_user_2, bank_user_3]:
    print(bu.username, bu.password, bu.pin, bu.balance)
""" Driver Code for BankUser Methods """
bank_user_1.show_balance()
# 
bank_user_2.balance = 10.00
bank_user_2.show_balance()
bank_user_2.withdraw(9)
bank_user_2.show_balance()
# 
bank_user_3.show_balance
bank_user_3.deposit(1000000)
bank_user_3.show_balance