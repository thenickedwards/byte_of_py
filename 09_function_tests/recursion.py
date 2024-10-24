# find index of Fibonacci sequence
def rFib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return rFib(n-1) + rFib(n-2)

''' TERMINAL IN INTERACTIVE MODE
(byte_of_py) ➜  byte_of_py git:(main) ✗ python -i 09/recursion.py
>>> rFib(5)
5
>>> rFib(13)
233
>>> rFib(7)
13
>>> 
'''