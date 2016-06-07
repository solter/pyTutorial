#!/usr/bin/env python3

"""
This module finds the intersection of 2 functions using
the bisection method.

This is not the most efficient implementation, but should
demonstrate the basic idea.

For the plotting, see
http://matplotlib.org/users/gridspec.html
for the gridspec examples, and see
http://matplotlib.org/1.4.3/api/pyplot_summary.html
for a list of all the plotting functions

This utilizes lambda functions.
Lambda functions are special functions which are defined inline rather
by thier own code block. They are specified as
lambda <variable list> : <expression to return>,
which can be assigned to a variable which will now act as:

def <variable>(<variable list>):
    return <expression to return>

Seee line 53
"""

import numpy as np

def intersect(f, g, x0, tol=.001, plot=False):
    """
    This is the actual algorithm to perform the bisection.

    inputs:
        f - function -
            this should be a function that takes 1 number and returns a number
        g - function -
            this should be a function that takes 1 number and returns a number
        x0 - float -
            this should be the value for a first guess at when f and g intersect

    optional inputs:
        tol=.01 - float -
            The tolerance. The actual root will fall between
            (output - .5*tol, output + .5*tol)
        plot=False - boolean -
            A boolean indicating whether we want to plot every
            step or not. If true, produces plots
    """

    # Define a new function named delta.
    # This will output the difference f(x) - g(x).
    delta = lambda x: f(x) - g(x)
    # This is equivalent to the following definition
    #def delta(x):
    #   return f(x) - g(x)

    # if delta(x0 - .5*tol) is on the opposite side of the intersection
    # as delta(x0 + .5*tol), the intersection MUST fall between x0-.5*tol
    # and x0 + .5*tol, so x0 is a solution
    if( ( delta(x0 - .5*tol ) <= 0) != ( delta(x0 + .5*tol) <= 0 ) ):
        # If x0 is a solution, return
        return x0

    # if x0 is not a solution, form a bracket which right now is
    # x0 to x0
    bnd = [x0, x0]

    # Expand our brackets until delta(bnd[0]) and
    # delta(bnd[1]) are on opposite sides of the intersection,
    # meaning that a the intersection falls between bnd[0] and bnd[1]
    step_size = 10*tol
    while( ( delta(bnd[0]) <= 0 ) == ( delta(bnd[1]) <= 0) ):
        # move bnd[0] backwards
        bnd[0] -= step_size
        # move bnd[1] forwards
        bnd[1] += step_size
        # increase the step size for the next iteration.
        # this prevents taking tiny steps if we need large steps
        step_size *= 1.2

    # We now know that our bounds lie on opposite sides of 0,
    # so we can shrink our bounds, guaranteeing that they remain
    # on opposite sides of the intersection. Thus our terminating condition
    # is when bnd[1] - bnd[0] < tol, since this implies that the
    # equal point lies in between bnd[0] and bnd[1] which has less
    # than tol room to wiggle.
    while bnd[1] - bnd[0] > tol: # while there is too much wiggle room
        test_bnd = .5*sum(bnd) # take the average position

        # check to see if we hit the intersection on the head
        dtb = delta(test_bnd)
        if dtb == 0:
            # if we hit the the intersection exactly, return it.
            # Return will escape the function and return the value
            return test_bnd

        # replace the bnd on the same side with test_bnd, so the bnd's get closer
        if( ( dtb <= 0 ) == ( delta(bnd[0]) <= 0 ) ):
            # if the both fall on the same size of the intersection, replace bnd[0]
            bnd[0] = test_bnd
        else:
            # since test_bnd didn't fall on the same side of the intersection as bnd[0]
            # it must fall on the same side as bnd[1],
            # so replace it
            bnd[1] = test_bnd

    # At this point, we know that bnd[1] and bnd[0] lie on opposite sides of the intersection
    # and bnd[1] - bnd[0] < tol, so the corerect answer is guaranteed to fall within .5*tol of
    # .5*(bnd[1] + bnd[0])
    return .5*sum(bnd)

def testTanExp():
    """
    This tests the bisection method using
    the tangent and 1.2**x as functions.
    
    The result is printed to the screen, and the
    algorithm is plotted.
    """
    f = np.tan
    f = np.tan
    g = lambda x: 1.2**x
    x = intersect(f, g, .73, plot=True)
    delta = lambda x: f(x) - g(x)
    print('intersection = {:f}\nf(x) - g(x) = {:f}'.format(x, delta(x)))
    print('delta(x+tol) = {}, delta(x-tol) = {}'.format(delta(x+.01), delta(x-.01)))

if __name__ == '__main__':
    testTanExp()
