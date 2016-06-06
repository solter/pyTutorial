#!/usr/bin/env python3

"""
This script is intended to demonstrate the following built in data
structures in python:

    dictionaries

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
a_dict = {} 

# This defines a non-empty dictionary
b_dict = {'key_1':'value_1', 'key2':15}

# Dictionaries use 'keys' to access 'values' rather than integer indices.
# Values can be anything.

# assign a series of items to a, using numbers and strings as keys
a_dict['key1'] = 'string key'
a_dict[15]     = 'integer key'
a_dict[26.25]  = 'float key'

pprint(a_dict)

# Any immutable object can be a key - such as tuples
a_dict[(1,2,3)] = 'tuple key'
pprint(a_dict)

# Lists and dictionaries are mutable, so CANNOT be keys
try:
    a_dict[ [1,2,3] ] = 'list key'
except Exception as e:
    print(e.args)

# Values in dictionaries can be anything, including lists
a_dict['list'] = [1,2,3]
a_dict['dic']  = {'t':15, (1,2):[4,5,6,'hello']}

pprint(a_dict)

# The length of a dictionary is the number of keys it has
print(len(a_dict))

# You can overwrite the value stored in a key. But each key remains unique to the dictionary.
pprint(a_dict)
a_dict[15] = 'updated integer key'
pprint(a_dict)

# you can test if a key is in a dictionary using the in keyword
print(15 in a_dict)
print(16 in a_dict)

# You can get a list of keys or values using the dictionary functions keys() and values()
pprint(a_dict.keys())
pprint(a_dict.values())

# You can get a list of key, value pairs using the items keyword
pprint(a_dict.items())
