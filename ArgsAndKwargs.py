# *Args and **Kwargs

# *args

# def func_with_args(*args):
#     print(args)
#
#
# func_with_args(2, 3, 15, 29)


# def ten_percent_of_product(x, y, z):
#     return (x * y * z)*0.1
#
#
# print(ten_percent_of_product(10, 20, 7))

# def ten_percent_with_args(*args):
#     product = 1
#     for num in args:
#         product = product * num
#     return product * 0.1
#
#
# print(ten_percent_with_args(10, 20, 7, 15))


# def percent_with_args(percent, *args):
#     product = 1
#     for num in args:
#         product = product * num
#     return product / 100 * percent
#
#
# print(percent_with_args(10, 200))

# **kwargs

# def func_with_kwargs(**kwargs):
#     print(kwargs)
#
#
# func_with_kwargs(first=1, second=2, third=3, fourth=4)

# def hello_with_kwargs(**kwargs):
#     if 'name' in kwargs:
#         print('Hello, nice to meet you, {}'.format(kwargs['name']))
#     else:
#         print('Hello, what is your name? ')
#
#
# hello_with_kwargs(gender='male', age=50, name='Alish')
# hello_with_kwargs(gender='male', age=50)

# def hello_with_greeting_and_kwargs(greeting, **kwargs):
#     if 'name' in kwargs:
#         print('{}, nice to meet you, {}'.format(greeting, kwargs['name']))
#     else:
#         print('{}, what is your name? '.format(greeting))
#
#
# hello_with_greeting_and_kwargs('Hola', gender='male', age=50, name='Alish')
# hello_with_greeting_and_kwargs('Guten Abend', gender='male', age=50)

#
# def func_with_args_and_kwargs(*args, **kwargs):
#     print('{},bring me {} and {} and don\'t spoil my {}.'.format(args[2], kwargs['food'], kwargs['drink'],
#                                                                  kwargs['cloth']))
#
#
# func_with_args_and_kwargs('Jimmy', 'Singh', 'Indus', drink='borman', food='fish', cloth='jeans')


# def is_cat_there(*args):
#     if 'cat' in str(args).lower():
#         return True
#     else:
#         return False
#
#
# print(is_cat_there('Cat', 'dog', 'bird', 'snake'))


# def is_item_here(item, *args):
#     if item in args:
#         return True
#     else:
#         return False
#
#
# print(is_item_here('cat', 'dog', 'snake', 'camel', 'cat'))


def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is {}, but {} is also pretty good!'.format(my_color, kwargs['color']))
    else:
        print('My favorite color is {}, what is your favorite color?'.format(my_color))


your_favorite_color('red', model='Volvo', year=2019, mileage=10000, color='blue')
