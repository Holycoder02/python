#polymorphism with classes method overriding means that you can make them behave differently
class Bird():
    def sound(self):
        print('Birds make sounds')

class Crow(Bird):
    def sound(self):
        print('Crows say "caw caw caw"')
    
class Parrot(Bird):
    def sound(self):
        print('Parrots say "squawk squawk"')

bird1 = Crow()
bird2 = Parrot()

bird1.sound() #Output: Crows say "caw caw caw"
bird2.sound() #Output: Parrots say "squawk squawk"

"""
=======================================================
with operators

"""

print(5 + 10)
print('Hello' + 'world')
print([1,2] + [3,4])

