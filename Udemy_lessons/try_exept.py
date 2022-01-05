# print('Some code.')
# print(my_code)
# print(len(23))
# try:
#     # print(my_code)
#     print(len(23))
# except NameError:
#     print('NameError has happen.')
# except TypeError:
#     print('TypeError has happen.')
# print('Code after error.')

user_dictionary = {'first_name': 'Alisher', 'last_name': 'Vakilov', 'age': 50}


# print(user_dictionary['last_name'])
# print(user_dictionary['name'])

# print(user_dictionary.get('last_name'))
# print(user_dictionary.get('name'))

def get_dictionary_value(dictionary, key):

    '''
    If dictionary hasn't specified key, the function returns None
    :param dictionary:
    :param key:
    :return:
    '''
    try:
        return dictionary[key]
    except KeyError:
        return None

print(get_dictionary_value(user_dictionary, 'age'))
print(get_dictionary_value(user_dictionary, 'name'))
print(get_dictionary_value(user_dictionary, 'first_name'))
