# tuple_investigation.py

# tuple is an immutable list
# reason 1 - optimisation of performance
# reason 2 - good sw engineering practice to prevent things from changing

t = tuple(range(1, 11))

print (t)

print (t[0])
print (t[-1])

# slicing works on tuples
print (t[3:6])
print (t[:6])
print (t[6:])
print (t[::2])
print (t[::-1])

#  you cannot change a tuple
#t[0] = 999 # will cause an error

# What can I use this for?

# return multiple values from a function

def process_list(numbers):
    mx = max(numbers)
    mn = min(numbers)
    return (mx, mn)

numbers = [1, 10, 87, 99, 56, 34, 21]
answer = process_list(numbers)

print (numbers)
print (answer)
print (f"max = {answer[0]}   min = {answer[1]}")

# use unpacking to get individual variables
(mx, mn) = process_list(numbers)
print (f"max = {mx}  min = {mn}")


# use a tuple as a key for a dictionary
# this allows a compound key in a dictionary
d = {
    (1, 1): "red", 
    (1, 2): "green",
    (2, 1): "red", 
    (2, 2): "blue"
}

print (d[(1, 1)])


# you can use a tuple to swap some variables

a = 10
b = 20

print (f"a = {a}     b = {b}")
# swap these variables
# traditionally we use a temporary variable
t = a
a = b
b = t

print (f"a = {a}     b = {b}")

# use a tuple - no temporary
(a, b) = (b, a)

print (f"a = {a}     b = {b}")


# NB - you don't always need the ()


t = (1, 2, 3)
a, b, c = t
print (a, b, c)


mx, mn = process_list([8, 7, 6, 5, 10, 9])
print (mx, mn)


# you might need a tuple with a single item
t = (1)
print (t, type(t))

t = (1, )
print (t, type(t))

t = 1,
print (t, type(t))


# the enumerate function returns tuples (index, item)
lst = ["red", "green", "blue", "black", "white"]

for index, colour in enumerate(lst):
    print (index, "\t", colour)

for item in enumerate(lst, 1):
    print (item[0], "\t", item[1])






































