# for x in range(3, 15, 3):
#     print(x)
#
# print(range(5))
# print(list(range(9)))
#
# letter_index = 0
# my_string = 'Alisherka'
# for letter in my_string:
#     print(letter + ' is at index ' + str(letter_index))
#     letter_index += 1
#
# for index, letter in enumerate(my_string):
#     print(letter + ' is at index ' + str(index))

# print('a' in 'Alisherka')
# print('u' in 'Alisherka')
# print(str(1) in 'Alisherka')
# print('1' in 'Alish')
#
# letter_list = ['a', 'b', 'c', 'd', 'f', True]
# print('a' in letter_list)
# print(1 in letter_list)
# print(True in letter_list)
#
# dict_1 = {1: 'Vasya', 2: 'Petya', 3: 'Ambros'}
# print(2 in dict_1)
# print(1 in dict_1.keys())
# print(4 in dict_1.keys())
# print('Vasya' in dict_1.values())
#
# print(min(1, 34, 72, 41, -23))
# print(max(1, 34, 72, 41, -23))
# my_list = [1, 34, 72, 41, -23]
# print(min(my_list))
# print(max('Alish'))
# for letter in 'Alish':
#     print(ord(letter))

from random import shuffle
my_list = [1, 34, 72, 41, -23]
shuffle(my_list)
print(my_list)

from random import randint
print(randint(1, 21))

