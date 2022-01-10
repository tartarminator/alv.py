# Higher ordered functions, which accepts another functions as arguments

def products(n, func):
    result = 1
    for number in range(1, n):
        result *= func(number)
    return result


def square(x):
    return x * x


print(products(4, square))
