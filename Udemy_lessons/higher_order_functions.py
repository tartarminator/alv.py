# Higher ordered functions, which accepts another functions as arguments

# def products(n, func):
#     result = 1
#     for number in range(1, n):
#         result *= func(number)
#     return result
#
#
# def square(x):
#     return x * x
#
#
# def cube(x):
#     return x * x * x
#
#
# print(products(4, square))
# # 1 2 3
# # 1 4 9
#
# print(products(4, cube))
# # 1 2 3
# # 1 8 27

# def my_function(a, b, func):
#     result = func([a, b])
#     return result
#
#
# print(my_function(2, 4, sum))

# Using nested functions

from random import choice


# def colorize(thing):
#     def get_color():
#         colors = ('red', 'yellow', 'blue', 'green')
#         color = choice(colors)
#         return color
#
#     result = get_color() + ' ' + thing
#     return result
#
#
# print(colorize('pen'))


# Higher ordered functions, which return another functions

# def make_color():
#     def get_color():
#         colors = ('red', 'yellow', 'blue', 'green')
#         color = choice(colors)
#         return color
#
#     return get_color
#
#
# first_color = make_color()
# second_color = make_color()
# third_color = make_color()
#
# print(first_color())
# print(second_color())
# print(third_color())


# Inner function can access outer function scope

def colorize1(thing):
    def get_color():
        colors = ('red', 'yellow', 'blue', 'green')
        color = choice(colors)
        return color + ' ' + thing

    return get_color


print(colorize1('pen')())

colorized_car = colorize1('car')
print(colorized_car())
