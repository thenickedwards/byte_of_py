my_string = "giraffe"
print(my_string[-1])    # e  # negative numbers will get characters indexed from end
print(my_string[2:4])   # ra # get characters from index 2 to 4 (not included)

# substring = s[start : end : step]
print(my_string[:])     # get whole string
print(my_string[::])    # get whole string

# Characters from index 5 to the end                    # fe
print(my_string[5:])

# Characters from the start up to index 3 (exclusive)   # gir
print(my_string[:3])

