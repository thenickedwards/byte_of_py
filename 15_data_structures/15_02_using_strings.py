my_string = "alpha"
multiline_string = """bravo
charlie"""
print(my_string)            # alpha
print(multiline_string)
# bravo
# charlie

#####
print("#####")
#####

print(my_string[0]) # a
print(my_string[3]) # h

# slicing strings
print(my_string[0:3])   # alp
print(my_string[:2])    # al
print(my_string[2:])    # pha
print(my_string)        # alpha

# my_string[0] = "b"​ # ERR - cannot change string, immutable

# strings and for loops
for char in my_string:
    print(char)
    
print("pha" in my_string)   # True
print("z" not in my_string) # True bc not keyword

# f strings
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

# f strings w/ expressions
number = 5
square = f"The square of {number} is {number ** 2}."
print(square)

# f strings w/ methods
my_string = "hello world"
formatted_string = f"{my_string.upper()} has {len(my_string)} characters."
print(formatted_string)

# f strings and formatting numbers
pi = 3.14159
formatted_pi = f"Pi to three decimal places is {pi:.3f}"
print(formatted_pi)


name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."

# f strings in multiline
multiline_fstring = f"""
Name: {name}
Age: {age}
Greeting: {greeting}
"""
print(multiline_fstring)