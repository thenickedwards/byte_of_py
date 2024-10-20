# PC OPTIONS
wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150

elf = "Elf"
elf_hp = 100
elf_damage = 100

human = "Human"
human_hp = 150
human_damage = 20

# BBEG
dragon = "Dragon"
dragon_hp = 300
dragon_damage = 50

##### CHARACTER SELECTION
while True:
    print(
    """
    WELCOME TO BATTLE GAME! 

    Your journey of epic adventure starts now. 🏹🔥🐉🛡️🗡️
    Begin by choosing a character from the options below:
    1) Wizard
    2) Elf
    3) Human
    """)
    pc_choice = input("Choose your character by entering their number: ")

    if pc_choice == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif pc_choice == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif pc_choice == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown character")
        continue

print(f"""
You have chosen: 
{character}
Health: {my_hp}
Damage: {my_damage}
""")

##### DRAGON BATTLE
while True:
    print(f"The {character} attacked and damaged the Dragon for {my_damage} HP!")
    dragon_hp = dragon_hp - my_damage
    print(f"The Dragon's hit points are now: {dragon_hp}")
    if dragon_hp <= 0:
        print(f"The battle is over and the {character} has won the day! 🗡️🏹🛡️")
        break

    print(f"The Dragon attacked and damaged you for {dragon_damage} HP!")
    my_hp = my_hp - dragon_damage
    print(f"Your hit points are now: {my_hp}")
    if my_hp <= 0:
        print(f"The battle is over and the {character} has been defeated by the Dragon. Better luck next time 🔥")
        break

"""
Optional Challenges for v1:
Choose character by typing class (case_insensitive)  or number.
Add "Dwarf" class.
Write exit game option.
After game over, ask if they want to play again.

Optional Challenges for v2:
Roll to hit, roll for damage.
Attack bonuses.
Damage relative to random d20 roll.
HP randomizes within range.
BBEG randomizes.
Classes as chraracter types.
"""