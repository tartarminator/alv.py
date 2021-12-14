# greeting = 'Hello!'
# letter_list = []
# # for letter in greeting:
# #     letter_list.append(letter)
# #     print(letter_list)
#
# for letter in greeting:
#     letter_list.append(letter)
# print(letter_list)
# letter_list = [letter for letter in greeting]
# print(letter_list)
# number_list = [number for number in '0123456789']
# print(number_list)
# num_list_1 = [num for num in range(0, 10, 2)]
# print(num_list_1)
# num_list_2 = [num ** 2 for num in range(0, 10)]
# print(num_list_2)
# num_list_3 = [((num+3)/2)**2 for num in range(0, 10)]
# print(num_list_3)

# number_list_more = [6, -42, 21, -7, 81, 15, 0]
# new_list = [number ** 2 / 2 for number in number_list_more if number > 0]
# print(new_list)
# new_list_1 = ['+' if number > 0 else '-' if number < 0 else 'zero' for number in number_list_more]
# print(new_list_1)

# new_list = []
# greetings = ['hello', 'hi', 'hey', 'hola']
# for word in greetings:
#     new_list.append(word[1])
# print(new_list)
#
# new_list_1 = [letter[1] for letter in greetings]
# print(new_list_1)
#
# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# digits_list = []
# for number in digits:
#     if number % 2 == 1:
#         digits_list.append(number)
# print(digits_list)
#
# digits_list_1 = [num for num in digits_list if num % 2 == 1]
# print(digits_list_1)

# Dictionary Comprehension
# num_dict = {'first': 1, 'second': 2, 'third': 3}
# new_dict = {key: value ** 3 for key, value in num_dict.items()}
# print(new_dict)

# number_list = [6, -42, 21, -7, 81, 15, 0]
# number_dict = {number: number ** 2 for number in number_list}
# print(number_dict)
# number_dict = {number: 'positive' if number > 0 else 'negative' if number < 0
# else 'zero' for number in number_list}
# print(number_dict)

# Set comprehension

number_list = [6, -42, 21, -7, 81, 15, 0]
number_set = {number ** 2 for number in number_list}
print(number_set)

number_list = [6, -42, 21, -7, 81, 15, 0]
number_set = {number ** 2 for number in range(0, 15, 3)}
print(number_set)

letter_list = {letter.lower() for letter in 'Hey, Alisher'}
print(len(letter_list))
print(letter_list)
