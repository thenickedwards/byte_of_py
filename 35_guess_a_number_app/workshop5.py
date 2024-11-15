import random

'''
human vs linear vs binary searches

Requirements
GOAL 1: Have a player guess a random number.
GOAL 2: Have the program guess a random number using linear search.
GOAL 3: Have the program guess a random number using binary search.
'''


# Human vs Random Number
def guess_random_number(tries, start, stop):
    target = random.randint(start, stop)
    print(f"I'm thinking of a number between {start} and {stop}. Can you guess it?")
    while tries > 0:
        print(f"Let's give it go, you have {tries} chances left.")
        guess = int(input(f"Guess a number between {start} and {stop}: "))
        if guess == target:
            print("Congrats! You won!!! 🎉")
            return
        elif guess < target:
            print("Close but you're way off. Guess higher!")
            tries -= 1
            continue
        elif guess > target:
            print("Perfect guess, for another game. Guess lower!")
            tries -= 1
            continue
    print(f"Sorry you're out of tries and failed to guess the number. \n    (pssst, the number was {target})")


# Linear Search vs Random Number
def guess_random_num_linear(tries=5, start=0, stop=10):
    nums_list = list(range(start, stop+1))
    target = random.randint(start, stop)
    print(f"I'm thinking of a number between {start} and {stop}. Can a linear search find the number with only {tries} tries?")
    for i in nums_list:
        while tries > 0:
            print(f"Let's give it go, you have {tries} chances left.")
            print(f"Linear search will guess: {i}")
            if i == target:
                print("Congrats! Linear search worked!!! 🎉")
                return
            elif i < target:
                print("Close but you're way off. Guess higher!")
                tries -= 1
                i += 1
                continue
            elif i > target:
                print("Perfect guess, for another game. Guess lower!")
                tries -= 1
                i += 1
                continue
    print(f"Sorry linear search is out of tries and failed to guess the number. \n    (pssst, the number was {target})")
            
        
# Binary Search vs Random Number






# EXAMPLES
def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1
    
    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]
        
        if pivot_value == target:
            print(f"Got it! Found {pivot_value} at index {the_list.index(pivot_value)}")
            return pivot
        if pivot_value > target:
            upper_bound = pivot - 1
        else:
            lower_bound = pivot + 1
    print(f"Can't find {target} in this list.")
    return -1


##########     DRIVER CODE     ##########
# guess_random_number(5, 0, 10)
guess_random_num_linear(5, 0, 10)