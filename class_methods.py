class Gamer:
    active_gamers = 0

    @classmethod
    def get_active_gamers(cls):
        return Gamer.active_gamers

    @classmethod
    def gamer_from_string(cls, data_string):
        nickname, age, level, points = data_string.split(',')
        return cls(nickname, age, level, points)

    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

    def logout(self):
        Gamer.active_gamers -= 1

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adult_level_permission(self):
        if self.is_adult():
            print(self.nickname + ' you have access to adult level of the game.')
        else:
            print(self.nickname + ' You cannot play this game. You are too young.')


# print(Gamer.active_gamers)

gamer_1 = Gamer('Tartarminator', 21, 1, 10)
# print(Gamer.active_gamers)
gamer_2 = Gamer('Heavy_Rain', 18, 2, 15)
# print(Gamer.active_gamers)
gamer_3 = Gamer('Young_boy', 15, 1, 1)

# print(gamer_1.get_age())
# gamer_1.get_adult_level_permission()
# print(gamer_2.get_age())
# gamer_2.get_adult_level_permission()
# print(gamer_3.get_age())
# gamer_3.get_adult_level_permission()
# print(gamer_1.get_nickname())
# gamer_3.logout()
# print(Gamer.active_gamers)
# print(Gamer.get_active_gamers())
timur = Gamer.gamer_from_string('tima, 34, 12, 41')
murka = Gamer.gamer_from_string('Cathy, 24, 15, 39')
print(timur.get_age())
print(murka.get_level())
print(Gamer.active_gamers)
print(timur.get_nickname())
my_dict = dict.fromkeys((1, 2, 3), ('apple', 'orange', 'lemon'))
print(my_dict)

