class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)
        
user1 = User("jane", "jane@nucamp.co", "janespassword")
print(user1.password)
# janespassword

user1.change_password("be$tp455word!")
# Your password has been changed to be$tp455word!

print(user1.password)
# be$tp455word!