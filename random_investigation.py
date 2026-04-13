# random_investigation.py

from random import choice, randint, randrange, shuffle

r = randint(1, 10)
print (r)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (lst)

shuffle(lst)
print (lst)

#lst = randrange(1, 100, 20)
#print (lst)

print (choice(lst))

