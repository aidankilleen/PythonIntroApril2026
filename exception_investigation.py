# exception_investigation.py

from random import randint

a = 10
b = 0
lst =[1, 2, 3, 4]
n = "ninety nine"
answer = 0

r = randint(1, 4)

try:
    if r == 1:
        answer = int(n)
    elif r == 2:
        answer = lst[4]
    elif r == 3:
        answer = a / b
    else:
        # no error occurs
        answer = 42
except ZeroDivisionError:
    print ("you can't divide by zero")
    answer = 1
except IndexError:
    print ("index out of range")
    answer = lst[-1]
# always supply a catch all Exception handler
# catch all exception should be last
except Exception as ex:
    print ("Something went wrong")
    print (ex)
finally:
    # this code gets called no matter what
    # it gets called if there is an exception
    # it gets called if there isn't
    print (f"The answer is {answer}")

print ("Finished")

