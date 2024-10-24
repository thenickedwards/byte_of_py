# similar to arrow functions in JavaScript
# known as anonymous functions (they do not have a name)
# e.g.
# lambda arg1, arg2: expression to return

lambda num: num ** 2
# same as named function below
def square(num):
    return num ** 2

###

def callback_func(arg):
    return arg ** 2

# higher order function accepts function as argument
def a_function(callback_func):
    print(callback_func(3))

# higher order function w/ lambda
a_function(lambda num : num ** 2)   # output: 9
