state_capitals = {"Washington": "Olympia", "Oregon": "Salem", "California": "Sacramento"}

# iterate with keys
for state in state_capitals: 
    print(state)
    # Washington
    # Oregon
    # California
    
# iterate with values       # values method
for city in state_capitals.values(): 
    print(city)
    # Olympia
    # Salem
    # Sacramento

# iterate with keys[values]     # braket notation
for state in state_capitals:
    print(state_capitals[state], "is the capital of", state)
    # Olympia is the capital of Washington
    # Salem is the capital of Oregon
    # Sacramento is the capital of California

# iterate with keys, values     # items method
for state, city in state_capitals.items():
    print(city, "is the capital of", state)
    # Olympia is the capital of Washington
    # Salem is the capital of Oregon
    # Sacramento is the capital of California