# slicing_introduction.py

lst = list(range(1, 11))

print (lst)

print (lst[0])
print (lst[-1])

# slicing
print (lst[2:5])    # [start:stop] start is included stop is excluded

print (lst[:5])     # leave out the first no it assumes the start
print (lst[5:])     # leave out the last no it assumes the end

print (lst[0:9:2]) # [start:stop:step]

odd_numbers = lst[::2]
print (odd_numbers)
even_numbers = lst[1::2]
print (even_numbers)

# step = -1 reverses
print (lst[::-1])


# does this work in other places - eg string?

text = "abcdefghijklmnopqrstuvwxyz"

print (text[0])
print (text[-1])

print (text[5:10])
print (text[:12])
print (text[12:])
print (text[::2])

print (text[::-1])
























