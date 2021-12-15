# Inheritance


class Car:
    wheels_numbers = 4

    def __init__(self, model, color, year, is_crashed):
        self.model = model
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        print('Car is created.')

    def drive(self, city):
        print(self.model + ' is driving to ' + city)

    def change_color(self, new_color):
        self.color = new_color


class Truck(Car):
    def __init__(self, model, color, year, is_crashed):
        Car.__init__(self, model, color, year, is_crashed)
        print('Truck is created.')


volvo_truck = Truck('Volvo', 'grey', 2010, False)
volvo_truck.drive('London')

