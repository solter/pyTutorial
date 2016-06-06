#!/usr/bin/env python3

"""
This script is intended to demonstrate the following built in data
structures in python:

    tuples
    lists

This script acts better as a series of commands to enter
into the interactive python interpreter

See https://docs.python.org/3.4/library/stdtypes.html
"""

#### Tuples 

# This is a tuple
a_tuple = (3, 4, 'hello')

# You can access indidual elements of a tuple,
# starting from 0
print(a_tuple[0])
print(a_tuple[1])
print(a_tuple[2]) # the last element

# Tuples CANNOT be modified once created
try:
    a_tuple[0] = 10
except TypeError as te:
    print(te.args) #print the error message

# You can check if a value is in the tuple
print(3 in a_tuple)
print(5 in a_tuple)

# tuples are the default data type if you provide multiple arguments
b_tuple = 5, 6, 'goodbye'
print(b_tuple)

# you can concatenate 2 tuples by using addition
a_plus_b = a_tuple + b_tuple
print(a_plus_b)

# you can duplicate a tuple through multiplication
a_times_3 = a_tuple*3 # = a_tuple + a_tuple + a_tuple
print(a_times_3)

print('slicing')
# you can access a series of tuple items.
# This does NOT include the last index
# Thus this print statement prints
# a_times_3[1] a_times_3[2] a_times_3[3] a_times_3[4]
print(a_times_3[1:5])

# slicing can be more complicated, see python documentation
print(a_times_3[:4:2])

# you can find the length of a tuple using the len command
print('length a = {:d}\nlength of a*3 = {:d}'.format(
                       len(a_tuple), len(a_times_3) )
     )

# you can get the first index of a certain value
print(a_plus_b)
print('first index of 5 is {:d}'.format(a_plus_b.index(5)))

# you can get the min and max - IF all values are comparable
c = (10, 3, 15, 4, -3)
print('max c = {:d}\nmin c = {:d}'.format(max(c), min(c)))
try:
    max(a_tuple)
except Exception as e:
    print(e.args)

### LISTS 

# A list is like a tuple, but can be modified
a_list = [4, 5, 'hello']
print('Lists')
print(a_list)
a_list[0] = 2
print(a_list)

# You can convert back and forth via the list and tuple functions
c_list = list(c)
print('c_list')
print(c_list)
c_tuple = tuple(c_list)
print('c_tuple')
print(c_tuple)

# Since lists are mutable, you can sort them
c_list.sort()
print('sorted c_list')
print(c_list)

# You can also add elements to lists
c_list.append(101)
# or add the elements of another list to the end of the list
c_list += [102]
print(c_list)

# See documentation for a full list of list and tuple methods
