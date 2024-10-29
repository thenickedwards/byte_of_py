states = ["Washington", "Oregon", "California"]

print(states[0])    # Washington
print(states[1])    # Oregon
print(states[2])    # California

print(states[-1])   # California
print(states[-2])   # Oregon
print(states[-3])   # Washington

# modify list
states[2] = "Arizona"
print(states)       # ['Washington', 'Oregon', 'Arizona']

# find length (number of values in list)
print(len(states))  # 3

#  add value to list
states.append("New York")
print(states)       # ['Washington', 'Oregon', 'California', 'New York']

# remove last value
states.pop()        # ['Washington', 'Oregon']
print(states)

# removes value at index
states.pop(1)       # ['Washington']
print(states)
