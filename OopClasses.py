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

# class Car:
#     wheels_numbers = 4
#
#     def __init__(self, model, color, year, is_crashed):
#         self.model = model
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
#
# mazda_car = Car(model='Mazda CX7', color='red', year=2018, is_crashed=True)
# print(mazda_car.model, mazda_car.color, mazda_car.year, mazda_car.is_crashed)
# print(mazda_car.wheels_numbers)
# bmw_car = Car(model='BMW Z-800', color='blue', year=2020, is_crashed=False)
# print(bmw_car.model, bmw_car.color, bmw_car.year, bmw_car.is_crashed)
# print(type(bmw_car))
# print(bmw_car.wheels_numbers)
#
# num_of_wheels_3_pc = Car.wheels_numbers * 3
# print(num_of_wheels_3_pc)


class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes


first_blog = BlogPost(user_name='Andrew', text='Hi everybody!!!', number_of_likes=100)
second_blog = BlogPost(user_name='Neville', text='Hello lady and gentelmen!', number_of_likes=120)

first_blog.number_of_likes = 110
print(first_blog.number_of_likes)
print(second_blog.number_of_likes)
