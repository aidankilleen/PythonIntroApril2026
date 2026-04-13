# building_block.py
# By: Aidan
# Date: 13/04/2026

# the hash character introduces a comment


from random import randint


print ("Core Building Blocks of Python") # comments at end of line


"""
this 
is
a 
multi line comment
"""

# note the naming convention
building_blocks = ""

# building block #2 - variables

name = "Aidan"
n = 1234
f = 1.23456

# python has types
# but it is "weakly typed"
n = 99
n = "ninety nine"

print (n)

# pythonic (unique to python)
# you can create large numbers
n = 349839485734987509834750394780895347908475073409
n2 = 234987230947239872430897432089723407234042370


# building block # 3 - expression

a = 10
b = 20

answer = ((a + b) * 20) - ((15 / 3) * (2 ** 3))

# pythonic - you can multiply a string
print ("*" * 50)


# building block #4 - condition

a = 10
b = 20

#NB: the tab on the line after the : is part of the syntax
# pythonic - most languages ignore whitespace but python does not
if a < b:
    print ("a is less than b")
    print ("this is exectured too")
else:
    print ("a is greater than b")

n = 5
if n < 5:
    print ("small")
elif n < 7:
    print ("medium")
else:
    print ("large")


# building block # 5 - loop.
n = 1

while n < 10:
    print (n)
    n += 1      # shortcut equivalent to  n = n + 1


# building block #6 - arrays - list

lst = [1, 4, 3, 2, 9, 6, 7, 5]

# pythonic - python has a number of list-like constructs

print (lst[1]) # list index starts at 0 - lst[1] is the second item
print (lst[0])

print (len(lst))    # len() function returns the length

# pythonic - python supports negative index
print (lst[-1])     # last item from the list

print ("*" * 50)
# iterate or loop through the list using for
for i in lst:
    print (i)

# lists can have different elements
# lists are heterogenous
lst = [3, 3.0, [1, 1, 1], "three"]


# building block # 7 - functions

# built-in functions
name = "Aidan"
print(name)
len(name)


# standard libarary functions
# to use a function from the standard libary
# you must "import" - see top of file
r = randint(1, 10)
print (r)

# there are hundreds of thousands third pary libararies
# pypi.org

# user defined functions

def greet(name):
    print ("hello " + name)

greet("Aidan")
greet("Bob")
greet("Carol")

# if a function does a calculation
# it can return the value to the caller
def mysum(a, b):
    answer = a + b
    return answer

print (mysum(10, 20))

# building block # 8
# python is an object oriented programming language
# the values (data) and functions (methods) for an data type
# are encapsulated in the string object

name = "Aidan"
print (name.upper())


# we can write our own objects
# we will working with objects that are coming from a 
# module or library.







































































































