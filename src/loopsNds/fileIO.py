#!/usr/bin/env python3

"""
This module introduces some simple file io.
It needs the demo.txt file.

See the https://docs.python.org/3/tutorial/inputoutput.html documentation
for more details (but beware as it mostly focuses on file io WITHOUT
a context manager, which is not usually a good idea unless you have to).
"""

from pprint import pprint
import numpy as np

# This shows how to work with simple, unstructured files.
# You will rarely encounter these, as usually a standard format
# is used.

### READING FILES

# the open function with a 'r' opens up the file
# for reading. By burying it inside a with, python
# makes sure that the file is closed at the end
fileTxt = ""
with open('demo.txt','r') as f:
    # read every line in the file, in a loop
    for line in f:
        # append the line into the fileTxt variable
        fileTxt += "{}".format(line)        

print(fileTxt)

# parsing it into a dictionary
standings = {}
with open('demo.txt','r') as f:
    # read the header line and advance to the next line
    f.readline()
    # read the file line by line, starting after the first line due to the above advancement
    for line in f:
        # split the line. The line is a string, and
        # split will turn it into a list of strings.
        # The list is the input string broken at each whitespace (by default), or user provided character set.
        name, win, loss = line.split()
        # Store these in the standings dictionary
        standings[name] = {'w':int(win), 'l':int(loss)}

pprint(standings)

### WRITING FILES
# We can write the standings variable into a file using the following three methods (among others)

# custom format
# using the open(*,'w') opens the file for writing.
with open('demo2.txt','w') as f:
    # write the header
    f.write('name  win  loss\n')
    for name, rec in standings.items():
        f.write('{} {:d} {:d}\n'.format(name, rec['w'], rec['l']))

# using the json format
import json 
with open('demo.json','w') as f:
    # the indent option makes it more readable
    json.dump(standings, f, indent=2)

# read it back in with standings
with open('demo.json','r') as f:
    st2 = json.load(f)
print('after json-ifying')
print(st2)

# using the pickle format
# this is a binary format, so we have to open up a bytestream. hence the 'wb' - implying write bytes
import pickle
with open('demo.pkl','wb') as f:
    pickle.dump(standings,f)

with open('demo.pkl','rb') as f:
    st3 = pickle.load(f)
print('after pickling')
print(st3)

### NUMPY CONVENIENCE READER

# Numpy also has built in functions to read in a structured text file.
# Here is one example:
standings_np = np.genfromtxt('demo.txt', 
                             dtype=[('name','S10'),('w','i8'),('l','i8')], 
                             skip_header=1)
                             
# See the http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.genfromtxt.html documentation.
# Other methods to accomplish the same thing include:
#   http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.loadtxt.html - a simpler but less powerful function

print(standings_np)
print('names')
print(standings_np['name'])
