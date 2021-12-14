# Immutable
# first_name = "Jake"
# first_two_letters = first_name[:2]
# last_letter = first_name[-1:]
# new_name = first_two_letters + "n" + last_letter
# print(new_name)
#
# # Multiplication
#
# yummy = "Yum "
# print(yummy.upper() * 6)
# print(yummy.upper() * 7)
#
# long_string = "This is the long string."
# print(long_string.split())
# print(long_string.split('s'))
# print(long_string.split('i'))
# # Formating
#
# name = 'Jack'
# age = 23
# name_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
# print(name_age)
# name_age = 'My name is {0}. I\'m {1} years old.'.format('Jack', '23')
# print(name_age)
#
# week_days = 'There are 7 days in a week: {3}, {1}, {6}, {0}, {4}, {5}, {2}.' \
#     .format('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# print(week_days)
#
# week_days = 'There are 7 days in a week: {mo}, {wed}, {fr}, {tu}, {th}, {sa}, {sun}.' \
#     .format(mo='Monday', tu='Tuesday', wed='Wednesday', th='Thursday', fr='Friday', sa='Saturday', sun='Sunday')
# print(week_days)


# float_result = 1000/7
# print(float_result)
# print('The result of division is {0:1.3f}'.format(float_result))
#
# print('''
#  {0:10.2f} {1:10.2f} {2:10.2f}
#  {3:10.2f} {4:10.2f} {5:10.2f}
#  {6:10.2f} {7:10.2f} {8:10.2f}
# '''.format(1.234, 227.22345, 34.234, 1234.4, 2345.1, 1.234, 227.22345, 34.234, 1234.4))
print('''
 {0:15.4f}{1:15.4f}{2:15.4f}{3:15.4f}
 {4:15.4f}{5:15.4f}{6:15.4f}{7:15.4f}
'''.format(1245.5678, 4356.0986, 546.9876, 43.76543, 54.76543, 453.98765, 764.876, 12.212121))



name = 'Jack'
age = 23
name_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_age)
name_age = f'My name is {name}. I\'m {age} years old.'
print(name_age)

