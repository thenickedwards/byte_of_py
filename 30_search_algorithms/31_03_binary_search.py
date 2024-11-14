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


'''
1. There is a built-in list method in Python that can search a list for an item using a target value. Conduct online research to Provide an example of how you could use it.

The simplest approach to this would be something to the effect of:
3 in [1, 2, 3] # => True
There
matches = filter(expression, lst)
You can also use the filter method, though IMO this is less legible. Note: in Python 2. Here you can see higher-order functions at work. In Python 3, filter doesn't return a list, but a generator-like object.


2. What kind of algorithm technique is used by the Linear Search algorithm? Name the technique and explain why you believe Linear Search fits under this category. 
This would be considered a brute force technique as the algorithm will try all possible solutions until the correct one is found or the search is exhausted. In Linear Search, every element in the list is checked one by one. Like most brute force techinques, yhis approach is straightforward but can be inefficient for large datasets.


3. Conduct online research into other types of search algorithms beyond Linear Search and Binary Search. Choose one and write at least 2-3 or more sentences to briefly describe how it works.
I took a look into memoization and how it functions in dynamic programming.

Dynamic programming is a technique that breaks down complex problems into smaller subproblems, saves the results, and then optimizes the subproblems to find the overall solution. Memoization speeds up recursive algorithms by saving the results of previous calculations. This is done by creating a cache, or memo, for each function that stores the results of its calculations. When the same problem is encountered again, the solution is retrieved from the memo instead of being recalculated. 
'''