#example of using constructor to initialize the value

'''
__init__()
'''

class Car():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

#creating objects
car1 = Car('tesla', 'red')

print(car1.brand)
print(car1.color)
