# help(list)
# my_list = [1, 2, 3, 4]
#
# my_list.append(5)
# print(my_list)


# class MyFirstClass:
#     pass
#
#
# object_of_my_class = MyFirstClass()
# print(type(object_of_my_class))

class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year


mazda_car = Car(model='Mazda CX7', color='red', year=2018)
print(mazda_car.model, mazda_car.color, mazda_car.year)

bmw_car = Car(model='BMW Z-800', color='blue', year=2020)
print(bmw_car.model, bmw_car.color, bmw_car.year)
