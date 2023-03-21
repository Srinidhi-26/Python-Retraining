class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return "The car is starting."
    
    def stop(self):
        return "The car is stopping."

my_car = Car("Toyota", "Camry", 2022)

def call():

    print(my_car.make) 
    print(my_car.model) 
    print(my_car.year)

    v= my_car.start() 
    b=my_car.stop() 

    print(v,b)

call();