#example for  not use constructor and use method to initialize the value

'''
__int__()
'''

class Car():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

#creating objects
car1 = Car()
car1 = Car('tesla', 'red')

print(car1.brand)
print(car1.color)
