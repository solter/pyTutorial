#!/usr/bin/env python3
"""
This module contains a class which
allows for the definition of a quadratic equation,
with solution methods built into the class.

It also shows how to throw an exception for bad inputs
"""

import numpy as np

# The following is a class.
# A class is a container that stores data,
# and can have its own functions. These functions
# will ALWAYS be called with the class object as the first
# argument. Typically this argument is called self.
class quadratic_Equation:
    """
    This class allows the definition of a quadratic equation.
    It also contains methods to find the roots of the equation
    """

    # Methods inside classes can come in 2 flavors,
    # regulare methods and magic methods. Magic methods
    # begin with a dunder (double underscore, __).
    # For a good guide to the magic methods and what they
    # do, see http://www.rafekettler.com/magicmethods.html
    #
    # This first argument to all functions is the class itself,
    # convention is to name this variable 'self'

    def __init__(self, a, b, c):
        """
        This is the initializer (called a constructor in other languages).
        This method is called whenever a new object of quadratic_Equation
        type is instantiated (created).

        3 inputs are required, a, b, and c - the coefficients of a quadratic equation.
        Python takes care of providing the class to the method in the self variable
        """
        # Store the input a, b, and c in variables attached to the object.
        # These variables remain stuck to the object that was instantiated
        # Variables and methods of this class are accessed via calling <object>.<var/func name>
        self.a = a
        self.b = b
        self.c = c


    def evaluate(self, x):
        """
        This function evaluates the quadratic equation at x
        """
        return self.a * x**2 + self.b * x + self.c

    def __call__(self, x):
        """
        This magic method allows the user to call the object as a
        function. When you call the object, this specifies that
        you must provide it 1 variable, x.

        It then evaluates the function at x.
        """
        # invoke this object's evaluate method and return its output
        return self.evaluate(x)

    def root(self, positive=True):
        """
        This function finds the root of a the quadratic equation.

        optional inputs:
            positive = True -- if True, returns the positive root.
                               if False, returns the negative root.

        This function raises an exception if both roots are imaginary.
        """
        disc2 = self.b**2 - 4*self.a*self.c

        # If the discriminant is <0 (so only imaginary roots),
        # raise a new exception. This will terminate the program
        # and cascade up to the caller unless caught by a try...except
        # statement.
        if disc2 < 0:
            raise QuadException(msg='No real roots exist')

        if positive:
            root = -self.b + np.sqrt(disc2)
        else:
            root = -self.b - np.sqrt(disc2)

        root /= 2*self.a

        return root

    def __str__(self):
        """
        This magic method tells python how to display
        this class when asked to print it. No need to format
        it explicitly yourself every time you want to examine it.
        """
        toret = "The quadratic equation is:\n"
        # The format statement can be used on any string, as
        # it is here. Furthermore, line breaks are fine IF
        # they are buried inside a set of ().
        # Also, adding strings is equivalent to appending
        # the second string to the first
        toret += "{:.2f} * x^2 + {:.2f} * x + {:.2f}".format(
                self.a, self.b, self.c)
        return toret

# The following shows how to define a class
# which is a subclass of the built in exception class.
# A subclass contains all the methods of Exception,
# and anywhere an Exception is needed QuadException will
# suffice
#
# See https://docs.python.org/3/tutorial/errors.html for a
# complete understanding of how exceptions and exception handling works.
class QuadException(Exception):
    """
    An exception used by the quadratic_Equation class
    """
    def __init__(self, msg=""):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)

# When a python script is called, python gives it
# a __name__ of __main__. By adding this if block,
# python only bothers to execute IF it is called
# directly from the command line
if __name__ == '__main__':
    q1 = quadratic_Equation(2.1, 5.4, 1.2)

    print(q1)# print the string representation of q1
    print()

    # The following 2 statements do the same thing
    quad_at_root1 = q1.evaluate(q1.root())
    quad_at_root1 = q1(q1.root())

    quad_at_root2 = q1(q1.root(False))

    print( "The positive root is {:f}".format( q1.root() ) )
    print( "subsituting the positive root into the equation gives:")
    print("  {:f}".format(quad_at_root1) )
    print()
    print( "The positive root is {:f}".format( q1.root() ) )
    print( "subsituting the positive root into the equation gives:")
    print("  {:f}".format(quad_at_root2) )

    # This changes b to .02
    q1.b = .02
    
    print(q1)# print the string representation of q1
    print()

    # But now only imaginary roots exist, so the following
    # will throw the exception
    q1.root()
