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
        print('Truck ' + self.model + ' is changed color to ' + new_color + '.')


class Truck(Car):
    wheels_numbers = 10

    def __init__(self, model, color, year, is_crashed):
        Car.__init__(self, model, color, year, is_crashed)
        print('Truck is created.')

    def drive(self, city):
        print('Truck ' + self.model + ' is driving to ' + city)

    def load_cargo(self, weight):
        print('The cargo is loaded. Weight is ' + str(weight) + ' kg.')


volvo_truck = Truck('Volvo', 'grey', 2010, False)
volvo_truck.drive('London')
print(volvo_truck.wheels_numbers)
print(volvo_truck.color)
volvo_truck.change_color('pink')
print(volvo_truck.color)
volvo_truck.load_cargo(10000)

# Polymorphism
