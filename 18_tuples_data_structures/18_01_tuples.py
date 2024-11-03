# Tuple (collection of values which is ordered and immutable, 0-indexed, all data types accepted, values do not need to be uniqu)

zoo_doo_animals = ("rhino", "zebra", "hippo", "tiger")
zoo_doo_animals_alt = "rhino", "zebra", "hippo", "tiger"    
# parentheses not required (when not empty) but recomended

empty_tuple = ()
empty_tuple2 = tuple()              # same
print("empty_tuple", empty_tuple)
print(type(empty_tuple))

one_item_tuple= ("lion",)   
# note: trailing comma required

# immutable (cannot be changed) but values can be updated
# e.g. the 2nd declaration of zoo_animals "creates" a new tuple by updating the value of the varaiable
zoo_animals = ("ape", "zebra", "penguin")
zoo_animals = ("elk", "giraffe", "condor")
# you cannot modify the tuple
# e.g. these would error:
'''
zoo_animals[0] = "brontosaurus"     # cannot change value
zoo_animals.pop(1)                  # cannot apply methods to change value
'''
