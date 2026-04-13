# range_investigation.py

# 10 is "stop" - start is 0 by default
for i in range(10):

    print (i)

print ("-" * 50)
# start, stop
for i in range(1, 5):
    print (i)

print ("-" * 50)

# start, stop, step
for i in range(1, 10, 2):
    print (i)

# start is "inclusive"
# stop is "exclusive"

# python strives for logical consistency
# in other contexts start is usually inclusive and stop is usually exclusive

r = range(1, 11)
l = list(r)
print (l)

l = list(range(1, 11))
print (l)


# use range in for

print ("-" * 50)

# c programmers usually try to get an index
# to go through a list
for i in range(len(l)):
    print (l[i])

# but remember 
# we can just iterate through the list
for item in l:
    print (item)

colours = ["red", "green", "blue", "black", "white"]

"""
1 = red
2 = green
3 = blue
...
"""

# perfectly valid
for i in range(len(colours)):
    print (f"{i} = {colours[i]}")

# pythonic way - use the enumerate() function

for (index, colour) in enumerate(colours, 1):
    print (f"{index} = {colour}")



















