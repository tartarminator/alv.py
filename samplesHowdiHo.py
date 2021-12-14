def howdi_ho():
    '''Описание функции'''
    print(howdi_ho.__doc__)


howdi_ho()


def howdiHo(name):
    print('Egegey ' + name() + '!')


test = howdiHo


def read_name():
    return ' :::' + input('Введите Ваше имя: ') + ':::'


test(read_name)


def shout(word):
    return word + '!'


speak = shout
output = speak('shout')
print(output)
