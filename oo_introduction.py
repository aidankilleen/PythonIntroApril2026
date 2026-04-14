# oo_introduction.py

# object is a programming construct
# where data related to a concept
# and all the functions for working on that concept
# are "encapsulated" together into a single reusable unit


# goals 
# modular - everything is in a single place
# promote code reuse
# model things from the real world easier
# than if we just had functions

value = 9999

# naming convention for constants
# is to use ALLCAPS
MAX_ENGINE_SIZE=10000


#Naming convention for objects
# is UpperCamelCase
class SuperCar():
    pass

class Car():
    
    # __init__ is the constructor - java, c++ 
    def __init__(self, make, model, engine_size):
        print ("creating a new car")
        self.make = make
        self.model = model
        self.engine_size = engine_size

    def __str__(self):
        return f"{self.make} {self.model} {self.engine_size}"
    
    def start(self):
        print (f"starting... {self.make} {self.model}")


#print (f"__name__ = {__name__}")

class Truck():
    pass

if __name__ == "__main__":
    mycar = Car("Nissan", "Micra", 1400)
    print (mycar)


    mycar.start()
    print (mycar.make)
    print (mycar.model)
    print (mycar.engine_size)

    mycar2 = Car("Mercedes", "SLK", 2400)
    print (mycar.make)
    print (mycar.model)
    print (mycar.engine_size)

    print (mycar)











