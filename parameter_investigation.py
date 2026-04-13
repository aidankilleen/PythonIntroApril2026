# parameter_investigation.py

# if you supply a default value for a parameter
# that parameter becomes optional

# named vs positional parameters - is fairly pythonic

def greet(name="", greeting="Welcome", repeat=1):
    # pass is a valid python command that does nothing
    for i in range(repeat):
        print (f"{greeting} {name}")

greet("Alice", "Welcome")
greet("Bob", "Bienvienu")
greet("Carol", "Wilkommen")
greet("Dan", "Failte")
greet("Eve")
greet("Fred")

# named parameters
# order doesn't matter
greet(greeting="Failte", name="Zoe")
greet(greeting="Failte")

# positional parameters (arguments)
greet("Alice", "Failte", 4)
greet("Bob", "Wilkommen")
greet("Carol")
greet()

# positional and named parameters
greet("Alice", greeting="Failte", repeat=3)


# named parameters are extremely useful
# for functions that have a lot of paramters
greet(name="Alice", greeting="Failte", repeat=3)


