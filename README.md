# pyTutorial
Python tutorial for incoming summer students at UT:ARL 2016

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
$ ls
$ mkdir my_new_directory
$ ls
$ cd my_new_directory
$ echo 'Hello world' > test.txt
$ cp test.txt test2.txt
$ less test.txt
$ less test2.txt
$ man man
$ man ssh
```
This series of commands should have done the following:

1. list the files and subdirectories in your current directory (this will probably be your home)
2. makes a new directory named 'my_new_directory'
3. Same as 1, but should now include a new directory
4. moves you into the directory 'my_new_directory'
5. echo prints 'Hellow world' to the screen, but the `> test.txt` dumps the output into the file test.txt
6. copies the test.txt file to a new file called test2.txt
7. less opens the file to view. It is a minimal viewing program that does NOT allow editing of the file.
   Navigate with the arrow keys. Exit by pressing 'q'
8. opens the test2.txt file. Should be identical to the test.txt file opened in 7
9. man opens up the manual page for the command. This line opens up the manual command for man itself
10. the man page for ssh. This is how you can move to using a different machine

## Python
For this demo we will be using python.
This is a fairly user-friendly language that takes care of lots of
overhead behind the scenes (memory management, complex data structures),
and there exist a LOT of packages out there to make the base language more powereful.

We will be focusing on python3, and the packages NumPy and MatplotLib.
There is also an older version python2 still commonly used, but the syntax
is very similar.

Python is an interpreted language, which means no compilation is necessary before
running it. In fact, you can run it through an interactive console, so each command
is executed directly after you type it.

If you are not there for the live demo, the source below exists
inside the src/ directory which you can execute on your own machine.

### Editing python code
#### Interactive console
Similiar to how bash commands were preceded by a `$`, in the interactive console
in python precedes each command with a `>>>`.
To launch the interactive console, open a terminal and launch 'python3'.
Try running the following commands:
```Python
>>> print('Hello World')
>>> a = 2016
>>> a
>>> b = 'My first formatted statement in'
>>> print('{} {:d}!'.format(b,a))
```
This series of command should have done the following:

1. printed teh statement 'Hello world' to the screen
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
* format statments let you print more complicated statements. What it is printed
  as is defined inside the `{}`. The first item was left unspecified, so python
  did its best (printing a string is pretty straightforward). The second item was
  specified as `{:d}`, which told python to print the contents of a as an integer
  (d stands for integer in print statements)

#### Python modules
A python module is just a text file containing python commands.
The convention is that python files use the extension .py.
Copy the following code into a file name test.py:
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

You can also run this directly from the terminal without calling python.
But first you have to tell your machine that it is safe to execute this file.
To enable execution, use the command (look it up via `$ man chmod`)
```Shell
$ chmod +x test.py
```
Then execute the file using
```Shell
$ ./test.py
```

```
NOTE: The first line in the file,
#!/usr/bin/env python3
is a special type of comment for the first line. It is called a shebang, and the terminal 
you are in reads this and knows to launch this file as a python3 script.
(technically your shell is doing the heavy lifting. The terminal is just the screen
interface to the shell. Google "bash shell" for a description of the standard shell) 
```

### Roots of a quadratic equation

