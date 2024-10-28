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
