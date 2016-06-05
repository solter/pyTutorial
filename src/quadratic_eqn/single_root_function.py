#!/usr/bin/env python3

"""
This module contains a quadratic equation solver,
but uses an optional parameter so multiple root functions
do not need to be defined.
"""

import numpy as np

a = 2.1
b = 5.4
c = 1.2

# The following shows how to define optional parameters.
# The last input has a default value of True.
# If a user calls the function with only 3 inputs, the positive
# variable remains True. Users can also call it with a 4th input
# specifying whether positive should be true or false
def root(a,b,c, positive=True):
    """
    This function takes the coefficients of a quadratic equation and
    calculates a root.

    By default, it calculates the positive root. If positive=False,
    it calculates the negative root
    """
    disc = np.sqrt(b**2 - 4*a*c)
    # If statements allow you to do something if a condition is true,
    # otherwise do something else.
    #
    # There is a also a third way of using ifs, namely
    # if (condition):
    #     do stuff
    # elif (another condition):
    #     do other stuff
    # else:
    #     do something completely different
    if positive:
        root = (-b + disc) / (2*a)
    else:
        root = (-b - disc) / (2*a)
    # This tells python to return the root1 value when the positive_root function is called
    return root

def eval_quad(a,b,c,x):
    """
    This function evaluates the quadratic equation
    a * x**2 + b*x + c
    """
    return a * x**2 + b*x + c

# There are 3 ways to get the positive root.
# Two of which are commented out
root1 = root(a,b,c)
#root1 = root(a,b,c,True)
#root1 = root(a,b,c,positive=True)

# There are 2 ways to get the negative root.
# The latter of which is commented out.
root2 = root(a,b,c,False)
#root2 = root(a,b,c,positive=False)

quad_at_root1 = eval_quad(a,b,c, root1)
quad_at_root2 = eval_quad(a,b,c, root2)

print( "The quadratic equation is:" )
print( "{:f} * x^2 + {:f} x + {:f}".format(a,b,c) )
print( "  = {:.2f} * x^2 + {:.2f} x + {:.2f}".format(a,b,c) )# only printing 2 places after the decimal
print(  )
print( "The positive root is {:f}".format(root1) )
print( "subsituting the positive root into the equation gives:\n  {:f}".format(quad_at_root1) )
print(  )
print( "The negative root is {:f}".format(root2) )
print( "subsituting the negative root into the equation gives:\n  {:f}".format(quad_at_root2) )
