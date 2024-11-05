# Oriented Programming
# Classes - blueprint for an object 
#           can be use like a custom data structure
#           Class inheritance - child classes based on parent classes

class Player: 
    max_hp = 4000
    
# Objects - instantiating → instances of a class

player1 = Player() 
print(player1.max_hp)       # 4000

player2 = Player()
print(player2.max_hp)       # 4000

Player.max_hp = 5000
print(player1.max_hp)       # 5000
print(player2.max_hp)       # 5000