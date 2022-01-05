# If we have an error - except block fires and else block doesn't  fire
# If we haven't an error - else block fires and except block doesn't  fire
# Finally block fires anyway

# while True:
#     try:
#         number = int(input('Enter any number: '))
#         print(number/2)
#
#     except:
#         print('You have to enter a number')
#     else:
#         print('Well done, this is a number')
#         break
#     finally:
#         print('Finally block')
#
#     print('Code after an error handling.')


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        print('You can\'t divide by zero!')
        print(e)
    except TypeError as e:
        print('x and y must be  numbers!')
        print(e)
    else:
        print('x has been divided by y!')
    finally:
        print('Finally block')

print(divide(21, 0))
print(divide(2, 'ah'))


