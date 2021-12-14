# Built-in functions
# x = print('Hello')
# y = set()
# print(type(x))
# print(type(y))
# print(x)
# print(y)
# # Built-in methods
#
# my_list = [1, 2, 3, 4]
# my_list.append(5)
# print(my_list)
# my_list.clear()
# print(my_list)

# def print_greeting():
#     '''
#     Prints 'Hello'
#     :return: None
#     '''
#     print('Hello')
#
#
# print_greeting()
#
# # Recieves description of function
#
# help(print_greeting)
# def greeting_with_name(name='Name'):
#     '''
#     :param: Name
#     :return: None
#     '''
#     print('Hello ' + name + '!')
#
#
# help(print(greeting_with_name))
# greeting_with_name()
# greeting_with_name('Alisher')
# x = greeting_with_name('Jane')
# print(x)


# def sum_of_two(x=0, y=0):
#     '''
#
#     :param x:first addend
#     :param y:second addend
#     :return: sum of x and y
#     '''
#     return x + y
#
#
# print(sum_of_two(4, 5))
# a = sum_of_two(7, 12)
# print(a)
#
# help(sum_of_two)

# def hello_in_text(text):
#     if 'hello' in text.lower():
#         return True
#
#     else:
#         return False
#
#
# x = hello_in_text('Say Hello to everyone , Hello')
# print(x)

# def hello_in_text(text):
#     return 'hello' in text.lower()
#
#
# x = hello_in_text('Say Hello to everyone , Hello')
# print(x)
#
#
# def is_string_in_text(string, text):
#     return string in text
#
#
# print(is_string_in_text('he', 'The apple'))
#
#
# def greeting_depends_on_gender(name, gender):
#     if gender == 'male':
#         print('Hello, ' + name + '! You look great.')
#         return gender
#     elif gender == 'female':
#         print('Hello, ' + name + '! You are so beautiful.')
#         return gender
#     else:
#         print('Hello, ' + name + '!I\'ve never seen people like you.')
#         return gender
#
#
# returned_value = greeting_depends_on_gender('Gosha', 'trance')
# returned_value1 = greeting_depends_on_gender('Petya', 'male')
# returned_value2 = greeting_depends_on_gender('Manya', 'female')
# print(returned_value, returned_value1, returned_value2)

# def cat_voice():
#     print('Meow!')
#
#
# def dog_voice():
#     print('Woof!')
#
#
# cat_voice()
# dog_voice()
#
#
# def cat_voice():
#     return 'Meow!'
#
#
# def dog_voice():
#     return 'Woof!'
#
#
# print(cat_voice() * 2)
# print(dog_voice() * 2)
#
#
# def get_voice(text):
#     return text + ' !'
#
#
# print(get_voice('Hello'))
#
#
# def is_odd(a, b):
#     list_of_nums = list(range(a, b + 1))
#     odd_list = []
#     for num in list_of_nums:
#         if num % 2 == 1:
#             odd_list.append(num)
#     return odd_list
#
#
# print(is_odd(3, 7))
#
#
def is_odd_comp(a, b):
    nums_list = list(range(a, b + 1))
    odd_list_1 = [num for num in nums_list if num % 2 == 1]
    return odd_list_1


print(is_odd_comp(4, 12))


one = {3, 6, 4, 1, 6}
two = {10, 4, 5, 11, 1}
print(one.intersection(two))
