class car():
    #method
    def start(self):
        print('car is starting....')

    def stop(self):
        print('car is stopping....')
    
car1 = car()
car2 = car()

car1.start()
car1.stop()

car2.start()
car2.stop()


class Car():
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color

    def show_details(self):
        print(f'car brand is a {self.color} {self.brand}')

car1 = Car()
car1.set_details('red', 'Toyota')

car2 = Car()
car2.set_details('blue', 'Honda')

car1.show_details()
car2.show_details()

              