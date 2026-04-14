# list_splitting.py

lst = list(range(1, 11))

print (lst)

[a, b, *rest] = lst

print (a)
print (b)
print (rest)

a = 27

print (lst)

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

a = 10
b = 20
c = a + b


final_list = lst1 + lst2
print (final_list)

print (id(lst1))
print (id(lst2))
print (id(final_list))





