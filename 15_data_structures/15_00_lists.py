strings_list = ["nick", "nako", "murph", "rob", "avw", "doug"]

my_tuple = ("apple", "banana", "cherry") 
my_set = {"apple", "banana", "cherry", "apple"}

# LIST = ordered sequence of multiple values, 0-indexed
my_list = [
            "n",                                        # string
            5,                                          # int
            9.17,                                       # float
            ["list", "nested"],                         # nested list
            {"id": 1234},                               # dictionary
            ("apple", "banana", "cherry"),              # tuple
            {"apple", "banana", "cherry", "apple",},    # set
            strings_list, my_tuple, my_set              # variables
        ]

# braket notation
print(my_list[0])   # n
print(my_list[3])   # ["list", "nested"]