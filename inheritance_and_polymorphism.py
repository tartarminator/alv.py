# Inheritance


class Car:
    wheels_numbers = 4

    def __init__(self, model, color, year, is_crashed):
        self.model = model
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

    def drive(self, city):
        print(self.name + ' is driving to ' + city)

    def change_color(self, new_color):
        self.color = new_color

class Truck(Car)



