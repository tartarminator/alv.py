# class Car:
#     wheels_numbers = 4
#
#     def __init__(self, model, color, year, is_crashed):
#         self.model = model
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
#     def drive(self, city):
#         print(self.model + ' Car is driving to ' + city)
#
#     def change_color(self, new_color):
#         self.color = new_color
#
#
# opel_car = Car('Opel Vectra', 'white', 2019, False)
# opel_car.drive('Tashkent')
# print(opel_car.drive)
# print(opel_car.wheels_numbers)
# print(opel_car.is_crashed)
# print(opel_car.model)
#
# mazda_car = Car('Mazda CX7', 'red', 2018, True)
# mazda_car.drive('Moscow')
# mazda_car.change_color('yellow')
# print(mazda_car.color)


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.circumference = 2 * self.pi * self.radius

    def get_area(self):
        return self.pi * (self.radius ** 2)

    # def get_circumference(self):
    #     return 2 * self.pi * self.radius


circle_1 = Circle(radius=12)
# print(circle_1.get_area(), get_circumeference())
x = circle_1.circumference
print(x)
print(circle_1.get_area())
circle_2 = Circle(7)
print(circle_2.get_area())
print(circle_2.circumference)


# print(circle_2.get_area())


class BankAccount:
    def __init__(self, client_id, client_first_name, client_last_name, balance=0.0):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = balance

    def add(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


vip_client = BankAccount('Vip client', 'Tim', 'Johns')
vip_client.add(15000)
print(vip_client.balance)
vip_client.withdraw(500)
print(vip_client.balance)
