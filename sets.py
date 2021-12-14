rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}
print(rainbow_colors)
print(type(rainbow_colors))

empty = {}
print(type(empty))
empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1, 1, 45, 2, 3, 45, 53]
text_tuple = ('stop', 'were', 'kung-fu', 'karate', 'kung-fu', 'football')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)
set_from_list.add(273)
set_from_tuple.add('basketball')

print(set_from_tuple)
print(set_from_list)

x = set_from_list.pop()
y = set_from_tuple.pop()
print(y)

print(set_from_tuple)
print(set_from_list)
print(x)

set_from_list.remove(273)
set_from_tuple.remove('were')
# 'remove' does not return anything
set_from_list.discard(45)
# set_from_list.remove(45)
set_from_list.discard(45)
print(set_from_tuple)
print(set_from_list)

set_from_list.clear()
print(set_from_list)

text_set = set('A set is a mutable collection of distinct hashable objects, same as the list and tuple.')

print(text_set)
print(type(text_set))
