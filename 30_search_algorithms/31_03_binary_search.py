'''
Binary Search
    - divide and Conquer
    - repeatedly divides search interval in half until target is found
'''
list1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
# there is a native method to see if value is in a list but this is for practice

def binary_search(the_list, target):
    lower_bound = 0                     # 0 index
    upper_bound = len(the_list) - 1     # -1 index
    
    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]
        
        if pivot_value == target:
            print(f"Got it! Found {pivot_value} at index {the_list.index(pivot_value)}")
            return pivot
        if pivot_value > target:
            upper_bound = pivot - 1
        else:
            lower_bound = pivot + 1
    print(f"Can't find {target} in this list.")
    return -1

##########

binary_search(list1, 30)    # Got it! Found 30 at index 5
binary_search(list1, 100)   # Can't find 100 in this list.
binary_search(list1, 1)     # Can't find 1 in this list.
binary_search(list1, 42)    # Can't find 42 in this list.
binary_search(list1, 70)    # Got it! Found 70 at index 13