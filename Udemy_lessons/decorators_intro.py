# def simple_function():
#     # print('Some code before the old code')
#     print('Simple function code')
#     # print('Some code after the old code')


# simple_function()


def decorator_function(original_function):
    def wrap_function():
        print('Some code before the old code')
        original_function()
        print('Some code after the old code')

    return wrap_function


# decorated_function = decorator_function(simple_function)
# decorated_function()


# @decorator_function
# def simple_function():
#     print('Simple function code')


# simple_function()


def make_compliment(func):
    def wrapper_func(*args, **kwargs):
        print('Nice to meet you!')
        func(*args, **kwargs)
        print('You look great! ')

    return wrapper_func


@make_compliment
def ask_name():
    print('What is your name?')


ask_name()


@make_compliment
def say_name(name):
    print('My name is ' + name)


say_name('Alisher')


@make_compliment
def order(food, drink):
    print(f'Give me {food} and {drink}!')


order(food='Burger', drink='Cola')
