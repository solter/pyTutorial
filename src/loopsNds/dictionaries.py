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

# To import just 1 class or function from a module,
# you can use the from <module> import <class>
#
# In this case we are importing the function pprint
# from the pprint module. This function allows us to
# print the data structures in a more readable format than
# the default print statement
from pprint import pprint 

# This defines an empty dictionary
a = {} 

# Dictionaries use keys to access elements rather than integer indices
# Elements can be anything

# assign a series of items to a, using numbers and strings as keys
a['key1'] = 'string key'
a[15]     = 'integer key'
a[26.25]  = 'float key'

pprint(a)

# Any immutable object can be a key - such as tuples
a[(1,2,3)] = 'tuple key'
pprint(a)

# Lists and dictionaries are mutable, so CANNOT be keys
try:
    a[ [1,2,3] ] = 'list key'
except Exception as e:
    print(e.args)

# Values in dictionaries can be anything, including lists
a['list'] = [1,2,3]
a['dic']  = {'t':15, (1,2):[4,5,6,'hello']}

pprint(a)

# The length of a dictionary is the number of keys it has
print(len(a))

# You can overwrite keys, and the key remains unique
pprint(a)
a[15] = 'updated integer key'
pprint(a)

# you can test if a key is in a dictionary using the in keyword
print(15 in a)
print(16 in a)

# You can get a list of keys or values using the dictionary functions keys() and values()
pprint(a.keys())
pprint(a.values())

# You can get a list of key, value pairs using the items keyword
pprint(a.items())
