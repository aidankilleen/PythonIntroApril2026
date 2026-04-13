# string_operations.py


from random import randint


message = "welcome to the python course"

print (message)
print (message.title())

# we can multiply strings
print ("=" * 50)

a = 10
b = 20
answer = a + b

print ("The answer is " + str(answer))

print (str(a) + " + " + str(b) + " = " + str(answer))

# this type of string concatenation is quite tedious
# use f-strings instead

print (f"{a} + {b} = {answer}")

# nb: you can put an expression into an f-string
print (f"{a} + {b} = {a + b}")


# inline conditional
r = randint(1, 10)

print (r)
if r < 5:
    print (f"{r} is small")
else:
    print (f"{r} is large")

print (f"{r} is {"small" if r < 5 else "large"}")

print ("-" * 50)
lst = [10, 5, 3, 7, 1, 8]

for n in lst:
    print (n, "\t", "*" * n)

# note print can have multiple parameters print (a, b, c, ...)
# \t is an "escape" character - tab

# \n - newline
# \r - is a carriage return
# \" - puts in a double quote

message = "press the \"red\" button"

# \\ puts a single slash character into my string
filename = "c:\\my files\\file.txt"

# single quotes and double quotes do the same thing

message = "this is a message"
message = 'this is a message'

message = 'press the "red" button'
print (message)

name = "John O'Sullivan"
print (name)

print (len(name))
for c in name:
    print (c)


# python tries to be logically consistent
# if len() returns the length of a list
# it should also return the length of a string
# or the length of a file 
# or the length of anything you care to send it

# if I can use for to iterate through the items in a list
# I should be able to use for to iterater through 
# the characters in a string
# the lines in a file
# anything else that is iterable










































