def linear_search_dictionary(the_dict, target):
    for x in the_dict:
        if the_dict[f'{x}'] == target:
            print("Found at index", x)
            return x
    print("Target is not in the list")
    return -1

##########

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)