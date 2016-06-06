#!/usr/bin/env python3
"""
This module solves a quadratic equation using
a series of functions
"""

import numpy as np

a = 2.1
b = 5.4
c = 1.2

# Following is a function.
# Functions take inputs, and produce output(s).
# The outputs are specified at the end with a return statement (this encompasses returning no variables as well).
# They are defined using the following syntax:
# def your_function_name(name_of_input_1, name_of_input_2, ...):
#
# They execute all the commands within the definition.
# In python, definitions last for as long as the next command
# remains indented. The first non-indented command ends the definition.
#
# All variables defined within the definition or within the function
# are no longer defined outside of the function.
# This is called the 'scope' of the variable.
# In python, the scope of a variable is everything at the same or
# deeper indentation level as where the variable is defined*. Once
# a variable is out of scope, it no longer exists.
# If the same variable name is used in multiple scopes, the
# variable with the least scope (defined at the largest indent level) is
# the one used.
#
# * this holds for functions and classes, but not if statements.
#   see https://docs.python.org/3/tutorial/classes.html for the full
#   set of scope rules
def positiveRoot(a,b,c):
    """
    This is a function docstring. It should immediately follow
    the definition line.

    This function takes the coefficients of a quadratic equation and
    calculates the positive root.
    """
    # The discriminant
    disc = np.sqrt(b**2 - 4*a*c)
    root1 = (-b + disc) / (2*a)
    # This tells python to return the root1 value when the positive_root function is called
    return root1

def negativeRoot(a,b,c):
    """
    This function takes the coefficients of a quadratic equation and
    calculates the negative root.
    """
    # The discriminant
    disc = np.sqrt(b**2 - 4*a*c)
    root2 = (-b - disc) / (2*a)
    # This tells python to return the root2 value when the positive_root function is called
    return root2

def evalQuad(a,b,c,x):
    """
    This function evaluates the quadratic equation
    a * x**2 + b*x + c
    """
    return a * x**2 + b*x + c

# This line calls eval quad, with x replaced by 
# the output of the positive_root function
quad_at_root1 = evalQuad(a,b,c, positive_root(a,b,c))
quad_at_root2 = evalQuad(a,b,c, negative_root(a,b,c))

print("The quadratic equation is:")
print("{:f} * x^2 + {:f} x + {:f}".format(a,b,c))
print("  = {:.2f} * x^2 + {:.2f} x + {:.2f}".format(a,b,c))# only printing 2 places after the decimal
print()
print("The positive root is {:f}".format(positiveRoot(a,b,c)))
print("subsituting the positive root into the equation gives:\n  {:f}".format(quad_at_root1))
print()
print("The negative root is {:f}".format(negativeRoot(a,b,c)))
print("subsituting the negative root into the equation gives:\n  {:f}".format(quad_at_root2))
