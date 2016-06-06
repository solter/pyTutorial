#!/usr/bin/env python3

"""
This script is intended to demonstrate how python handles loops and
complex if statements.
The loop types are:
    for loops
    while loops
    list comprehensions

When writing these lines in interactive mode,
for indented blocks hit enter at the end of a newline and
indent the code using spaces.
A blank line terminates the indentation level and thus executes
the block of code.

e.g.
>>> i = 1
>>> while(i < 10):
...   i += 1
...
>>>

See the https://docs.python.org/3/tutorial/controlflow.html page
"""

### If blocks

# define some boolean expressions
a = True
b = True
c = False
d = False

# The most obvious if blocks use boolean expressions.
if a: # if a is true
    print('a is true')


if a and b: # if both a and b are true
    print('a and b are true')

if not a and b: # if (not a) is true and b is true = if a is false and b is true
    print('a false and b true')

# as expressions get longer and more complicated, parenthesis for clarification
# are HIGHLY recommended
if (a and (b or c or d)): # if a is true and (at least one of b, c, d is true)
    print('a and something else is true')

# NOTE: c = d assigns the value of d to c
# c == d returns a boolean indicating whether c and d are the same
if c == d: # if c equals d
    print('c equals d')

if a != d: # if a does not equal d
    print('a does not equal d')

# We can also do something if the expression is not met
if a:
    print('a is true')
else:
    print('a is false')

# We can also check multiple states, and chain them indefinitely
# elif and else statements ONLY exist to ammend if statements
if a and b and c and d: # if they are all true
    print('everything is true')
elif c: # if the above condition is not met, and c is true
    print('c is true')
elif b: # if the above conditions are not met, and b is true
    print('b is true')
else: # if none of the above conditions are met
    print('the above conditions all failed')
    
# NOTE: The 3 if statents below are COMPLETELY DIFFERENT
# from the if elif block above
if a and b and c and d: # if they are all true
    print('everything is true')
if c: # if c is true - DOES NOT DEPEND ON ABOVE CONDITION
    print('c is true')
if b: # if b is true - DOES NOT DEPEND ON ABOVE CONDITIONS
    print('b is true')
else: # this triggers if b is false
    print('b is false')

# For numbers (and anything properly defined, see documentation) we can
# use the <, >, <=, and >= comparisons
a = 1
b = 2
c = 3
d = 4
if a < b and d < c:
    print('a < b and d < c')
elif a <= b and d <= c:
    print('a <= b and d <= c')
elif a <= b < c: # we can also chain comparisons together
    print('a <= b and b < c')
else:
    print('the above conditions fail')

# See https://docs.python.org/3/reference/expressions.html#bComparisons for a complete explanation
# of comparisons

### While loops

# A while loop repeats a set of instructions until the condition is false.
# The condition can be anything that ends in a boolean, just like if blocks.
# The instruction set is enclosed by an indentation block

print('while loop')
i = 1
print(i)
while (i < 10):
    # comments are allowed in indentation blocks

    # as are empty lines
    i *= 2
    print(i)

print(i)

### FOR LOOPS

# For loops will loop through a tuple or list, or you can construct range objects for it to loop through

# A range object is like a slice in a list. It starts at 0 (or the first argument if multiple are given),
# and goes up to (not including) the last value in step sizes of 1 (or the third argument)

print('range tests')
print('range(5)')
for i in range(5):
    print(i)

print('range(2,5)')
for i in range(2,5):
    print(i)

print('range(1,7,2)')
for i in range(1,7,2):
    print(i)

# You can turn a range into a list with the list function
print('list from range')
a = list(range(1,7,2))
print(a)

# we can loop through the list, and manipulate the index
print('modifying loop index')
print(a)
for ele in a:
    # This modifies ele, but NOT the element inside a
    ele += 1
    print(ele)
print(a)

# to modify the value inside a, we can loop through its index range
print('modifying a')
print(a)
for i in range(len(a)):
    a[i] += 1
    print(a[i])
print(a)

# Simple list comprehension
# Instead of using an explicit for loop, we can build a list through
# list comprehensions. They act remarkable similar to for loops.
# The choice of which to use should be decided by readability usually
# There are some gotchas, especially for nested list comprehensions
# See https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions for
# a more thorough description.
print('form b as a**2 using list comprehension')
b = [ele**2 for ele in a]
print('a: {}'.format(a))
print('b: {}'.format(b))

# there are a variety of ways to loop through a dictionary, as below
print('\n\ndictionary loops\n')
d = {'a':1,'b':2,'c':3}
print('the dictionary')
print(d)

print('loop through keys')
for key in d.keys():
    print(key)

print('loop through values')
for val in d.values():
    print(val)

print('loop through key value pairs')
for key, val in d.items():
    print('key: {}, val: {}'.format(key, val))

print('modify the dictionary values')
for key, val in d.items():
    d[key] = val + 1
print(d)
