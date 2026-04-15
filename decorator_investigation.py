#decorator_investigation.py


# decorators are indicated using @

# a decorator 

def wrapper_function(func):
    def wrapper(*args, **kwargs):
        print ("About to call the function")
        func(*args, **kwargs)
        print ("After calling the function")
    return wrapper

@wrapper_function
def greet(name):
    print (f"Welcome {name}")

greet("Alice")