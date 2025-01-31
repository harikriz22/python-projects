# class variables
# class methods

class Car:

    wheels=4 #class variable

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def starts(self):
        return "Car is starting"
    
    @classmethod
    def showwheels(cls):
        print(cls.wheels)
    
    @staticmethod
    def addz(a,b):
        return a+b

c1=Car('honda','civic',2015) 
c2=Car('honda','amaze',2015) 
print(c2.addz(3,4))

# variables inside a class
    
#     class variable / static variable
#     instance variable

# type of methods inside a class
    # class method
    # instance method
    # static method




# decorators

# functions hichh wraps another functions