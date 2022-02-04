def say_good_bye():
    print('Good bye!')


def say_bye_bye():
    print('Bye-Bye!')


def say_hasta_lavista():
    print('Hasta Lavista!')


# from itertools import count, accumulate, takewhile, product, permutations
#
# for i in count(3):
#     print(i)
#     if i >= 11:
#         break

# nums = list(accumulate(range(9)))
# print(nums)
# print(list(takewhile(lambda x: x <= 6, nums)))
#
# letters = ('A', 'B')
# print(list(product(letters, range(2))))
# print(list(permutations(letters)))
#
# a = {1, 2}
# print(len(list(product(range(3), a))))


nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))


def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)


print(power(2, 3))

num = int(input('Input a number:'))


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


for i in range(num):
    print(fibonacci(i))
