'''
Linear Search
    - search for an item linearly, one after another
    - will always work whether items sorted or unsorted
    - slows as number of items increase in data set
    - useful for small unsorted data sets, otherwise very inefficient
'''
list1 = [1, 7, 5, 4, 10]
list2 = [1, 7, 2, 4, 5]
list3 = [1, 7, 2, 4, 10]
# there is a native method to see if value is in a list but this is for practice

def linear_search(list):
    for v in list:
        if v == 5:
            print("Yes, the value is in this list!")
            break
        elif list.index(v) == len(list) - 1:
            print("The value 5 is not in this list.")
            break
        else:
            continue

##########

linear_search(list1)    # Yes, the value is in this list!
linear_search(list2)    # Yes, the value is in this list!
linear_search(list3)    # The value 5 is not in this list.
