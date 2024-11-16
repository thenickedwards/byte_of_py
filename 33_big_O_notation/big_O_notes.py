'''
BIG O NOTATION

Efficiency of algorithm not based on real-time minutes/seconds bc computer speeds can vary drastically.
O = Order of
Analyze algorithms for efficiency by looking at how increasing size of inputs given affects the number of operations or time complexity. (We assume that each operations takes a similar amount of time ∴ more operations = more time)

constant:       O(1)
    - does not depend on input size
    - (e.g. declaring a var, retrieving a value from a list, appending or popping a list)

linear:         O(n)
    - as input grows, number of operations grows proportionally
    - (e.g. iterating every value in a list/string, linear search, creating a list)
    
logarithmic:   O(log₂n)
    - (AKA log time) most efficient after constant time (often shortened to O(log (n)) or O(log n) as base 2 is assumed for cpu
    - (e.g. input is repeatedly partitioned, binary search)
    
linearithmic:   O(n log₂(n))
    - combo of linear and logarithmic
    - depends on input size times the log of input size
    - (e.g. quicksort = repeated division into 2 parts (O = log₂n) + comparison to pivot (O = n))
    
quadratic:      O(n²)
    - least efficient, based on square of input size
    - (e.g. bubble sort)

'''