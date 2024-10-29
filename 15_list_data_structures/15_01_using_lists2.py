states = ["Washington", "Oregon", "California"]

#  list with for in loop
for x in states:
    print(x)
    # Washington
    # Oregon
    # California

for state in states:
    print(state)
    # Washington
    # Oregon
    # California
    
#  with method applied
for state in states:
    state = state.lower()
    print(state)
    # washington
    # oregon
    # california
    
print("Washington" in states)       # True
print("Tennessee" in states)        # False
print("Washington" not in states)   # False

# concatenating lists
states2 = ['Arizona', 'Ohio', 'Louisiana']
best_states = states + states2
# print(best_states)
#          ['Washington', 'Oregon', 'California', 'Arizona',  'Ohio', 'Louisiana' ]
# indices  [0,             1,        2,            3,          4,      5          ]

# slicing lists
print(best_states[1:3])     # ['Oregon', 'California']
print(best_states[:2])      # ['Washington', 'Oregon']
print(best_states[4:])      # ['Ohio', 'Louisiana']


