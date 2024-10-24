import random

high_score = 0


def dice_game():
    global high_score
    while True:
        print(
        f"""
        TIME FOR A DICE GAME 🎲😈🎲

        Current high score: {high_score}
        
        Wanna play?
        1) Roll them dice! 
        2) Leave Game 👿
        """)
        pc_choice = input("Choose your choice: ")
        
        if pc_choice == '2':
            print("Thanks for stopping by! Don't be a stranger and come 'round soon again, ya here? :D")
            break
        elif pc_choice == '1':
            die_1 = random.randint(1, 6)
            die_2 = random.randint(1, 6)
            print(f'\n🎲 On your first die you roll a... {die_1}')
            print(f'🎲 On your second die you roll a... {die_2}')
            print(f'\nFor a total of: {die_1 + die_2}\n')
            # high score check
            if die_1 == 1 and die_2 == 1:
                print(f'Wow. Nice one. 😂')
            elif die_1 + die_2 > high_score:
                print(f'Congrats on the new high score! 🔝')
                high_score = die_1 + die_2
                if high_score == 12:
                    print("\nYOU'VE DONE IT! You've beaten the game. This is the best you could possibly do.\nCongrats champ 🏆")
                    break
            elif die_1 + die_2 == high_score:
                print(f'Pretty good, you tied high score! Wanna try to beat it? 😏')
            else:
                print(f'Not bad. Not great. Wanna try again? 🐓')
            continue
            
# let's get this party started :D
dice_game()



'''
Your Challenge:
Write the content of the body for the dicegame() function so that it works like this:
When the code is first run, this menu is shown:
    Current High Score: 0
    1) Roll Dice
    2) Leave Game
    Enter your choice:

Entering a choice of 1 results in a pair of dice being "thrown". That is, two separate random integers from 1-6 are chosen. 
The result from each "roll" is shown to the player, along with the total. 
The total is also compared to the value of high_score. If it is higher than the high_score, then it is set as the new high score, and a message is shown.
    Current High Score: 0
    1) Roll Dice
    2) Leave Game
    Enter your choice: 1
    
    You roll a... 2
    You roll a... 6
    
    You have rolled a total of: 8
    
    New high score!
    
    Current High Score: 8
    1) Roll Dice
    2) Leave Game
    Enter your choice: 2
    
    Goodbye!
    
The player can repeat option 1 as many times as they like. If they choose option 2, the game exits:

TIPS:
Use an infinite while loop, breaking out of the loop if the player chooses option "2". 
To include newlines in your print statements, you can use \n inside quotes. For example, the \n in this print statement creates a newline at the end of the text:
print("New high score!\n")
You will need to use what you learned about modifying global variables in local scope. 

'''