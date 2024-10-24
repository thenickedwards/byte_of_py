import my_module

my_module.greet('Albert Einstein')
print ('My fave flave of ice cream is', my_module.flavor)

##### use import below to bring in specifci functions, varibales, etc
# also avoid dot notation :D

from my_module import greet, flavor

greet('Albert Einstein')
print ('My fave flave of ice cream is', flavor)