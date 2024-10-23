# using native range()
for i in range(0, 5, 1):
    # range(start, stop, step)
    print(f"i is {i}")
    
""" OUTPUT:
i is 0
i is 1
i is 2
i is 3
i is 4
"""

# using iterable value
sounders_cabinet = ["U.S. Open Cup 2009", "U.S. Open Cup 2010", "U.S. Open Cup 2011", "U.S. Open Cup 2014", "Supporters' Shield 2014", "MLS Cup 2016", "MLS Cup 2019", "CONCACAF Champions Cup 2022"]

for trophy in sounders_cabinet:
    print(f"Sounders win {trophy}! 💚💙")
    
for l in "CHAMPIONS":
    print(l)