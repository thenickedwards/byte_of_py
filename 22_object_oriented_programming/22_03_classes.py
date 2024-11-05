class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0
        
player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1300)

print("P1:", player1.name, " -- HP:", player1.hp, "-- SCORE: ", player1.score)
# P1: Aaron  -- HP: 1200 -- SCORE:  0
print("P2:", player2.name, " -- HP:", player2.hp, "-- SCORE: ", player2.score)
# P2: Irene  -- HP: 1300 -- SCORE:  0

player1.hp += 500 
player1.score += 10

print("P1:", player1.name, " -- HP:", player1.hp, "-- SCORE: ", player1.score)
# P1: Aaron  -- HP: 1700 -- SCORE:  10
print("P2:", player2.name, " -- HP:", player2.hp, "-- SCORE: ", player2.score)
# P2: Irene  -- HP: 1300 -- SCORE:  0