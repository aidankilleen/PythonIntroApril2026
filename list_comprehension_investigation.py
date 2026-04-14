# list_comprehension_investigation.py


from random import shuffle


names = ["alice", "bob", "carol", "dan"]
capitalised_names = []

for name in names:
    capitalised_names.append(name.title())

print (capitalised_names)
# not the pythonic way!!!
# the pythonic way is to use a "list comprehension"

capitalised_names = [name.title() for name in names]
print (capitalised_names)

# we can use a list comprehension to filter a list as well
numbers = [9, 6, 5, 4, 2, 8, 7, 1]

odd_numbers = [n for n in numbers if n % 2 == 1]

print (numbers)
print (odd_numbers)

# you can have multiple for loops
products = ['pen', 'pencil', 'paint']
colours = ['red', 'green', 'blue']

product_list = [f"{colour} {product}" for colour in colours for product in products]

print (product_list)

# Exercise

# use a list comprehension to create 52 playing cards 
# shuffle the cards
# deal 4 hands of 13 cards 

suits = ["H", "S", "D", "C"]
values = ["A"] + [str(i) for i in range(2, 11)] + ["J", "Q", "K"]

print (suits)
print (values)

cards = [f"{value}{suit}" for suit in suits for value in values]

print (cards)
shuffle(cards)
print (cards)

hand1 = cards[::4]
hand2 = cards[1::4]
hands = [cards[i::4] for i in range(4)]

for hand in hands:
    print (hand)




#print (hand1)
#print (hand2)










# cards = ["AH", "2H", ..., "KD"] # use a list comprehension to create this array

# hand1 = [...]
# hand2 = [...]
# hand3
# hand4






















