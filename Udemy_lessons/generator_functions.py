# Generators are iterators
# Generators can be created with generator functions
# Generators can be created with geberator expressions

# def my_function(x):
#     return x
#
# print(my_function(2))

def count_up_to(x):
    count = 1
    while count <= x:
        yield count
        count += 1


print(count_up_to(4))
counter = count_up_to(4)
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(next(counter))
# print(next(counter))
# print(next(counter))

# counter = count_up_to(10)
# print(list(count_up_to(7)))

# for number in counter:
#     print(number)

# counter.__next__()
# counter.__next__()
#
# for number in counter:
#     print(number)

#
# def get_week_day():
#     week = [
#         'Sunday',
#         'Monday',
#         'Tuesday',
#         'Wednesday',
#         'Thursday',
#         'Friday',
#         'Saturday'
#     ]
#     for day in week:
#         yield day
#
# today = get_week_day()
#
# print(today.__next__())
# print(today.__next__())
# print(today.__next__())
# print(today.__next__())
# print(today.__next__())
# print(today.__next__())
# print(today.__next__())


def even_odd():
    string = 'even'
    while True:
        yield string
        if string == 'even':
            string  = 'odd'
        else:
            string = 'even'



even_odd_generator = even_odd()
print(next(even_odd_generator))
print(next(even_odd_generator))
print(next(even_odd_generator))
print(next(even_odd_generator))



def fibonacci(xterms):
    # первые два условия
    x1 = 0
    x2 = 1
    count = 0

    if xterms <= 0:
        print("Укажите целое число больше 0")
    elif xterms == 1:
        print("Последовательность Фибоначчи до", xterms, ":")
        print(x1)
    else:
        while count < xterms:
            xth = x1 + x2
            x1 = x2
            x2 = xth
            count += 1
            yield xth



fib = fibonacci(5)

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

# str = 'pfrhtgktybt vfnthbfkf'
# def func():
#     str = '*проверка*'
#     def enclosed():
#         print(str, end=' ')
#     enclosed()
# func()
# print(str, end=' ')
