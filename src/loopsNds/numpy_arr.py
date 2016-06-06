#!/usr/bin/env python3

"""
This script should show some of the power
of numpy arrays, and demonstrate their usage.

See the numpy documentation for more information
http://docs.scipy.org/doc/numpy/
start with the User Guide's quickstart
"""

import numpy as np

### The numpy array

# Numpy arrays are defined with an initial size, which cannot
# change without redefining the array. Furthermore, all elements
# of an array are of the same type, and must be a number. By
# default, this uses a float (think of a  float as a round rubber tube,
# j.k. its actually how computers store real numbers instead of integers)
# We can start by building an array with each element equal to 1
# it will have 2 dimensions, the first of which is 3 and the second
# of which is 4. Typically, this is thought of as 3 rows with 4 elements
# per row (4 columns), similiar to matrices.
a = np.ones((3,4))
print(a)

# Let us define an array b, and fill it with a multiplication table
b = np.zeros((3,4))
print(b)
# every array has a shape attribute, which stores its shape as tuple
print(b.shape)
for i in range(b.shape[0]):
    for j in range(b.shape[1]):
        # We can access the i row, j column entry using
        # either b[i][j], or b[i,j]
        b[i,j] = i*j
print(b)

# We can perform numerical operations on array, and they happen element-wise.
# So squaring b is equivalent to squaring each element of b
print('a')
print(a)
print('b')
print(b)
print('b**2')
print(b**2)
print('a + b')
print(a+b)
print('a*b')
print(a*b)
print('3*b - 2')
print(3*b - 2)

# Numpy has functions that will work element-wise on arrays
print('sqrt(b)')
print(np.sqrt(b))
print('arctan(b) in degrees')
print(np.rad2deg(np.arctan(b))) 

# arithmetic does NOT work on arrays of different shapes if they both have
# the same dimension

# Turn a on its side
a = a.transpose()
print('a transpose')
print(a)

print('a + b')
try:
    print(a + b)
except Exception as e:
    print(e.args)

# But consider the following 0-dimension array
c = np.zeros((3,))
for i in range(c.shape[0]):
    c[i] = i+1
d = np.zeros((4,))
for i in range(d.shape[0]):
    d[i] = i+5

print('c')
print(c)
print('d')
print(d)

# Numpy will try to do a sensible 'broadcasting' to make arithemetic possible
print('b + c')
try:
    print(b + c)
except Exception as e:
    print(e.args)
print('b + d')
print(b + d)

# BEWARE THE NUMPY BROADCAST. it can be helpful, but also leads to weird bugs that are hard to track down

# We can also tranform numpy arrays to lists, and vice versa

# array to list. This transform preserves the [i][j] indexing
b_list = b.tolist()
print('list b')
print(b_list)

# list to array
c = np.array(b_list)
print('c array = np.array(b_list)')
print(c)

# BEWARE THE LIST/ARRAY CONFUSION. 

# Note the difference between the array times a number and list times a number.
# It is easy to get this mixed up if you transform between these often.
print('b*3')
print(b*3)
print('np.array((list b)*3)')
print(np.array(b_list*3))

# You cannot add a non-list to a list, but you can for an array
print('b + 1')
print(b + 1)
print('(list b) + 1')
try:
    print(b_list + 1)
except Exception as e:
    print(e.args)
