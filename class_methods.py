class Gamer:
    active_gamers = 0

    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

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
            print('You have access to adult level of the game.')
        else:
            print('You cannot play this game. ')


gamer_1 = Gamer('Tartarminator', 21, 1, 10)
gamer_2 = Gamer('Heavy_Rain', 18, 2, 15)
gamer_3 = Gamer('Young_boy', 15, 1, 1)

print(gamer_1.get_age())
print(gamer_1.get_adult_level_permission())
print(gamer_2.get_age())
print(gamer_2.get_adult_level_permission())
print(gamer_3.get_age())
print(gamer_3.get_adult_level_permission())
print(gamer_1.get_nickname())
