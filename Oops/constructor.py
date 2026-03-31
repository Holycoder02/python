class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
car1 = Car("Toyota", "Red") #values automatically set
print(car1.brand, car1.color) #Output: Toyota Red



"""
syntax:
class ClassName:
    def __init__(self, parameter1, parameter2):
     self.property1 = parameter1
     self.property2 = parameter2

__init__ is a special method in Python classes, known as the constructor. It is automatically called when an object of the class is created. The purpose of the __init__ method is to initialize the attributes of the class with the values provided as arguments when creating an instance of the class.
__init__() constructor     
self.property:   it store the value of the parameter passed to the constructor when creating an instance of the class. It allows us to set the initial state of the object with specific values for its attributes.

"""

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

#creating objects of the Student class
student1 = Student('Rakesh', 100, 'A')
student2 =Student('Kalpesh', 50, 'B')

print(student1.name, student1.age, student1.grande) #Output: Rakesh 100 A
print(student2.name, student2.age, student2.grade) #Output: Kalpesh 50 B

"""
1- defauilt contructor: (self)   :- If you do not define an __init__ method in your class, Python will provide a default constructor that does nothing. This means that you can create instances of the class without passing any arguments, but the attributes will not be initialized.
2- Parameterized constructor: (self, name, age, grade)   :-You can define an __init__ method that takes parameters to initialize the attributes of the class. This allows you to create instances of the class with specific values for its attributes.
3- Multiple constructors: or constructor with default values: you can define multiple __init__() methods with different parameters, or you can use default values
"""