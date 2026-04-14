# raise_exception_investigation.py


def greet(name):
    if isinstance(name, str):
        print ("Welcome {name.title()}")
    else:
        raise TypeError("You need to supply a string")

# we raise errors to encourage who ever is calling out code
# to use try and catch
greet("Aidan")
greet(12)



