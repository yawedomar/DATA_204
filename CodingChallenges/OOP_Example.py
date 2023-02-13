# Attributes = what an object is or has [name,height,age]
# Methods = what an object can do/ An action [Sleep,Eat,Run]
# instance variable = declared inside the constructor and can be given unique values
# class variable = declared within a class but outside the constructor. Cna set default value for all instances of this class

# Class can function as a blue print that would describe what attributes and methods that a distinct type of objects will have. 
# Class can function as a blue print to create objects, can assign attributes and methods

class Vehicle:

    wheels = 4     #Class variable/attribute- declared inside the class but outside the constructor
    
    def __init__(self, mileage,cost):
        self.mileage = mileage  #instance variable, each object can have their own unqiue values
        self.cost = cost

    def show_vehicle_details(self):    #Creating methods 1
        print("Mileage of vehicle is", self.mileage, "and it costs £",self.cost)
    

''' 
Each class can have their own unique attributes and methods, along with the attributes and methods they inherit from parents 
Multiple inheritance = when a child class is derived from more than one parent class
'''

class Car(Vehicle):     #child class inherits everything from parent class
    
    def __init__(self, mileage, cost, model, colour):
        self.model = model     
        self.colour = colour
        super().__init__(mileage,cost)
    
    def show_car_details(self):    
        print("The model of the car is", self.model)
        print("The colour of the car is", self.colour)
    
    def setspeed(self, speed):
        print(self.model,"Now travelling at", speed, "miles per hour")

    
class Engine(Car):

    def __init__(self, mileage, cost, model, colour, power):
        self.power = power     
        super().__init__(mileage, cost, model, colour)

    def setPower(self, power):
        print ("Current Engine power is set to: ", power)

    def show_car_details(self):        #Example of method overiding from 'Car CLASS'
        print("The engine detail for",self.model, "is not available")




v1 = Vehicle(3000, 50000)
v2 = Vehicle(1400, 99000)
c1 = Car(1200,8600,"Vauxhall","Black")
c2 = Engine(200,16600,"Ford","Pink", 10000)



v1.show_vehicle_details()
# Prints Mileage of vehicle is 3000 and it cost £50000

v2.show_vehicle_details()
# Prints Mileage of vehicle is 1400 and it cost £99000

#Calling the child class

c1.show_car_details()
# Prints The colour of the car is Black

c2.setPower(1000)
#Prints Current Engine power is set to 1000

c2.show_car_details() #Overding the car class
#Prints The engine detail for Ford is not available"

###


