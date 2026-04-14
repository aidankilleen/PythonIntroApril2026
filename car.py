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

