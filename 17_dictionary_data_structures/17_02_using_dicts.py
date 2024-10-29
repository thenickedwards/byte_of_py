state_capitals = {"Washington": "Olympia", "Oregon": "Salem", "California": "Sacramento"}

print(len(state_capitals))  # 3

# access dict values
print(state_capitals["Washington"])
# Olympia

# modifying and adding kvps
state_capitals["Washington"] = "Aberdeen" 
state_capitals["Texas"] = "Austin"
print(state_capitals)
# {'Washington': 'Aberdeen', 'Oregon': 'Salem', 'California': 'Sacramento', 'Texas': 'Austin'}

# delete with "del" keyword
del state_capitals["California"] 
print(state_capitals)
# {'Washington': 'Aberdeen', 'Oregon': 'Salem', 'Texas': 'Austin'}

removed_capital = state_capitals.pop("Oregon")
print(removed_capital)
# Salem

state_capitals = {"Washington": "Olympia", "Oregon": "Salem", "California": "Sacramento"}
state_capitals.pop("Oregon") 
print(state_capitals)
# {'Washington': 'Olympia', 'California': 'Sacramento'}

