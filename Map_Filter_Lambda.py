# map()
#
# def sum_of_two_num(x):
#     return x + x
#
#
# num_list = [1, 2, 3, 4, 5, 6, 7]


#
# result = map(sum_of_two_num, num_list)
# print(result)
# #
# # for item in result:
# #     print(item)
#
# for item in map(sum_of_two_num, num_list):
#     print(item)
#
# print(list(map(sum_of_two_num, num_list)))
#

# def is_a_in_string(string):
#     if 'a' in string:
#         print('String has \'a\' ')
#         return True
#     else:
#         print('String has not "a".')
#         return False
#
#
# string_list = ['Hello', ' Hey', 'Hi', 'Salom']
# print(list(map(is_a_in_string, string_list)))

# filter()

# num_list = [1, 2, 3, 4, 5, 6, 7]
#
#
# def is_number_odd(num):
#     return num % 2 == 1

#
# print(filter(is_number_odd, num_list))
# print(list(filter(is_number_odd, num_list)))
#
# for num in filter(is_number_odd, num_list):
#     print(num)
#
#
# def is_a_in_string(string):
#     if 'a' in string:
#         print('String has \'a\' ')
#         return True
#     else:
#         print('String has not "a".')
#         return False
#
#
# string_list = ['Hello', ' Hey', 'Hi', 'Salom', 'Hahaha']
# print(list(filter(is_a_in_string, string_list)))

# Lambda expression

num_list = [1, 2, 3, 4, 5, 6, 7]


# def cube(number):
#     return number ** 3
#
#
# print(list(map(cube, num_list)))

# print(list(map(lambda number: number ** 3, num_list)))


def is_number_odd(num):
    return num % 2 == 1


print(list(filter(lambda number: number % 2 == 1, num_list)))
print(list(map(lambda number: number % 2 == 1, num_list)))
print(list(filter(lambda number: number % 2 == 0, num_list)))

string_list = ['Hello', ' Hey', 'Hi', 'Salom', 'Hahaha']
print(list(map(lambda string: string[-1], string_list)))
print(list(map(lambda string: string[::-1], string_list)))


def square(num):
    return num * num


nums = [1, 2, 3, 4, 5]
mapped = map(square, nums)
print(*nums)
print(*mapped)

list_a = [1, 2, 3]
list_b = [10, 20, 30]

print(list(map(lambda x, y: x + y, list_a, list_b)))

