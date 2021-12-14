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
    def __init__(self, model, color, year, is_crashed):
        self.model = model
        self.color = color
        self.year = year
        self.is_crashed = is_crashed


mazda_car = Car(model='Mazda CX7', color='red', year=2018, is_crashed=True)
print(mazda_car.model, mazda_car.color, mazda_car.year, mazda_car.is_crashed)

bmw_car = Car(model='BMW Z-800', color='blue', year=2020, is_crashed=False)
print(bmw_car.model, bmw_car.color, bmw_car.year, bmw_car.is_crashed)
print(type(bmw_car))

