# using native range()
for i in range(0, 5, 1):
    # range(start, stop, step)
    # stop is non-inclusive
    print(f"i is {i}")
    
""" OUTPUT:
i is 0
i is 1
i is 2
i is 3
i is 4
"""

# can use 1 argument
for x in range(3):
    # range(start_default==0, stop==6, step_default=1)
    # stop is non-inclusive
    print(f"x is {x}")
    
""" OUTPUT:
x is 0
x is 1
x is 2
"""

# can use 2 arguments
for f in range(2, 4):
    # range(start==2, stop==6, step_default=1)
    # stop is non-inclusive
    print(f"f is {f}")
    
""" OUTPUT:
f is 2
f is 3
"""