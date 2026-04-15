# set investigation.py


s1 = {1, 2, 2, 3, 4}

print (s1)

c1 = {"red", "green", "blue", "orange"}
c2 = {"pink", "white", "black", "red "}

c3 = [colour.strip() for colour in list(c2)]

print ("-" * 50)
print (c3)

print (c1)
print (c2)
colours = c1.union(c2)
print (colours)

both = c1.intersection(c2)
print (both)

print (c1.difference(c2))
print (c2.difference(c1))

print(c1.symmetric_difference(c2))

print ("-" * 50)
# python operator overloading
print (c1 | c2) # union
print (c1 & c2) # intersection

print (c1 - c2) # difference
print (c2 - c1) # difference

print (c1 ^ c2) # symmetric difference


s1 = {1, 2, 3, 4}
s2 = {4, 3}

if s2 <= s1:
    print ("s2 is a subset of s1")
else:
    print ("s2 is not a subset of s1")

if 4 in s2:
    print ("4 is in the set")
else:
    print ("4 is not in the set")

r = range (1, 10)

print (r[2:5])

# start is inclusive stop is exclusive
#numpy.ran

print ("-" * 50)

c1 = {"red", "green", "blue", "orange"," red", "red\n"}
c2 = {"pink", "white", "black", "red "}

print (c1)
print (c2)

c1 = set([colour.strip() for colour in list(c1)])
c2 = set([colour.strip() for colour in list(c2)])

print (c1)
print (c2)
print (c1 | c2)





