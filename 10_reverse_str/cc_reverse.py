'''
Your Challenge:
Above the existing code in cc_reverse.py, define a function named reverse.
For its parameter list, provide a single parameter: str
In the function body, write code to reverse the string that is passed into the str parameter.
You will need to do some research online to find out how to reverse a string in Python. Typically, this is done using slicing notation. 
Return the reversed string as the return value of the function.
'''

def reverse(str):
    return str[::-1]

# Slice notation takes the form [start:stop:step]. In this case, we omit the start and stop positions since we want the whole string. We also use step = -1, which means, "repeatedly step from right to left by 1 character".

name = input("What is your name? ")
print("Your name reversed is:", reverse(name))
