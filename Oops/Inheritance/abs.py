from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod     #which is used to declare a method as abstract method
    def start(self):
        pass  #no implementation, just a placeholder

class Car(Vehicle):
    def start(self):
        print('Car starts with a key')
    
class bike(Vehicle):
    def start(self):
        print('bike starts with a button')
    
car = Car()
bike = bike()  #child class objects

car.start() #Output: Car starts with a key
bike.start() #Output: bike starts with a button

"""
key Takways:
1- Abstraction hides the unnecessary details and show only the essential features of the object.
2- Abstract methods are defined in the abstract class using the @abstractmethod decorator. These methods
3- complexity makes very easy to use and understand.
4- Abstract classes cannot be instantiated directly, but they act as blueprints.
5- child classes must define classses that inherit from the abstract class and provide implementations for the abstract methods.
6- Abstraction allows us to focus on what an object does rather than how it does it

"""