'''
Quicksort
    - one of the most efficient ways to sort an unordered list (uses divide and conquer technique)
    - pivot is chosen (rather then always half like in binary search)
    - values less than pivot go below pivot
    - values greater than pivot go above pivot
    - pivot chosen for each sublist, repeat recursively until list is sorted  
'''

my_list = [5, 4, 1, 2, 3]
swaps = 0

def sort_part(the_list, low_idx, pivot_idx):
    global swaps
    pivot_val = the_list[pivot_idx]

    while pivot_idx != low_idx:
        low_val = the_list[low_idx]

        print(the_list, low_val, pivot_val, swaps)
        if low_val <= pivot_val:
            low_idx += 1
        else:
            the_list[low_idx] = the_list[pivot_idx-1]
            the_list[pivot_idx] = low_val
            the_list[pivot_idx-1] = pivot_val
            pivot_idx -= 1
            swaps += 1

    return pivot_idx

def quicksort(the_list, low_idx, high_idx):
    if low_idx > high_idx:
        return

    pivot_idx = sort_part(the_list, low_idx, high_idx)
    quicksort(the_list, low_idx, pivot_idx-1)
    quicksort(the_list, pivot_idx+1, high_idx)



#####     DRIVER CODE     #####
quicksort(my_list, 0, len(my_list)-1)
print("my_list:", my_list)