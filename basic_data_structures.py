# basic_data_structures.py

lst = [1, 2, 3, 4, 5, 6]

print (len(lst))

print (lst[0])
print (lst[-1])

for item in lst:
    print (item)




# there is a built-in function called "list"
# in python we don't get an error if we reassign an existing item!
#list = [1,2,3,4,5]
#print (list)

print(lst)

# lists are mutable
lst[0] = 9999
print (lst)

# Dictionary
d = {
    "id": 10000, 
    "name": "Aidan", 
    "email": "aidan@gmail.com", 
    "active": True
}

print (d)
print (d["id"])
print (d["name"])

print (d.keys())
print (d.values())

# print (d["xxxxxxx"])
# code "crashes" if there is a runtime error

print (len(d))
for key in d:
    #print (f"{key} \t {d[key]}")

    print (key, d[key])

# dictionaries are "mutable"
d["phone"] = "0871234567"

print (d)



print ("Tuple")
# tuple - a list but you can't modify it
# (immutable) - mutate means to change
# In python a lot of things are immutable (can't be changed)
t = (1, 2, 3, 4, 5)

print (t)
print (len(t))
print (t[0])
print (t[-1])

for i in t:
    print (i)

# tuples are immutable
# t[0] = 999


# python uses immutable objects for 2 main reasons

# 1. if something can't be changed then python can 
# optimise the memory
#
# 2. in software engineering - if something can't be changed 
# it eliminates a lot of potential bugs 


# Set

# data structure where there is only one of each item
# use it to create a distinct list
# list of unique items
s = {1, 1, 1, 1, 2, 2, 2, 22, 3, 3, 3, 3, 4, 4, 4, 4, 4}

s = {4, 3, 2, 1,1,2,3,4,1,2,3,4,1,2,3,4}   # be consistent

print (s)
print (len(s))

for i in s:
    print (i)

# list
# dictionaries
# tuples (immutable)
# sets




# converting from one thing to another

s = "10"

# there is usually a built-in function for conversions
answer = int(s) * 5
print (answer)

print (int("10") * int("5"))

#print ("answer = ")

lst = [1, 2, 3]

t = tuple(lst)

print (t)

l = list(t)

print (l)


lst = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 7, 7, 9]

print (set(lst))
# print (dict(lst))
print (type(lst))
print (type(t))
print (type(d))


#
a = 10

amount = 20

final_amount = 30

finalAmount = 30

#3d = "" # variable names cannot start with a number

d0 = 1
d1 = 2

#list = 10 # don't reassign names


keys = ["id", "name", "email"]
values = [100, "Aidan", "aidan@gmail.com"]

print (zip(keys, values))

d = dict(zip(keys, values))

print (d)

dvalues = [("id", 100), ("name", "Aidan")]

d = dict(dvalues)

print (d)



































