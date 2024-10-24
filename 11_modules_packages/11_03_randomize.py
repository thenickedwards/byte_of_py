import random           # https://docs.python.org/3/library/random.html

### built in random methods

print(random.randint(1, 10))

pets = ['cat', 'dog', 'bird', 'dinosaur']

print(random.choice(pets))

print('orignal order: ', pets)
random.shuffle(pets)
print('shuffle #1: ', pets)
random.shuffle(pets)
print('shuffle #2: ', pets)
random.shuffle(pets)
print('shuffle #3: ', pets)

### more testing random module methods

pips = random.randint(1, 6)
print('You roll the die... it lands with', pips, 'pips showing.')

prizes = ["a car", "$10000", "a pony", "$500000"]
prize_won = random.choice(prizes)
print("You spin the wheel of fortune... It lands on a prize of", prize_won + "!!")

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
random.shuffle(cards)
print("The cards are now in this order: ")
print(cards)