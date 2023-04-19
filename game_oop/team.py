from random import randint

from game_oop.names import Names


class Team:
    all_team = list()
    count = 0

    def __init__(self):
        self.__heroes = list()
        self._current_index = 0
        self.__size = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < len(self.__heroes):
            hero = self.__heroes[self._current_index]
            self._current_index += 1
            return hero
        raise StopIteration

    def append(self, hero):
        self.__heroes.append(hero)
        Team.all_team.append(hero)
        Team.count += 1
        self.__size += 1

    def __getitem__(self, key):
        return self.__heroes[key]

    def __contains__(self, hero):
        return self.__heroes.__contains__(hero)

    def fill_team(self, size: int, cls: list, team_side):
        for i in range(size):
            self.append(cls[randint(0, len(cls) - 1)](Names.get_random_name(), team_side))

    @staticmethod
    def fill_teams(first_team, second_team, size: int, cls: list):
        for i in range(size):
            first_team.append(cls[randint(0, len(cls) - 1)](Names.get_random_name(), False))
            second_team.append(cls[randint(0, len(cls) - 1)](Names.get_random_name(), True))

    @property
    def size(self):
        return self.__size

    def filter_visible_team(self):
        live_team = Team()
        live_team.copy(self)
        for hero in live_team:
            if hero.state != "Stand":
                live_team.remove(hero)
        return live_team

    def remove(self, hero):
        self.__heroes.remove(hero)
        self.__size -= 1

    def copy(self, copy_object):
        self.__heroes = copy_object.__heroes.copy()
        self.__size = copy_object.size
