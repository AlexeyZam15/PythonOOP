from random import randint

from game_oop.names import Names


class Team:
    all_team = list()
    count = 0

    def __init__(self):
        self.__heroes = list()
        self._current_index = 0

    def __iter__(self):
        self._current_index = 0
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

    def filter_visible(self):
        live_team = Team()
        live_team.copy(self)
        for hero in self:
            if hero.state != "Stand":
                live_team.remove(hero)
        return live_team

    def remove(self, hero):
        self.__heroes.remove(hero)

    def copy(self, copy_object):
        self.__heroes = copy_object.__heroes.copy()

    def has_live_ally(self, class_name: str):
        for hero in self.__heroes:
            if hero.class_name == class_name and hero.state == "Stand":
                return True
        return False

    def get_live_ally(self, class_name: str):
        for hero in self.__heroes:
            if hero.class_name == class_name and hero.state == "Stand":
                return hero
        return self

    def has_injured_hero(self):
        for hero in self:
            if hero == self:
                continue
            if hero.max_hp > hero.hp:
                return True
        return False

    def get_lowest_hp_hero(self):
        max_hp_diff = self[0].hp_diff
        lowest_hp_hero = self[0]
        for hero in self:
            if max_hp_diff < hero.hp_diff:
                max_hp_diff = hero.hp_diff
                lowest_hp_hero = hero
        return lowest_hp_hero

    def filter_live(self):
        live_team = Team()
        live_team.copy(self)
        for hero in self:
            if hero.state == "Dead":
                live_team.remove(hero)
        return live_team

    def __len__(self):
        return len(self.__heroes)
