# x = 5
# while x >= 1:
#     print(str(x) + ' Hello')
#     x -= 1
# while x <= 10:
#     print(x)
#     x += 2
# print('Next code!')
# x = 0
# while x < 10:
#     print(f'{x} is less than 10.')
#     x += 2
# else:
#     print(f'{x} more or equal than 10.')
#
# for x in range(11):
#     print(f'{x} is less than 11.')
# else:
#     x += 2
#     print(f'{x} more than 10.')

# break, continue, pass

my_list = [1, 2, 3, 4]
# for item in my_list:
#     pass
# print('Another code!')

for item in my_list:
    if item == 4:
        break
    print(item)
print('Another code')
for item in my_list:
    if item == 3:
        continue
    print(item)
print('Another code')



