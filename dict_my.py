# car_prices = {'opel': 8000, 'toyota': 5000, 'bmw': 10000}
# print(car_prices)
# print(car_prices['opel'])
# car_prices['Mazda'] = 4000
# print(car_prices)
# car_prices['opel'] = 3000
# print(car_prices['opel'])
# del car_prices['bmw']
# print(car_prices)
# car_prices.clear()
# print(car_prices)

person = {
    'first name': 'Alisher',
    'last name': 'Vakilov',
    'age': 50,
    'hobbies': ['football', 'guitar', 'photo'],
    'children': {'son': 'Michael', 'daughter': 'Camilla'}
}
print(person['children'])
print(person['age'])
print(person['hobbies'])
hobbies = person['hobbies']
print(hobbies)
print(hobbies[2])
print(person['hobbies'][2])
children = person['children']
print(children['son'])
print(person['children']['daughter'])
person['car'] = 'Mazda'
print(person)
person['hobbies'][1] = 'singing'
print(person['hobbies'])
print(person.keys())
print(person.values())
print(person.items())

car = {
    'year': 2010,
    'color': 'white',
    'model': 'bmw',
    'mileage': 100000
}
print(car['mileage'])

personal_computer = {
    'CPU': 'Intel Core',
    'memory': 1000,
    'DDR_memory': 8,
    'video': 'NVIDIA 1050',
    'display': 17
}
print(personal_computer)