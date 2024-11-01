def login(database, username, password):
    if username in database and database[f"{username}"] == password:
        print(f"\n  You have successfully logged in! \n Welcome back {username}")
        return username
    else: print("❌ Login Error: Incorrect username or password ❌")

def register(database, username):
    if username in database:
        print(f"\n  That username is already registered. \n Let's try another.")
        return ""
    else:
        print(f"\n  Congratulations, you've registered the username: \n     {username}")
        return username


