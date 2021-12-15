class Gamer:
    active_gamers = 0

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
            print(self.nickname + ' you are ' + str(self.age) + ' years old  and  have access to adult level of the '
                                                                'game.')
        else:
            print(self.nickname + ' You cannot play this game. You are too young.')


print(Gamer.active_gamers)

gamer_1 = Gamer('Tartarminator', 21, 1, 10)
print(Gamer.active_gamers)
gamer_2 = Gamer('Heavy_Rain', 18, 2, 15)
print(Gamer.active_gamers)
gamer_3 = Gamer('Young_boy', 15, 1, 1)

print(gamer_1.get_age())
gamer_1.get_adult_level_permission()
print(gamer_2.get_age())
gamer_2.get_adult_level_permission()
print(gamer_3.get_age())
gamer_3.get_adult_level_permission()
print(gamer_1.get_nickname())
gamer_3.logout()
print(Gamer.active_gamers)
