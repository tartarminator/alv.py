from functools import wraps
import time

# def check_if_first_arg_is(value):
#     def inner_dec(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if args and args[0] != value:
#                 print(f'First argument has to be {value}!')
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return inner_dec
#
#
# @check_if_first_arg_is('red')
# def print_rainbow_colors(*colors):
#     print(colors)
#
#
# print_rainbow_colors('violet', 'red', 'blue', 'yellow', 'green', 'orange')
#
#
# @check_if_first_arg_is(7)
# def multiply_7(a, b):
#     return a * b
#
#
# print(multiply_7(6, 5))


# def enforce(*types):
#     def inner_dec(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             new_args = []
#             for a, t in zip(args, types):
#                 new_args.append(t(a))
#             return func(*new_args, **kwargs)
#
#         return wrapper
#
#     return inner_dec
#
#
# @enforce(str, int)
# def print_text_n_times(text, n):
#     for number in range(n):
#         print(text)
#
#
# print_text_n_times('Hello!', '4')


# *args - ('Hi', '3')
# *types - (str, int)
# zip(args, types)-('Hi' str)('3' int)

# @enforce(float, float)
# def divide(a, b):
#     return a / b


# print(divide(4, 7))
# print(divide('4', '7'))


# y = list(filter(lambda x: bool((x + 1) % 2), range(10)))
# print(y[2])


lst = [1, 2, 3]
a, b, c = lst
print(a + b + c)


def pause_execution(pause_time):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(pause_time)
            print(f'There was a pause {pause_time} seconds before execution {func.__name__}')
            return func(*args, **kwargs)

        return wrapper

    return inner


@pause_execution(5)
def divide(a, b):
    return a / b


print(divide(522, 17))

nums = (55, 44, 33, 22)
print(max(min(nums[:-2]), abs(-42)))
