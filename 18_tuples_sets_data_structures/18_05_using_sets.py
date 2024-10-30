numbers_set = {1, 2, 3, 4, 4}
print(numbers_set)
# duplicate values removed
# OUTPUT: {1, 2, 3, 4}

# invalid set bc of list
# numbers_set2 = {1, 2, 3, 4, [5, 6]}
# print(numbers_set2)
''' OUTPUT: 
Traceback (most recent call last):
  File "/Users/thenickedwards/Desktop/Repos/Nucamp ONPA-SU24-10-02/byte_of_py/18_tuples_sets_data_structures/18_05_using_sets.py", line 4, in <module>
    numbers_set2 = {1, 2, 3, 4, [5, 6]}
                   ^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'
'''

numbers_set3 = {1, 2, 3, 4, (5, 6)}
# valid bc list now tuple

# Access set values
words_set = {"Alpha", "Bravo", "Charlie"}
abcd = ""
for word in words_set:
    abcd += word
print(abcd)
# OUTPUT: BravoCharlieAlpha
# not sets are unordered, may return differently

if "Alpha" in words_set:
    print("Alpha in set")   # FOUND!
else:
    print("Alpha not in set")
    

# Modify set values
words_set.add("Delta")
print(words_set)
# {'Alpha', 'Delta', 'Bravo', 'Charlie'}
words_set.discard("Bravo")
print(words_set)
# {'Alpha', 'Delta', 'Charlie'}