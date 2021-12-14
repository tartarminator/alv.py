# Immutable
#
# tuple_1 = (3, 'three', 3.098, 'bratshka', 876)
# tuple_2 = 1, 2, 3, 4
# print(tuple_2)
# print(type(tuple_2))
# print(tuple_1)
# print(tuple_1[0])
# print(tuple_2[-1])
# print(tuple_1[1:3])
#
# new_tuple = (tuple_2[2], tuple_1[2], tuple_1[3], 'Nu kak vi?', 2.34)
# print(new_tuple)

# x = y = z = 12
x, y, z = 12, 11, 10
print(x, y, z)

person_tuple = ('Alisher', 'Vakilov', 1971)
first_name, last_name, year_of_birth = person_tuple[0], person_tuple[1], person_tuple[2]
print(last_name)
print(year_of_birth)
print(first_name, last_name, year_of_birth)

t1 = (54, 34, 75, 1,  86, 12, 1)
print(t1.count(1))
print(t1.index(1))

greetings_tuple = ('Hello', 'Hi', 'Hey', 'Ehehey', 'Hello')
print(greetings_tuple.count('Hola'))
print(t1.index(12))
print(greetings_tuple.index('Hey'))

my_pc = ('Intel@Core', 1000, 8, 'BlueRay', 'NVIDIA')
cpu, hdd, ram, dvd_rom, video = my_pc
print(cpu, hdd, ram, dvd_rom, video)


