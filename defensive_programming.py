# defensive_programming.py

# defensive programming
# checking all inputs to all functions and anticipate
# all things that might go wrong and write code 
# to handle these

# this is very onerous
s = input("how many loops?")

if s.isnumeric():
    n = int (float(s))
    for i in range(n):
        print (i)
else:
    print ("That's not a number")

print ("finished")

# glass is half empty approach
# r = dosomething()
# if r == -1:
#     pass
# elif r == -2:
#     pass
# elif r == -3:
#     pass
# else:
#     # no error 
# r = dosomethingelse()
# if r == -1:
#     pass
# elif r == -2:
#     pass
# elif r == -3:
#     pass
# else:
#     # no error 


# use exceptions instead

# try:
#     dosomething()
#     dosomethingelse()

# except:
#     # errors get handled here
#     pass


