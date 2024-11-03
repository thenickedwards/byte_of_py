def login(database, username, password):
    if username in database and database[f"{username}"] == password:
        print(f"\n  You have successfully logged in! \n Welcome back {username}")
        return username
    else: print("❌ Login Error: Incorrect username or password ❌")

def register(database, username):
    if username in database:
        print(f"\n  That username is already registered. \n Please try to register a different username.")
        print(f"\n\n  Returning to main menu...")
        return ""
    elif len(username) > 10 or len(username) < 5:
        print(f"\n  Usernames must be between 5 and 10 characters. \n Please try to register a different username.")
        print(f"\n\n  Returning to main menu...")
        return ""
    else:
        print(f"\n  Congratulations, you've registered the username: \n     {username}")
        return username


