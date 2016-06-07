the second statement was not true# pyTutorial
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
   Navigate with the arrow keys. Quit/exit by pressing ''q''
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
* *Geany* - An open source ide, with native python support. Uses a fairly old graphics library, so runs on
            pretty much anything. Also designed to have few dependencies and be lightweight. See the [Geany manual](http://www.geany.org/manual/current/index.html)
* *pyCharm* - an ide designed specifically for python. There exists a free version available for download.
              See [PyCharm docs & demos](https://www.jetbrains.com/pycharm/documentation/)
* *Spyder* - an ide originally designed for python. Written in python. Open source, so free.
             See the [Spyder github repo](https://github.com/spyder-ide/spyder)
* This is *not* a complete list of text editors/IDE's that support python. Ask your supervisor if you have
  a hankering for something else.

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

1. printed the statement `Hello world` to the screen
2. defined a variable `a`, storing the numerical value `2016`
3. printed the value of `a` (`2016`) to the screen
4. defined the variable `b`, storing the string `'My first formatted statement in'`
5. printed the statement `'My first formatted statement in 2016!'`

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
This does the same thing the interactive console does, except does NOT print `a`.
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

> NOTE: The first line in the file,
> `#!/usr/bin/env python3`
> is a special type of comment that must go before any code (but can be after comments). 
> Lines beginning with `#!` are called a shebang, and the terminal 
> you are in reads this and knows to launch this file as a python3 script.
> (technically your shell is doing the heavy lifting. The terminal is just the screen
> interface to the shell. Google "bash shell" for a description of the standard shell) 

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

In python, sections of code are defined by the amount lines of code are indented.
Thus after defining a function, all subsequent lines are part of that function as
long as they have 1 more level of indentation than the function definition.
Indentation blocks are also used for if statments, loops, `try...except` blocks, etc.
Typically, indentation blocks are preceded by a line ending in a colon (:).

At ARL:UT the standard is to use 4 spaces per level of indentation.

Now execute the single_root_function.py script
The output should be identical as before.
Open up the source file and make sure you understand it.
You should have a basic grasp on the following:
* optional variables within python functions
* if statements

To understand the quad_class.py module, we are going to explore it
through the interpreter.
Open up the interpreter and enter the following command:
```Python
>>> import quad_class as qc
```
This imports the module quad_class (note that this is the filename without the .py extension),
and names it qc for future use.
Try reading the docstrings for the module and quadratic_Equation class by using the built in
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
*Go check out try...except blocks and the built in exceptions (esp. RuntimeExceptions).*

### Loops and Data Structures
This section should introduce you to the following:
* Basic python data structures
   * Tuples and lists
   * Dictionaries
   * NumPy arrays 
* Control flow
   * If statements and boolean expressions
   * For loops (looping through a list)
   * While loops (looping until a condition is met)
* Reading and writing to files
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
| controlFlow   | control structures (ifs and loops)| [[control flow](https://docs.python.org/3/tutorial/controlflow.html), [boolean expr](https://docs.python.org/3/reference/expressions.html#bComparisons), [data structures](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)] |
| numpy_arr     | numpy arrays                      | [Numpy documentation](http://docs.scipy.org/doc/numpy/), start with the User Guide's quickstart |
| fileIO        | file input/output                 | [[io tutorial](https://docs.python.org/3/tutorial/inputoutput.html), [numpy genfromtxt](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.genfromtxt.html)]

#### Tuples and Lists
See the tuplesNlists.py file for a more comprehensive description of tuples and lists.

##### Tuples
Tuples are a series of data which cannot be modified after creation.
Here is the creation of a tuple:
```Python
>>> a_tuple = (1,2,'hello',7,8,'goodbye')
```
Each element of the tuple can be an arbitrary object.
You can access the elements of tuple as follows:
```Python
>>> a1, a2, a3, a4, a5, a6 = a_tuple
>>> print('{} {}'.format(a1, a2))
>>> b1 = a_tuple[0]
>>> b2 = a_tuple[1]
>>> print('{} {}'.format(b1, b2))
```
Note that the first element is accessed via the index 0,
the second element by index 1, etc.

You can also access multiple elements within a tuple using slicing.
Try the following slices:
```Python
>>> seq_tuple = (1,2,3,4,5,6,7)
>>> seq_tuple[2:5]
>>> seq_tuple[:5]
>>> seq_tuple[2:]
>>> a_tuple[1:5:2]
>>> a_tuple[1::2]
```
Note that slicing does NOT include the final index.

##### Lists
Lists are like tuples, but can be modified after creation.
You can access the elements the same way as with tuples, slicing and all.

Here are some examples where we modify the list through concatenation and sorting.
```Python
>>> a_list = [19, 13, -5, 3, 14, -8]
>>> print(a_list)
>>> a_list[0] = 2
>>> print(a_list)
>>> a_list.append(3.1415)
>>> print(a_list)
>>> a_list += [20, -100, 12.5]
>>> print(a_list)
>>> a_list.sort()
>>> print(a_list)
```
Note that the add equal (+=) assignment is defined as concatenating the right
hand side to the original list. This only works with list, you cannot append using
a += operator.

#### Dictionaries
See the dictionaries.py file for a more comprehensive demonstration of dictionaries.

A dictionary is like a list, but uses keys rather than integer indices to access elements/values.
Since the indices are not integers, slicing does NOT work with dictionaries.

Here is some sample dictionary creation and access calls:
```Python
>>> from pprint import pprint
>>> a_empty_dict = {}
>>> pprint(a_empty_dict)
>>> a_empty_dict['key1'] = 'val1'
>>> a_empty_dict['key3'] = 25
>>> pprint(a_empty_dict)
>>>
>>> a_dict = {'key1':'val1', 'key3':25}
>>> pprint(a_dict)
>>> a_dict['dicKey'] = {1:'hi', 'deep key':'deep val'}
>>> pprint(a_dict)
```
Keys can be anything immutable, including numbers, strings and tuples.

#### Control Flow Statements
See the controlFlow.py file for a more comprehensive description of ifs and loops.

##### If
If statements allow you to execute a block of code only if certain conditions are met.
For example:
```Python
cond1 = True
cond2 = False
cond3 = True
if (cond1 and cond2) or cond3:
   print('the if block was true')
```
indicates that if both `cond1` and `cond2` are true or if `cond3` is true then `print('the if block was true')`.

The `if` statement has associated keywords `elif` (else if) and `else`.
These statements are only executed if the above `if`/`elif` statements failed.
For example:
```Python
>>> cond1 = True
>>> cond2 = False
>>> cond3 = True
>>> if (cond1 and cond2) or cond3:
...     print('the first if block was true')
... elif not cond1 or cond2:
...     print('second block was true')
... else:
...     print('neither statement above was true')
...
```
In this example, the first if statement is the same as the previous example.
If that statement is not `True`, then it checks the second statement.
The second statement checks if `cond1` is false or if `cond2` is true, then prints `second block was true`.
If neither the `if`'s condition nor the `elif`'s condition were true, the else statement executes and will
print `neither statement above was true`.

Next is an example that looks similar to the last one, but is actually *COMPLETELY DIFFERENT*.
```Python
>>> if (cond1 and cond2) or cond3:
...     print('the first if block was true')
... if not cond1 or cond:
...     print('second block was true')
... else:
...     print('the second statement was not true')
...
```
The first if block executes just like before.
But now the second if block is guaranteed to be checked, regardless of what happened with the
first block. The else statement executes if the second condition was not true, regardless
of the first statement.

##### Loops

Python supports 3 types of loops:
1. `while` loops
2. `for` loops
3. list comprehensions

`while` loops function like an if statement, but the code block is
repeated until the condition becomes false. For example:
```Python
>>> i = 1
>>> while (i < 10):
...     i *= 2
...     print(i)
...
>>> print(i)
```
Note that `i` preserves its value upon exit of the while loop.
Any boolean expression that works in an if statement can be used in a `while` loop.

`for` loops cycle through each element in a list, tuple or `range`.
`range` is like a special type of list, that takes 1, 2, or 3 arguments.
Try out the following:
```Python
>>> for i in range(10):
...     print(i)
...
>>> for i in range(2,10):
...     print(i)
...
>>> for i in range(2,10,3):
...     print(i)
...
```
Essentially, the arguments to `range` are analogous to specifying slicing in lists.

Cycling through a list or tuple is similarly easy:
```Python
>>> a_list = ['hello', 'there', 'george','the', 3]
>>> for ele in a_list:
...     print(ele)
...
```

Note that we can perform operations on the loop index, but it will NOT be changed in the
original list.
```Python
>>> a_list = [1,2,3,5,7,11]
>>> for ele in a_list:
...     ele = ele**2
...     print(ele)
...
>>> print(a_list)
```
There also exist 3 methods to allow looping through a dictionary.
They are `<dict_name>.keys()`, `<dict_name>.values()`, and `<dict_name>.items` that work as follows:
```Python
>>> a_dict = {1:'a', 'b':2, 3:'c', 'd':4, 7.2:8.9}
>>> for key in a_dict.keys():
...     print(key)
...
>>> for val in a_dict.values():
...     print(val)
...
>>> for key, val in a_dict.items():
...     print('key = {}, val = {}'.format(key, val))
...
```
Similar to lists, modifying the loop indices does NOT modify the dictionary.

The last type of loop is called a list comprehension.
This allows you to build a list using a for loop, without the multiple lines a for loop requires.
Here are 2 in action:
```Python
>>> squares_list = [x**2 for x in range(10)]
>>> print(squares_list)
>>> evens_list = [y for y in range(10) if y%2 == 0]
>>> print(evens_list)
```
The `squares_list` cycles through every value of `x` in `range(10)`, and saves it to an element in the list.
The `evens_list` cycles through every value of `y` in `range(10)`, and saves it to an element in the list 
if `y%2 == 0`. The `%` is a remainder operator, so `y%2` is the remainder of `y` divided by 2.

> NOTE: in C and java `%` is the modulus operator, which gives you the remainder but only for integers.
> In python by contrast, the number to the left *and/or* the right of `%` can be any number.

#### Numpy arrays
See the numpy_arr.py file for a more comprehensive description of Numpy arrays

Numpy stands for NUMerical PYthon, and is one of the most widely used packages for python
within the scientific community.
It contains many methods for performing numerical computations, as well as other helper functions.
But at the core of Numpy lies the Numpy.array data structure.

Numpy arrays have the following properties:
* a fixed size (or shape), which cannot be modified without redefining the variable
* every index within the shape holds a number
* every number within an array is of the same type (by default, a float.)
* arithmetic operations applied to Numpy.array objects apply element-wise

> In computers, numbers come in different types.
> Python supports ints, floats (similar to a real number), and complex.
> In Numpy, each type (int, float and complex) has subtypes corresponding
> to how much space they take up in memory. For example, a `i8` (integer 8) is twice as large
> as an `i4` (integer 4). The advantage of `i8` is that it can take many more values than `i4`,
> as less memory means less unique integers can be represented by `i4`.
> The vast majority of the time in python and Numpy, the default of float is just fine.
> See [wikipedia: floating point](https://en.wikipedia.org/wiki/Floating_point) for a wider discussion
> on floating point numbers.

Define the arrays `a` and `b` as follows:
```Python
>>> import numpy as np
>>> a = np.ones((3,4))
>>> print(a)
>>> b = np.zeros((3,4))
>>> print(b)
>>> for i in range(b.shape[0]):
...     for j in range(b.shape[1]):
...         b[i,j] = i*j
...
>>> print(b)
```
Some important thing's to note:
* Conventionally, Numpy is imported and renamed np to make code shorter and easier to read
* Numpy has many methods for defining arrays, we are using `np.ones` and `np.zeros` to define arrays filled
  with ones and zeros respectively
* Numpy arrays have an attribute `shape`. This is a tuple describing the size of the array
* For arrays with multiple dimensions, we can access the dimensions using 2 mechanisms - a list like access
  of `b[i][j]`, or an array like access used above (`b[i,j]`)

> NOTE: for 2 dimensional arrays, convention dictates that we consider the first index the row number,
> and the second index the column number. This arises from how matrices work in mathematics.
> Thus b[2,1] is the 3rd row, 2nd column of b (recall that the first row and column have indices of 0).

Since `a` and `b` have the same shape, we can use them both to perform arithmetic operations.
Each operation happens element-wise. Here are some examples:
```Python
>>> print(a)
>>> print(b)
>>> print(b**2)
>>> print(a + b)
>>> print(a*b)
>>> print(3*b - 2*a + 1)
```

The Numpy functions are nearly all defined to take an array in and apply the operation element-wise.
Some simple examples are:
```Python
>>> print(np.sqrt(b))
>>> print( np.rad2deg( np.arctan(b) ) )
```

If Numpy arrays do NOT have the same shape, but have the same dimension, they are incompatible and cannot be
used in the same expression. For example:
```Python
>>> print(a.shape)
>>> a = a.transpose()
>>> print(a.shape)
>>> print(a + b)
```
The last line will throw an exception because the shapes are different.

Numpy provides ways to transform lists of numbers into array, as follows:
```Python
>>> c = np.array([0, 1, 2])
>>> print(c)
>>> d = np.array(list(range(4)))
>>> print(d)
```
> *WARNING*: Be careful mixing lists and arrays. Lists have no fixed shape, and are not required
> to hold only numbers. Whereas arrays have a fixed shape at creation and must hold only numbers.

If you try to use arrays of different dimensions (`len(c.shape) != len(d.shape)`), Numpy will
try to broadcast the small dimension into the larger dimension. 
See [broadcasting rules](http://docs.scipy.org/doc/numpy-1.10.1/user/basics.broadcasting.html) for
a thorough description of how Numpy broadcasts arrays. Try the following:
```Python
>>> print(b.shape)
>>> print(c.shape)
>>> print(d.shape)
>>> print(b + c)
>>> print(b + d)
```
Note that Numpy successfully broadcast `d`, but not `c`.

> Note: Broadcasting can be very useful. It can also cause bugs that are hard to track down.
> These usually arise when Numpy broadcasts something so allows an operation you didn't think
> should work - and that you didn't intend to work.

One last thing, you can transform arrays to lists using the following command
```Python
>>> b_list = b.tolist()
```
> *WARNING - AGAIN*: Be careful mixing lists and arrays. Lists have no fixed shape, and are not required
> to hold only numbers. Whereas arrays have a fixed shape at creation and must hold only numbers.

#### File Input/Output
See the fileIO.py file for a more comprehensive description of fileIO.

For this set of examples, make sure you are inside the src/loopsNds directory for access to the demo.txt file.

There are 2 primary ways to read and write files in python
1. Modules that provide functions that handle all the input/output.
   We will look at one such function Numpy provides.
2. Context managers. These allow you to directly access files yourself.

If a Module function is provided, it is often the easiest way.
Here is an example using `np.genfromtxt`:
```Python
>>> import numpy as np
>>> standings = np.genfromtxt('demo.txt',
...                           dtype=[('name','S10'), ('w','i8'), ('l','i8')],
...                           skip_header=1)
>>> print(standings)
```
`np.genfromtxt` is provided 3 arguments in this example
1. filename
2. what type of data each column is, as well as a name for that column
3. the number of header lines it should skip

If a standard file format is expected, and a function is available from a module,
that is usually the easiest way to read and write to files.

If you are stuck reading and writing the file manually, then you need to open the file
with the context manager, using the following command
```Python
>>> with open(filename, what_to_do) as f:
...     # do stuff 
...
>>>
```
The `filename` should be a string specifying the filename.
The `what_to_do` is a 1 or 2 character code telling python what you want to do with
the file. Here are the most common:
* `"r"` - read from a text file
* `"w"` - write to a text file
* `"rb"` - read from a binary file
* `"wb"` - write to a binary file
Once the file is opened, within the indent block `f` represents your file (`f` is
a variable, so you can name it whatever you want).
One of the nifty things about file object like `f`, is that you can loop through them
like a list, and each iteration interprets a line.

Here is an example where we read the demo.txt file, and write it back out into demo2.txt
```Python
>>> file_lines = []
>>> with open('demo.txt','r') as f:
...     for line in f:
...         file_lines.append(line)
...
>>> print(file_lines)
>>> with open('demo2.txt','w') as f:
...     for line in file_lines:
...         f.write(line)
...
```
Open up demo2.txt, and it should be identical to demo.txt

There are two common data formats to store data from python,
JSON and pickle. JSON is a plain text format, but can only store
standard python types - not Numpy types or any custom objects.
Pickle files are binary files, and can store any arbitrary data from python.

We can write the previously read in file to JSON and pickle files as follows:
```Python
>>> import json
>>> import pickle
>>> with open('data.json','w') as f:
...     json.dump(file_lines, f, indent=2)
...
>>> with open('data.pkl','wb') as f:
...     pickle.dump(file_lines, f)
...
```
The `indent=2` option for JSON is optional, but makes reading the JSON file itself
much easier.
These can then be read in using:
```Python
>>> with open('data.json','r') as f:
...     out_json = json.load(f)
...
>>> print(out_json)
>>> with open('data.pkl','rb') as f:
...     out_pkl = pickle.load(f)
...
>>> print(out_pickle)
```

### Basic plotting
This example should introduce you to the following:
* Basic plotting routines
* Labeling your plots
* Adding legends to your plots

You will need to be in the src/quadratic_eqn/ directory to run this.

There are 3 plotting routines we are going to use:
* `plot_roots.simplePlot` - a simple routine which plots a quadratic equation
* `plot_roots.plotQE` - a plotting routine which plots a quadratic equation and allows the user
   to modify the y limits of the plot
* `plot_roots.plotRoots` - a plotting routine which plots a quadratic equation as well as placing
   vertical bars at its roots.

To set up your environment for these plots, enter the following into the python console:
```Python
>>> from quad_class import quadratic_Equation as QE
>>> import plot_roots as pr
>>> myeqn = QE(.8, 3, -2)
```

The plotting routines dump all plots to the screen - this will stop you from entering
new python command until you close it. 
To save it as a png instead, replace the command `plt.show()` with the command `plt.savefig('myname.png')`.
There are a variety of image formats that Matplotlib is capable of saving to,
depending on the extension you provide it.

To generate the simple plot, run the following:
```Python
>>> pr.simplePlot(myeqn, [-5, 3])
```
This will show a plot of the quadratic equation going from -5 to 3 on the x-axis.
The magic that makes this happen are the following lines:
```Python
x_vals = np.arange(xlim[0], xlim[1], .01) #go from xlim[0] to xlim[1] in step sizes of .01
y_vals = [quadEqn(x) for x in x_vals]
plt.plot(x_vals, y_vals)
plt.show()
```
You just need to define a list of x-values, a list of y-values, then call `plt.plot` on them (`plt` was imported
from Matplotlib).
The `plt.show()` function displays it to the screen.

The `plotQE` function is invoked similarly
```Python
>>> pr.plotQE(myeqn, [-5,3])
>>> pr.plotQE(myeqn, [-5, 3], [-5, 5])
```
The second invocation specifies what limits you want to impose on the y-axis.
Matplotlib is okay at choosing limits for your axis, but the end user can
often do a better job manually.

Limiting the ranges plotted is as easy as invoking the functions
```Python
plt.xlim([<min_x>, <max_x>])
plt.ylim([<min_y>, <max_y>])
```
Note that this plot also has labeled the x and y axis appropriately.
Please see the file for the complete list of commands used.

The final routine can be invoked via
```Python
>>> pr.plotRoots(myeqn)
```
This routine intelligently chooses the x-limits and y-limits
to show the function's roots. It also plots vertical lines at the roots,
adds a legend, and a plot title.

Please see the file for the complete list of commands used.

### Bisection root-finding method
This example should introduce you to the following:
* Bisection method
* lambda functions
* Matplotlib 
   * Labeling your plots
   * Matplotlib axes objects
   * Plotting multiple axes on 1 figure 
   * Saving plots and using a backend with no display non-visual

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
and finickiness of Matplotlib.

Here are some references:
* [lambda expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
* [Matplotlib plotting functions](http://matplotlib.org/1.4.3/api/pyplot_summary.html)
* [Matplotlib gridspec](http://matplotlib.org/1.4.3/api/pyplot_summary.html)
* [Matplotlib backends](http://matplotlib.org/faq/usage_faq.html#what-is-a-backend )
* [Matplotlib sample gallery](http://matplotlib.org/gallery.html)

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
* Comments
   * Comment anything you do that is not immediately obvious when looking at the code.
      This does not mean comment every line (usually - although there are times...),
      but every 'paragraph' of code should have a short comment describing what is going on.
   * Keep your comments succinct. They should not make the code harder to browse.
   * The right amount of comments is a mythical beast, but there _are_ wrong amounts of comments.

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
* [official python tutorial](https://docs.python.org/3/tutorial/)
* [numpy documentation](http://docs.scipy.org/doc/numpy/)
* [Matplotlib sample gallery](http://matplotlib.org/gallery.html)
* And of course, [Google](https://www.google.com/).

I also want to point out one more useful website when you have questions:
[Stack Exchange](http://stackexchange.com/)
Typically this is where google ends up directing you (unless it's Matplotlib,
then google as often as not points you to some wierd documentation page).

If you have any questions, start with the above documentation and google.
If those don't suffice within about half an hour, contact your supervisor.
I am also usually available, so feel free to stop by to see if I'm in.
