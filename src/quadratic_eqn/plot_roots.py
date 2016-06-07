#!/usr/bin/env python3

"""
This module should introduce you to basic plotting routines
using matplotlib.

We will be plotting quadratic equations since we already
have a module to calculate them.
"""
# Matplotlib is a module with routines to
# plot data and display them on the screen or save them to files.
# The primary plotting module is pyplot, which is conventionally imported
# as plt
import matplotlib.pyplot as plt
import numpy as np

# This is our quadratic_equation class, rename as QE for shortness
from quad_class import quadratic_Equation as QE

def simplePlot(quadEqn, xlim):
    """
    This function will plot a quadratic equation, using
    the quadratic_Equation module.

    inputs:
        quadEqn -- instance of QE --
            the quadratic equation to plot
        xlim -- list of [float, float] or None --
            This will define the limits for which x is plotted.
            If xlim is None, Matplotlib will auto-scale the axis.
    """
    # Enforce that quadEqn MUST be a QE object.
    # The isinstance function checks if the variable is of type QE,
    # and returns true if and only if it is.
    if not isinstance(quadEqn, QE):
        # RuntimeError is a built in exception class
        raise RuntimeError(msg='provided quadEqn is NOT of type QE')

    # Define the x values we are going to plot
    # np.arange is a function similiar to range, except
    # can use floats as well as integers.
    x_vals = np.arange(xlim[0], xlim[1], .01) #go from xlim[0] to xlim[1] in step sizes of .01

    # Define the y values to plot. This should be the value of our quadratic equation at each
    # value of x.
    # NOTE: x_vals and y_vals MUST have the same length to plot
    y_vals = [quadEqn(x) for x in x_vals]
   
    # Create a simple plot
    plt.plot(x_vals, y_vals)

    # Display the plot on the screen
    plt.show()

# We are introducing a new python object called None here.
# In python, None represents that nothing is there.
# So in the following definition we are saying that
# by default ylim will be a nothing.
def plotQE(quadEqn, xlim, ylim=None):
    """
    This function will plot a quadratic equation, using
    the quadratic_Equation module.

    inputs:
        quadEqn -- instance of QE --
            the quadratic equation to plot
        xlim -- list of [float, float] or None --
            This will define the limits for which x is plotted.
            If xlim is None, Matplotlib will auto-scale the axis.
    optional inputs:
        ylim=None -- list of [float, float] or None --
            This will define the limits for which y is plotted.
            If ylim is None, Matplotlib will auto-scale the axis.
    """
    # Ensure quadEqn is of type QE
    if not isinstance(quadEqn, QE):
        raise RuntimeError(msg='provided quadEqn is NOT of type QE')

    # Define the x values to plot
    x_vals = np.arange(xlim[0], xlim[1], .01) #go from xlim[0] to xlim[1] in step sizes of .01

    # Define the y values to plot.
    y_vals = [quadEqn(x) for x in x_vals]
   
    # Plot the function, but make it red, and only plot the actual data points without a line
    plt.plot(x_vals, y_vals, 'ro')

    # Set the plot so it only shows the defined x range
    plt.xlim(xlim)

    # If ylim was provided, set the y limits of the plot
    if ylim is not None:
        plt.ylim(ylim)

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Display the plot on the screen
    plt.show()

def plotRoots(quadEqn, xlim=None, ylim=None):
    """
    This function will plot a quadratic equation,
    along with vertical bars at its roots.

    inputs:
        quadEqn -- instance of QE --
            the quadratic equation to plot
    optional inputs:
        xlim=None -- list of [float, float] or None --
            This will define the limits for which x is plotted.
            If xlim is None, will only plot just beyond the roots of the function.
            If the roots are not real, an Exception will be raised.
        ylim=None -- list of [float, float] or None --
            This will define the limits for which y is plotted.
            If ylim is None, the limits will be chosen to fit the plot tightly.
    """
    # Ensure quadEqn is of type QE
    if not isinstance(quadEqn, QE):
        raise RuntimeError(msg='provided quadEqn is NOT of type QE') 
    # find the roots
    neg_root = quadEqn.root(False)
    pos_root = quadEqn.root(True)

    # if xlim not provided, set just further than the roots as the limits
    if xlim is None:
        # define padding of a tenth of the distance between the roots
        pad = pos_root - neg_root
        pad *= .1

        xlim = [min(neg_root, pos_root) - pad, max(neg_root, pos_root) + pad]

    # Define the x values to plot
    x_vals = np.arange(xlim[0], xlim[1], .01) #go from xlim[0] to xlim[1] in step sizes of .01

    # Define the y values to plot.
    y_vals = [quadEqn(x) for x in x_vals]
   
    # Create a plot of the equation, with a solid red line. Give it a label
    plt.plot(x_vals, y_vals, linestyle='-', color='red', label='Quad. Eqn.')

    # Set the plot so it only shows the defined x range
    plt.xlim(xlim)

    if ylim is not None:
        # If ylim was provided, set the y limits of the plot
        plt.ylim(ylim)
    else:
        # squeeze the y limits to just cover y-values
        plt.ylim([min(y_vals), max(y_vals)])

    # Plot a blue vertical bar at the the negative root, with a label
    plt.axvline(neg_root, color='blue', label='neg. root')
    # Plot a purple vertical bar at the the positive root, with a label
    plt.axvline(pos_root, color='purple', label='pos. root')

    # add a legend to the plot
    plt.legend()

    # add a title to the plot
    plt.title('root plot')

    # display the plot
    plt.show()

def test_plots():
    """
    A simple method to demonstrate the three plotting routines.
    """
    myeqn = QE(.8, 3, -2)
    simplePlot(myeqn, [-5,3])
    plotQE(myeqn, [-5,3])
    plotRoots(myeqn)

if __name__ == '__main__':
    test_plots()


