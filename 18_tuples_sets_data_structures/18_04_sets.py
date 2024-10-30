# Set (items are unordered, mutable, and do not allow duplicate values (they are remved) or mutable data types, i.e. lists, dictionaries, or sets)

valid_set = {"ALPHA", 123, (True, False)}
print(valid_set)
# OUTPUT: {(True, False), 'ALPHA', 123}

# invalid_set = {"ALPHA", 123, [True, False]}
# print(invalid_set)
''' OUTPUT:
Traceback (most recent call last):
  File "/Users/thenickedwards/Desktop/Repos/Nucamp ONPA-SU24-10-02/byte_of_py/18_tuples_sets_data_structures/18_04_sets.py", line 6, in <module>
    invalid_set = {"ALPHA", 123, [True, False]}
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'
'''

set_w_dupe = {"ALPHA", 123, 123}
print(set_w_dupe)
#  OUTPUT: {'ALPHA', 123}
# dupe value removed

# NOT AN EMPTY SET
empty_dictionary = {} 
# set() method required to make emty set
empty_set = set()
print(empty_set)
# OUTPUT: set()
