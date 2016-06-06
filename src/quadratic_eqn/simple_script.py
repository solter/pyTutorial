#!/usr/bin/env python3

"""
This is a multiline comment.
Python ignores the entire section between the triple quotes.

These type of comments are commonly used for documentation (docstrings).

You should include 1 docstring at the top of all python modules describing what
the module does.

here is the docstring for this file:
This module defines the coeffecients to the quadratic equation,
variables that find the roots of the equation, and displays the results.
"""

# import statements define the outside module for use.
# numpy is a numerical python package with lots of useful
# numerical functions defined. It is common to rename the
# package as the variable 'np', so to use it we can just call
# 'np.func' rather than 'numpy.func'. 
import numpy as np

# Store the coeffiecients a,b, and c
a = 2.1
b = 5.4
c = 1.2

# define temporary variables for convenience
disc = np.sqrt(b**2 - 4*a*c) # b**2 is b to the power of 2, or b^2 

# Define the first root using the quadratic formula.
root1 = (-b + disc) / (2*a)

# For the second root, define it in 2 parts.
# First define the numerator
root2 = -b - disc
# Then divide the variable by the denominator using an augmented assignment statement
root2 /= 2*a # equivalent to root2 = root2/(2*a)

quad_at_root1 = a * root1**2 + b * root1 + c
quad_at_root2 = a * root2**2 + b * root2 + c

print("The quadratic equation is:")
print("{:f} * x^2 + {:f} x + {:f}".format(a,b,c))
print("  = {:.2f} * x^2 + {:.2f} x + {:.2f}".format(a,b,c))# only printing 2 places after the decimal
print()
print("The positive root is {:f}".format(root1))
# The \n tells python to jump to the next line.
print("subsituting the positive root into the equation gives:\n  {:f}".format(quad_at_root1))
print()
print("The negative root is {:f}".format(root2))
print("subsituting the negative root into the equation gives:\n  {:f}".format(quad_at_root2))
