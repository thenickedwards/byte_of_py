all_fruits = ["apple", "banana", "cherry", "mango"]
for fruit in all_fruits:
    print(f"We got a... {fruit}!")

""" OUTPUT: 
We got a... apple!
We got a... banana!
We got a... cherry!
We got a... mango!
"""


for x in 'string':
    if x =='i':
        continue # skip current iteration
    print(x)
    
""" OUTPUT: 
s
t
r
n
g
"""


for l in 'broken_string':
    if l =='k':
        break # break out of loop
    print(l)

""" OUTPUT: 
b
r
o
"""