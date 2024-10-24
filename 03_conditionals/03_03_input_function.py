# native input() function to request data from user
# variable = input(prompt)
name = input("What is your name? ")
print(f"Nice to meet you, {name}!")
print("name variable data type is ", type(name), "It's always a string XD")

while True:
    print("1. Number One")
    print("2. Number Two")
    print("3. Break out of infintie loop")
    option = input("Pick an option: ")
    if option == "1":
            print("You chose 1!")
    elif option == "2":
            print("You chose 2!")
    elif option == "3":
            print("LEAVING THE LOOP!")
            break
    else:
           print("Invalid command: pick an option 😮‍💨")
print(f"Congratulations, {name}. You have left the loop.")