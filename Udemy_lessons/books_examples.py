# name = "John"
# print(f"Hello {name}")
# print("Hello {}, you are {} years old!".format(name, 28))
#
# name = "john smith"
# print(name.title())
# print(name.lower())
# print(name.upper())
# print(name.split())
# print(name.find('n'))
# print(name.__len__())
# print(name.__add__('abc'))
#
# words = 'Hello guys!'
# print(words)
# print(words.replace('guys', 'lady and gentlemen!'))
# s = ' Look over that way  '
# print(s.find('way'))
# print(s.replace('way', 'road'))
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())
# b = s.split()
# print(b[2])
# print(words.upper())
# print(words.upper)


p1_name, p1_price = 'Books', 49.95
p2_name, p2_price = 'Computer', 579.99
p3_name, p3_price = 'Monitor', 124.89

company_name = 'vakilov&Galimov brothers inc.'
company_address = 'qora-Qamish 2/5 10'
company_city = 'tashkent, UZ'

message = 'Thanks you for shopping with us.'

print('*' * 60)
print('&' * 60)
print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_city.title()))
print('=' * 60)
print('\tProduct name\t\tProduct Price')
print('\t{}\t\t\t\t${}'.format(p1_name.title(), p1_price))
print('\t{}\t\t\t${}'.format(p2_name.title(), p2_price))
print('\t{}\t\t\t\t${}'.format(p3_name.title(), p3_price))
print('=' * 60)

total = p1_price + p2_price + p3_price
print('\t\t\t${}'.format(total))
print('=' * 60)
print('\n\t{}\n'.format(message))

print(''.join(reversed(message)))
print('*'.join(message))

# my_lst = ['Hello', 'my friends', 'where', 'are', 'you', '?']
# print(my_lst.append('!'))
# my_lst.insert(1, 'lady and gentlemen')
#
# print(my_lst[::-1])
# print(' '.join(my_lst[:3].__reversed__()))
# print(' '.join(my_lst[:3]))
#
# print(my_lst)
# x = my_lst.pop()
# print(x)
# print(my_lst)
# my_lst.remove(my_lst[-1])
# print(my_lst)
# my_lst.insert(6, '?!')
# print(my_lst)
# print(' '.join(my_lst))
# print('+++', my_lst, '+++', x)
# my_lst.remove(my_lst[-1])
# y = ' '.join(my_lst)
# print('+++', y, '+++', x)

nums = [12, 24, 71, 12, 45]
print(min(nums))
print(max(nums))
print(sum(nums))


sorted_nums = sorted(nums)
print(sorted_nums)
sorted_nums.remove(sorted_nums[0])
print(sorted_nums)

names = ["Bob", "Jack", "Rob", "Bob", "Robert"]
while "Bob" in names:
    names.remove("Bob")

print(names)

x = -42.85
abs_x = abs(x)
print(f"Абсолютное значение {x} это {abs_x}")


txt = 'this is an awesome text'
l = txt.split()
print(l)
long_word = ''
for word in l:
    if len(word) > len(long_word):
        long_word = word

print(long_word)