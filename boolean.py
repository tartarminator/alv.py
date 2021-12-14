# print(1 < 2)
#
# print(type(True))
# print(type(False))
# # Comparison operators
#
# print(1 == 1)
# print(1 == 2)
# print('Hello' == 'Hello')
# print('Hello' == 'hello')

# print(1 != 1)
# print(1 != 2)
# print('Hello' != 'Hello')
# print('Hello' != 'hello')
#
# age = int(input('Input your age'))
# print('Your age is ', age)
# print('Access is permitted: ' + str(age >= 18))
#
# print(1 < 2)
# print(1 > 2)
# print(1 >= 2)
# print(1 <= 2)
# print(1 == 2)
# print(1 != 2)

# print('A' < 'a')
# print(ord('A'))
# print(ord('a'))
#
# letters = ['H', 'h']
# print(letters[0] > letters[1])
# print(ord(letters[0]), ord(letters[1]))


x = 1
y = 2
# print(x > y)
# print(x < y)

# and, or, not
# print(x > 1 and y > 1)
# print(x > 1 or y > 1)
# print(not x > 1)

print(True and True)
print(True or True)
print(not True)

print(False and False)
print(False or False)
print(not False)

print(True and False)
print(True or False)

name = 'Alisher'
age = 50
is_married = False
if age > 18 and is_married == False:
    print('Hi {}, now you can find lyanga here.'.format(name))
else:
    print('Senga mumkun emas ' + name + ' Hali yosh san, bratshka.')
