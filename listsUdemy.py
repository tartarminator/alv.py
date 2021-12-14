some_list = [21.32, 'Hello', 234.56, 34.43]
print(len(some_list))
print(some_list[:2])
print(some_list[1])
some_list[2] = 'Eeeeeeey'
print(some_list)
another_list = [23.456, 65.74, 'Guimplen', 547]
new_list = some_list + another_list
print(new_list)
# adding and removing items

# new_list.append(234.43)
# new_list.pop(2)
# print(new_list)
# new_list.pop()  # deleting last object
# print(new_list)
new_list.insert(3, 'EEEEEEEEeeeeyu')
new_list.insert(0, 'start')
print(new_list)
deleted_item = new_list.pop()
print(deleted_item)
print(new_list)
new_list.remove(34.43)
new_list.remove('Hello')
deleted_item = new_list.remove('start')
print(deleted_item)
new_list.reverse()
print(new_list)

num_list = [23, 45, -74, 12.567, 86]
print(len(num_list))
let_list = ['a', 'w', 'r', 't', 'm']
print(num_list + let_list)

x = num_list.sort()  # None nothing returns
new_num_list = num_list  # will return sorted list
print(new_num_list)
y = let_list.sort()  # None //////////////
new_let_list = let_list  # returns sorted list
print(new_let_list)

print(x)
print(y)
print(num_list + let_list)
new_num_list.reverse()
new_let_list.reverse()
print(new_num_list + new_let_list)

new_let_list.append(new_num_list)
print(new_let_list)
list = [2, -23.54, 'Hello', 123.321, 'Python', 67.92]
corrected_list = list[:3]
print(corrected_list)


lst = [5]
lst *= 3
lst[0] = 0
lst[2] = 10
print(sum(lst))
