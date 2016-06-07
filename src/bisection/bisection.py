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
"""

import numpy as np
import matplotlib
# This is to make matplotlib ONLY print good png's. Cannot print to screen.
# See http://matplotlib.org/faq/usage_faq.html#what-is-a-backend
matplotlib.use('Agg')
# This is the conventional way to import the plotting module
import matplotlib.pyplot as plt
# This will allow us to create a fancy layout
import matplotlib.gridspec as gs

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
    if plot:
        # define a new figure 11in w x 8 in t
        plt.figure(figsize=(11, 8))
        # define a 2x2 grid to lay plots on
        mygrid = gs.GridSpec(2, 2)

        # define an axis in bottom left corner to hold the function plot
        funcplot = plt.subplot(mygrid[1, 0])
        # define an axis in bottom right corner to hold the delta plot
        dplot = plt.subplot(mygrid[1, 1])
        # define an axis spanning the entire top to hold to algorithm plot
        alplot = plt.subplot(mygrid[0, :])

    # Define a new function named delta
    # This will output the difference f(x) - g(x)
    delta = lambda x: f(x) - g(x)

    if plot:
        # define the x range we are going to plot on all plots
        # a list of 100 values evenly spaced between x0-1 and x0+1
        x_vals = np.linspace(x0-1, x0+1, 100)

        # define the functions to plot
        f_vals = [f(x) for x in x_vals]
        g_vals = [g(x) for x in x_vals]
        delta_vals = [delta(x) for x in x_vals]

        ## plot the f and g functions on the funcplot

        # make the f function green, with a solid line, and a figure legend f(x)
        funcplot.plot(x_vals, f_vals, 'g-', label='f(x)')

        # make the g function red, with a solid line, and a figure legend g(x),
        # over the top of the f_plot
        funcplot.plot(x_vals, g_vals, 'r-', label='g(x)')

        # Define the axes labels
        funcplot.set_xlabel('x')
        funcplot.set_ylabel('y')
        # Define the horizontal and vertical limits
        funcplot.set_xlim([x0-.5, x0+.5])
        funcplot.set_ylim([-2, 2])
        # Create the grid
        funcplot.grid(True, which='major', linestyle='-', color='darkgrey')
        funcplot.axhline(0, linestyle='-', color='k')

        ## plot the delta function on the deltaplot, along with the initial guess

        # plot the delta function with a solid blue line
        dplot.plot(x_vals, delta_vals, linestyle='-', color='purple')

        # plot a black vertical line at the initial guess
        dplot.axvline(x0, color='dodgerblue')

        # Define the axes labels
        dplot.set_xlabel('x')
        dplot.set_ylabel('y')
        # Define the horizontal and vertical limits
        dplot.set_xlim([x0-.5, x0+.5])
        dplot.set_ylim([-2, 2])
        # Turn on the grid
        dplot.grid(True, which='major', linestyle='-', color='darkgrey')
        dplot.axhline(0, linestyle='-', color='k')

        ## plot the delta function on the alplot with a solid blue line
        alplot.plot(x_vals, delta_vals, linestyle='-', color='purple', label='f(x) - g(x)')

        # Define the axes labels
        alplot.set_xlabel('x')
        alplot.set_ylabel('y')
        # Define the horizontal and vertical limits
        alplot.set_ylim([-2, 2])
        # Turn on the grid
        alplot.grid(True)
        alplot.grid(True, which='major', linestyle='-', color='darkgrey')
        alplot.axhline(0, linestyle='-', color='k')

    # if delta(x0 - .5*tol) is on the opposite side of the intersection
    # as delta(x0 + .5*tol), the intersection MUST fall between x0-.5*tol
    # and x0 + .5*tol, so x0 is a solution
    if( ( delta(x0 - .5*tol ) <= 0) != ( delta(x0 + .5*tol) <= 0 ) ):

        # finalize the plots by adding legends, and saving the figure
        if plot:
            # Add legends. Only plots with labels will be added to the legend.
            funcplot.legend()
            alplot.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode='expand')
            plt.savefig('bisection.png')

        # If x0 is a solution, return
        return x0

    # if x0 is not a solution, form a bracket which right now is
    # x0 to x0
    bnd = [x0, x0]

    # add the initial expansion lines, with labels, to alplot. Also set the xlim
    if plot:
        alplot.axvline(bnd[0], color='blue', linestyle='-.', label='left expansion')
        alplot.axvline(bnd[1], color='brown', linestyle='-.', label='right expansion')

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

        # add the expansion lines, without labels, to alplot
        if plot:
            alplot.axvline(bnd[0], color='blue', linestyle='-.')
            alplot.axvline(bnd[1], color='brown', linestyle='-.')

    # add the initial homing lines, with labels, to alplot
    if plot:
        alplot.axvline(bnd[0], color='dodgerblue', linestyle='-', label='left homing')
        alplot.axvline(bnd[1], color='red', linestyle='-', label='right homing')
        alplot.set_xlim([bnd[0]-.1, bnd[1]+.1])

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
            # finalize the plots by adding legends, and saving the figure
            if plot:
                # Add legends. Only plots with labels will be added to the legend.
                funcplot.legend()
                alplot.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode='expand')
                plt.savefig('bisection.png')
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

        # add the homing lines, without labels, to alplot
        if plot:
            alplot.axvline(bnd[0], color='dodgerblue', linestyle='-')
            alplot.axvline(bnd[1], color='red', linestyle='-')

    # finalize the plots by adding legends, and saving the figure
    if plot:
        # Add legends. Only plots with labels will be added to the legend.
        funcplot.legend()
        alplot.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode='expand')
        plt.savefig('bisection.png')
    # At this point, we know that bnd[1] and bnd[0] lie on opposite sides of the intersection
    # and bnd[1] - bnd[0] < tol, so the corerect answer is guaranteed to fall within .5*tol of
    # .5*(bnd[1] + bnd[0])
    return .5*sum(bnd)

if __name__ == '__main__':
    f = np.tan
    g = lambda x: 1.2**x
    x = intersect(f, g, .73, plot=True)
    delta = lambda x: f(x) - g(x)
    print('intersection = {:f}\nf(x) - g(x) = {:f}'.format(x, delta(x)))
    print('delta(x+tol) = {}, delta(x-tol) = {}'.format(delta(x+.01), delta(x-.01)))
