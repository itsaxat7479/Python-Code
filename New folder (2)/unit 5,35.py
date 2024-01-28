#Create a base class called Vehicle with a method display_info. Implement two derived 
#classes, Car and Bike, that inherit from Vehicle. Override the display_info method in 
#each derived class to include specific information about the vehicle type.




class Vehicle:
    def display_info(self):
        print("Generic Vehicle Information")

class Car(Vehicle):
    def display_info(self):
        print("Car Information - Model XYZ")

class Bike(Vehicle):
    def display_info(self):
        print("Bike Information - Model ABC")

# Example usage:
vehicle = Vehicle()
vehicle.display_info()

car = Car()
car.display_info()

bike = Bike()
bike.display_info()
