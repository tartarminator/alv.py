# Inheritance (наследственность)


# class Car:
#     wheels_numbers = 4
#
#     def __init__(self, model, color, year, is_crashed):
#         self.model = model
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#         print('Car is created.')
#
#     def drive(self, city):
#         print(self.model + ' is driving to ' + city)
#
#     def change_color(self, new_color):
#         self.color = new_color
#         print('Truck ' + self.model + ' is changed color to ' + new_color + '.')
#
#
# class Truck(Car):
#     wheels_numbers = 10
#
#     def __init__(self, model, color, year, is_crashed):
#         Car.__init__(self, model, color, year, is_crashed)
#         print('Truck is created.')
#
#     def drive(self, city):
#         print('Truck ' + self.model + ' is driving to ' + city)
#
#     def load_cargo(self, weight):
#         print('The cargo is loaded. Weight is ' + str(weight) + ' kg.')
#
#
# volvo_truck = Truck('Volvo', 'grey', 2010, False)
# volvo_truck.drive('London')
# print(volvo_truck.wheels_numbers)
# print(volvo_truck.color)
# volvo_truck.change_color('pink')
# print(volvo_truck.color)
# volvo_truck.load_cargo(10000)

# Polymorphism (многообразие)


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         raise NotImplementedError('Class successor must implement this method.')
#
#
# class Dog(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name + ' is saying woof.')
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name + ' is saying meow.')
#
#
# class Bird(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name + ' is saying chi-chirik.')
#
#
# class Fish(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name + ' is saying nothing.')
#
#
# tuzik = Dog('Tuzik')
# simba = Cat('Simba')
# shegol = Bird('Shegol')
# freddy = Fish('Freddy')
# pet_list = [tuzik, simba, shegol, freddy]
#
# # pet_list[0].speak()
# # pet_list[1].speak()
#
#
# for pet in pet_list:
#     pet.speak()
#
#
# def pet_voice(pet):
#     pet.speak()
#
#
# pet_voice(tuzik)
# pet_voice(simba)
# pet_voice(shegol)
# pet_voice(freddy)


class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print('Hi my name is ' + self.name)


class Villain(GameCharacter):
    # def __init__(self, name, health, level):
    #     self.name = name
    #     self.health = health
    #     self.level = level

    def __init__(self, name, health,
                 level):
        GameCharacter.__init__(self, name, health,
                               level)

    def speak(self):
        print('Hi, my name is ' + self.name + ' and I will kill you.')

    def kill(self, gamer):
        gamer.health = 0
        print('Bang-bang, now you\'re dead.')


gamer_1 = GameCharacter('Piter', 90, 3)
gamer_2 = Villain('Negorro', 80, 5)
gamer_1.speak()
gamer_2.speak()
print(gamer_1.health)
gamer_2.kill(gamer_1)
print(gamer_1.health)

