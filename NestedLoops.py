smile = '\U0001f600'
# for i in range(1, 11):
#     print(str(i) + ' ' + smile * i)

# for number in range(10):
#     count = 0
#     emoticons = ' '
#     while count <= number:
#         emoticons += smile
#         count += 1
#     print(emoticons)

# for number in range(10):
#     emoticons = ' '
#     for count in range(number + 1):
#         emoticons += smile
#     print(emoticons)

# count = 1
# while count < 11:
#     print(str(count) + ' ' + smile * count)
#     count += 1

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13]]
# print(nested_list)
# print(len(nested_list))
# print(len(nested_list[2]))
# print(len(nested_list[-1]))
# print(nested_list[1][2])
# print(nested_list[3][2])
# print(nested_list[-1][2])
# print(nested_list[-1][-2])

# print nested_list

nested_list = [[1, 2, 3, True], [4, 5, 6, 'Hello'], [7, 8, 9, False], [10, 11, 12, 13, 'Hey!']]

# for inner_list in nested_list:
#     print(inner_list)
#
# for inner_list in nested_list:
#     for number in inner_list:
#         print(number)

[[print(number) for number in inner_list] for inner_list in nested_list]
