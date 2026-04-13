# greeting.py


def greet(name, greeting="Welcome", repeat=1):
    for _ in range(repeat):
        print (f"{greeting} {name}")


# dunder values
# double underscore before and after
# dunder usually implies something internal to python
# we won't really be creating any of these
# we will be using them

if __name__ == "__main__":
    print (f"__name__ = {__name__}")

    print ("This code is only run if the module is executed directly")
    print ("It is not run if the module is imported")
    greet("Aidan", "Failte", 3)



