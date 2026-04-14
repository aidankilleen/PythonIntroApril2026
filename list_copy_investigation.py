# list_copy_investigation.py

lst = list(range(1, 11))

print (lst)

cp = lst    # this operation does not copy the list
            # I just have 2 variables that are referring to the same list

print (lst)
print (cp)

cp[0] = 999

print (lst)
print (cp)

print (id(lst))
print (id(cp))

# we can use slicing to copy a list
cp = lst[:]

print (lst)
print (cp)

cp[0] = 1111

print (lst)
print (cp)

print (id(lst))
print (id(cp))




