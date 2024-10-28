import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

print("Let's play a game 🃏")
play_or_quit = input('Would you like to play? \nPress "Q" to quit or "Y" to pick a card: ')

while play_or_quit.lower() != "y":
    #  quit or error
    if play_or_quit.lower() == "q":
        quit()
    elif play_or_quit.lower() != "y":
        print("Sorry, I didn't understand that. \n\n")
        print("Let's play a game 🃏")
        play_or_quit = input('Would you like to play? \nPress "Q" to quit or "Y" to pick a card: ')
        continue

while diamonds:
    # playing the game
    if play_or_quit.lower() == "y":
        random_card = random.choice(diamonds)
        print(f"You drew a {random_card}!")
        diamonds.remove(random_card)
        hand.append(random_card)
        print(f"Your hand: {hand}")
        print(f"Remaining cards: {diamonds}")
        continue
    
    print("You got all the cards! 🏆 \nCONGRATS!")
    break