'''
Bubble Sort
    - takes unordered list and orders it
    - traverses from front to end repeatedly
    - larger values "bubble" to end of list
    - considered brute force technique
'''

unsorted_list = [101, 49, 3, 12, 56]


def bubblesort(the_list):
    high_idx = len(the_list) - 1
    for i in range(high_idx):
        for j in range(high_idx):
            item = the_list[j]
            next = the_list[j+1]
            if item > next:
                the_list[j] = next
                the_list[j+1] = item
            print(the_list, i, j)
            
def bubblesort2(the_list):
    swaps = 0
    print(the_list, 0, 0, swaps)
    high_idx = len(the_list) - 1
    for i in range(high_idx):
        for j in range(high_idx):
            item = the_list[j]
            next = the_list[j+1]
            if item > next:
                the_list[j] = next
                the_list[j+1] = item
                swaps += 1
            print(the_list, i, j, swaps)