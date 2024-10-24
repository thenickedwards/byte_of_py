# custom function w/o parameters
def myFn():
    print("You have called my function")

# built-in function w/ params
def add(x, y):
    z = x + y
    print(z)

### calling functions above

myFn()
add(2, 3)

### parameters play

add(3, 4)
a = 4
b = 5
add(a, b)