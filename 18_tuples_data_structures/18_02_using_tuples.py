my_tuple = (1, 2, 3, 4, 5)

# Access tuple values
print(my_tuple[0] + my_tuple[1])
#  1 + 2
'''OUTPUT: 3'''

print(my_tuple[1] + my_tuple[-2])
# 2 + 4
'''OUTPUT: 6'''

print(my_tuple[-1] + my_tuple[-2])
# 5 + 4
'''OUTPUT: 9'''

# Modify tuple values
# my_tuple[3] = 1
''' OUTPUT:
Traceback (most recent call last):
  File "/Users/thenickedwards/Desktop/Repos/Nucamp ONPA-SU24-10-02/byte_of_py/18_tuples_sets_data_structures/18_02_using_tuples.py", line 17, in <module>
    my_tuple[3] = 1
    ~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''

# re-assign the value of the variable
my_tuple = (5, 4, 3, 2, 1) 
print(my_tuple)
''' OUTPUT: (5, 4, 3, 2, 1)'''