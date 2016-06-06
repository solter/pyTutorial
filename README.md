# pyTutorial
Python tutorial for incoming summer students at ARL:UT 2016

## Basic command line navigation
This is intended for a unix environment (MacOS, Linux).

The command line provides a quick way to navigate through file systems
and run python. 
Open up a 'Terminal' - this should be a program available on your system.

To run a command, type the command and hit enter.
In the following comment, commands are prefaced by a `$` - you do NOT need this to run the
command (usually the shell starts every line with `<username>@<machine>$` - this is
configurable.

Try running the following commands (use 'q' to exit the windows brought up by less and man):
```Shell
$ pwd
$ ls
$ mkdir my_new_directory
$ ls
$ cd my_new_directory
$ pwd
$ echo 'Hello world' > test.txt
$ cp test.txt test2.txt
$ less test.txt
$ less test2.txt
$ man man
$ man ssh
```
This series of commands should have done the following:

1. print the present working directory (`pwd` - where you are in the file system) to the screen.
2. list (`ls`) the files and subdirectories in your current directory (this will probably be your home)
3. makes a new directory (`mkdir`) named 'my_new_directory'
4. Same as 2, but should now include a new directory
5. change the working directory (`cd`) 'my_new_directory'
6. Same as 1. Note that it should now have appended the my_new_directory you just changed into
7. prints (`echo`) 'Hello world' to the screen, but the `> test.txt` dumps the output into the file test.txt
8. copies (`cp`) the test.txt file to a new file called test2.txt
9. opens the file to view (`less`). It is a minimal viewing program that does NOT allow editing of the file.
   Navigate with the arrow keys. Quit/exit by pressing 'q'
10. opens the test2.txt file. Should be identical to the test.txt file opened in 7
11. opens up the manual page (`man`) for the command. This line opens up the manual command for man itself
12. the man page for `ssh`. This is how you can move to using a different machine

Here's a [cheat sheet](https://ubuntudanmark.dk/filer/fwunixref.pdf) for some common linux commands.

## Python
For this demo we will be using python.
This is a fairly user-friendly language that takes care of lots of
overhead behind the scenes (memory management, complex data structures),
and there exist a LOT of packages out there to make the base language more powerful.
For a very in-depth tutorial, see the [official python tutorial](https://docs.python.org/3/tutorial/).

We will be focusing on python3, and the packages NumPy and Matplotlib.
There is also an older version python2 still commonly used, but the syntax
is very similar.

Python is an interpreted language, which means no compilation is necessary before
running it. In fact, you can run it through an interactive console, so each command
is executed directly after you type it.

If you are not there for the live demo, the source files exist
inside the src/ directory which you can execute on your own machine.

To edit python files, here are some common programs:
* *Any text editor* - usually simple, but miss a bunch of useful features (like jump to method...)
* *XCode*(MacOS) - a text editor with syntax highlighting
* *vim* - a command line text editor, available with (nearly) all UNIX installs. Very configurable, but has a bit of a learning curve.
        See [vim python setup](https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/) for one way to configure vim. 
        This is also my favorite, so feel free to ask me for help configuring it.
        It can replace 80+% of the functionality an IDE provides, with sufficient configuration.
        A tutorial comes built in to most unix machines, just launch the `vimtutor`
* *emacs* - a text editor. vim and emacs aficionados enjoy arguing which one is best.
          See [emacs python setup](https://realpython.com/blog/python/emacs-the-best-python-editor/) for an example configuration.
* *Sublime* - this is a text editor with a free trial, but will eventually ask you to buy it (ask your supervisor if you want a copy).
            I've heard good things - but never used it myself.
            See [sublime python setup](https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/) for configuration.
* *eclipse* - a full IDE (integrated design environment), originally designed for java. This is open source (thus free), and contains
            a lot of features to make development easy. There exists a python plugin called pyDev (as well as plugins for many other
            languages). See [python eclipse usage](https://www.ics.uci.edu/~pattis/common/handouts/introtopythonineclipse/), or ask your
            supervisor for help setting it up.

### Editing python code
#### Interactive console
Similar to how bash commands were preceded by a `$`, in the interactive console
in python precedes each command with a `>>>`.
To launch the interactive console, open a terminal and run 'python3'.
Try running the following commands:
```Python
>>> print('Hello World')
>>> a = 2016
>>> a
>>> b = 'My first formatted statement in'
>>> print('{} {:d}!'.format(b,a))
```
This series of command should have done the following:

1. printed the statement 'Hello world' to the screen
2. defined a variable a, storing the numerical value 2016
3. printed the value of a (2016) to the screen
4. defined the variable b, storing the string 'My first formatted statement in'
5. printed the statement 'My first formatted statement in 2016!'

Some quick notes:

* variables can hold anything (strings, numbers, ...) without specifying 
  what it is holding beforehand
* the interactive console makes printing really easy, just typing the variable
  will show what its holding. No need for print statements to examine what's inside
  of a variable
* format statements let you print more complicated statements. What it is printed
  as is defined inside the `{}`. The first item was left unspecified, so python
  did its best (printing a string is pretty straightforward). The second item was
  specified as `{:d}`, which told python to print the contents of a as an integer
  (d stands for integer in print statements)

#### Python modules
A python module is just a text file containing python commands.
The convention is that python files use the extension .py.
Copy the following code into a file name myFirstProg.py:
```Python
#!/usr/bin/env python3

#This is a comment. Python ignores me.

print('Hello World')
a = 2016
a
b = 'My first formatted statement in'
print('{} {:d}!'.format(b,a))
```
To run this file, use the following command in your terminal after saving this file:
```Shell
$ python3 test.py
```
This does the same thing the interactive console does, except does NOT print a.
All print statements will write their output to the screen.

> NOTE:
> You can also run this directly from the terminal without calling python,
> But first you have to tell your machine that it is safe to execute this file.
> To enable execution, use the command (look it up via `$ man chmod`):
```Shell
$ chmod +x test.py
```
> (This only needs to happen once. Afterwards the machine knows it can execute the file.)
> Then execute the file using
```Shell
$ ./test.py
```

```
NOTE: The first line in the file,
#!/usr/bin/env python3
is a special type of comment that must go before any code (but can be after comments). 
Lines beginning with `#!` are called a shebang, and the terminal 
you are in reads this and knows to launch this file as a python3 script.
(technically your shell is doing the heavy lifting. The terminal is just the screen
interface to the shell. Google "bash shell" for a description of the standard shell) 
```

### Roots of a quadratic equation
This is a series of examples which should illustrate the following:
* Basic python syntax [[full python tutorial](https://docs.python.org/3/tutorial/index.html)]
* python functions
* python classes
* print statements
* python Exceptions and handling them

For this series of examples, navigate into the src/quadratic_eqn directory.

Execute simple_script.py.
Open up the source file and make sure you understand it.
You should have a basic grasp on the following (links to extensive python documentation provided to the right)
* importing external packages [[python modules](https://docs.python.org/3/tutorial/modules.html)]
* defining variables using `=` 
* updating variables using `/=` [[python statements](https://docs.python.org/3/reference/simple_stmts.html)]
* arithmetic expressions `+,-,*,/,**`
* print statements [[python format statements](https://docs.python.org/3/library/string.html#formatstrings), [python print](https://docs.python.org/3.4/library/functions.html#print)]

Now execute the solve_via_function.py script.
The output should be identical as before.
Open up the source file and make sure you understand it.
You should have a *basic* grasp on the following:
* functions [[python functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)]
* scope [[formal scope rules](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)]

Now execute the single_root_function.py script
The output should be identical as before.
Open up the source file and make sure you understand it.
You should have a basic grasp on the following:
* optional variables within python functions
* if...elif...else statements

To understand the quad_class.py module, we are going to explore it
through the interpreter.
Open up the interpreter and enter the following command:
```Python
>>> import quad_class as qc
```
This imports the module quad_class (note that this is the filename without the .py extension),
and names it qc for future use.
Try reading the docstrings for the module and quadrateic_Equation class by using the built in
help command:
```Python
>>> help(qc)
>>> help(qc.quadratic_Equation)
```
The help function pulls up the docstring, as well as the method signature.
This is one reason why docstrings should be included with ALL modules, functions and classes.

We can solve the quadratic equation via the following commands:
```Python
>>> q1 = qc.quadratic_Equation(2.1, 5.4, 1.2)
>>> print(q1)
>>> root1 = q1.root()
>>> root2 = q1.root(False)
>>> print('q1 at root1 = q1({:.2f}) is {:f}'.format(root1, q1(root1)))
>>> print('q1 at root2 = q1({:.2f}) is {:f}'.format(root2, q1(root1)))
```
The first line defines a new quadratic equation, and the first print statement
prints the q1 function (by internally calling the q1.__str__ function).

We can modify our quadratic equation. Try changing b to .01 and finding a root
via the following commands:
```Python
>>> q1.b = .02
>>> print(q1)
>>> root1 = q1.root()
```
The print statement indicates we successfully changed q1.
But the root statement throws an exception because the roots are imaginary.

Now open up the quad_class.py file and examine the source code that made all this
happen. Note that when it was imported, it was not the main program,
so the last section did NOT execute.
You should now have a *basic* grasp on the following:
* classes [[python classes](https://docs.python.org/3/tutorial/classes.html)]
* defining your own Exceptions [[user-defined exceptions](https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions)]
* magic methods within classes [[python magic methods](http://www.rafekettler.com/magicmethods.html)]

If you were accessing this within another module, you probably don't want
your program to fail when an exception is raised. Python provides the following construct
for this:
```Python
# Do some stuff
...

try:
    # What you want to do
    ...
except QuadException as qe:
    # What you want to do when this error is thrown
    # Will ONLY catch QuadException types of exceptions,
    # and store the exception as qe
    print(qe)
    ...

# Do more stuff
...
```
It is possible to catch all exceptions by specifying `except` or `except Exception as e`,
but this is bad practice. For a more in-depth treatment of exceptions and 
exception handling see [python exceptions](https://docs.python.org/3/tutorial/errors.html).

### Loops and Data Structures
This section should introduce you to the following:
* Basic python data structures
   * Tuples and Lists
   * Dictionaries
   * NumPy arrays 
* Control flow
   * if statements and boolean expressions
   * for loops (looping through a list)
   * while loops (looping until a condition is met)
* Reading and Writing to files
   * Using basic python IO functions
   * Using standard file types json and pickles
   * Using NumPy text reader

For this set of topics, please refer to the files inside src/loopsNds/.
These files are extended versions of the information below, with comments providing
the guide. The following table describes the content and lists references for each file/topic:

| file          | content                           | references |
| ---           | ---                               | ---        |
| tuplesNlists  | tuples and lists                  | [standard types](https://docs.python.org/3.4/library/stdtypes.html)|
| dictionaries  | dictionaries                      | [standard types](https://docs.python.org/3.4/library/stdtypes.html)|
| loops         | control structures (ifs and loops)| [[control flow](https://docs.python.org/3/tutorial/controlflow.html), [boolean expr](https://docs.python.org/3/reference/expressions.html#bComparisons), [data structures](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)] |
| numpy_arr     | numpy arrays                      | [Numpy documentation](http://docs.scipy.org/doc/numpy/), start with the User Guide's quickstart |
| fileIO        | file input/output                 | [[io tutorial](https://docs.python.org/3/tutorial/inputoutput.html), [numpy genfromtxt](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.genfromtxt.html)]

#### Tuples and Lists

#### Dictionaries

#### Loops

#### Numpy arrays

#### File Input/Output


### Bisection root-finding method
This example should introduce you to the following:
* Bisection method
* Matplotlib [[Matplotlib api](http://matplotlib.org/1.4.3/api/index.html), [Matplotlib command summary](http://matplotlib.org/1.4.3/api/pyplot_summary.html)]
   * Plotting basic data
   * Labeling your plots
   * Matplotlib axes objects
   * Plotting lines

For this section, navigate to the src/bisection/ directory.
You will see 2 python files, both which you can run.

The bisection_noplot.py file is the basic bisection algorithm.
Open it up, and see if you can figure out how it works.
The big new things are the introduction of lambda functions, and passing functions to a function.
The function passing behaves just like passing any other object (functions are objects in python).
Lambda functions are another way of defining functions which only take 1 line and return.
In this case it made defining the subtraction of functions passed in easy.

Try to understand what all is happening, and why the algorithm works (look at the
old_output.png for a visualization of the algorithm).

The second file is bisection.py. It contains identical code to the noplot file,
except contains a bunch of plot setup and generation.
All the plotting logic is inside of `if plot:` statements, so should be easy
to identify.

Running this file produces the same output to screen, but also
generates a new file (bisection.png). This should match the
old_output.png file.

It is not exactly a basic plot, but should show you some of the power
and finickyness of Matplotlib.

Here are some references:
[lambda expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
[Matplotlib plotting functions](http://matplotlib.org/1.4.3/api/pyplot_summary.html)
[Matplotlib gridspec](http://matplotlib.org/1.4.3/api/pyplot_summary.html)
[Matplotlib backends](http://matplotlib.org/faq/usage_faq.html#what-is-a-backend )

## One last thing
When coding in python, it is easy to just buckle down and create a workable script.
But as important as code that works, is well written code.
Here are some reasons for writing good code:

* So others (including your future self), can come back in 6 months and figure out what you were doing.
* Poor code is MUCH harder to trace down bugs in. and there WILL be bugs - there are always bugs.
* Well written code is easier to pull apart, so the most useful bits can be reused somewhere else by someone else.

There is no 1 definitive answer for what makes good code, but here are some tips

* Docstrings. They should be there.
* Make your code readable. If it is a byzantine monstrosity, there's probably a better way.
* Readability trumps cleverness. If you _can_ do it with a 1-liner, it doesn't mean you _should_.
* Readability (usually) trumps speed. 
* Don't copy/paste large sections of code. If you are doing this, try thinking about how to
  turn it into a loop or a function instead.
* Comment anything you do that is not immediately obvious when looking at the code.
  This does not mean comment every line (usually - although there are times...),
  but every 'paragraph' of code should have a short comment describing what is going on.
  The right amount of comments is a mythical beast, but there _are_ wrong amounts of comments.

To help you write readable code, a good starting point is analyzing your code with [pylint](https://www.pylint.org/).
To try it on the bisection.py code, navigate into the src/bisection/ directory, and run
the command
`pylint3 bisection.py`
This gives you all sorts of recommendations on how to improve your code.
It has a maximum score of 10, but no lower limit. It also should act as a guide, sometimes
its suggestions don't make sense - but usually its a good place to start improving your code.

## End of Tutorial
This concludes the ARL:UT python tutorial.
There are many references above, but here are the three that I find most useful:
[official python tutorial](https://docs.python.org/3/tutorial/)
[numpy documentation](http://docs.scipy.org/doc/numpy/)
[Matplotlib plotting api](http://matplotlib.org/1.4.3/api/pyplot_summary.html)
And of course, [Google](https://www.google.com/).

I also want to point out one more useful website when you have questions:
[Stack Exchange](http://stackexchange.com/)
Typically this is where google ends up directing you (unless it's Matplotlib,
then google as often as not points you to some wierd documentation page).

If you have any questions, start with the above documentation and google.
If those don't suffice within about half an hour, contact your supervisor.
I am also usually available, so feel free to stop by to see if I'm in.
